from sensor.entity import artifact_entity,config_entity
from sensor.exception import SensorException
from sensor.logger import logging
from scipy.stats import ks_2samp
from typing import Optional
import os,sys
import pandas as pd
from sensor import utils
import numpy as np



class DataValidation:


    def __init__(self,
                    data_validation_config:config_entity.DataValiadationConfig,
                    data_ingestion_artifact:artifact_entity.DataIngestionArtifact):
        try:
            logging.info(f"{'>>'*20} Data Validation {'<<'*20}")
            self.data_validation_config=data_validation_config
            self.Validation_error=dict()
        except Exception as e:
            raise SensorException(error_message=e, error_detail=sys)
    
    
    def drop_missing_values_columns(self,df:pd.DataFrame,)->Optional[pd.DataFrame]:
       """
       This function will drop column which contains missing value more than specified threshold

        df: Accepts a pandas dataframe
        threshold: Percentage criteria to drop a column
        =====================================================================================
        returns Pandas DataFrame if atleast a single column is available after missing columns drop else None
       """
       try:
           threshold=self.self.data_validation_config.missing_threshold
           null_report=df.isna().sum()/df.shape[0]
           ## selecting column name which has contain null values
           drop_column_names=null_report[null_report>threshold].index
           self.Validation_error["droppedcolums"]=drop_column_names
           df.drop(list(drop_column_name),axis=1,inplce=True)
           ## return None no columns left
           if len(df.columns)==0:
               return None
           return df


       except Exception as e:
           raise SensorException(e, sys)


    def is_required_columns_exits(self,base_df:pd.DataFrame,present_df:pd.DataFrame)->bool:
        try:
            
            base_columns=base_df.columns
            current_columns=current_df.columns
            missing_columns=[]
            for base_column in base_columns:
                if base_column not in current_columns:
                    missing_columns.append(base_column)

            if len(missing_columns)>0:
                self.Validation_error["missing columns"]=missing_columns
                return False
            return True

        except Exception as e:
            raise SensorException(e, sys)


    def data_drift(self,base_df:pd.DataFrame,current_df:pd.DataFrame):
        try:
            drift_report=dict()
            base_columns=base_df.columns
            current_columns=current_df.columns
            
            for base_column in base_columns:
                base_data,current_data=base_df[base_column],current_df[base_column]
                ## Null hypothesis is that both column data drawn from same distribution
                same_distribution=ks_2samp(base_data, current_data)

                if same_distribution.pvalue>0.05:
                    ## We are acceting null hypothesis
                    drift_report[base_column]={
                        "pvalues":same_distribution.pvalue,
                        "same_disribution":True
                    }
                ## same distribution
                else:
                    drift_report[base_column]={
                        "pvalues":same_distribution.pvalue,
                        "same_distribution":False
                    }
                ## Diffrent distribution


        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_validation(self)->artifact_entity.DataValidationArtifact:
        try:
            base_df=pd.read_csv(self.data_validation_config.base_file_path)
            base_df.replace({"na":np.NAN},inplace=True)
            ## base_df has na null
            base_df=self.drop_missing_values_columns(df=base_df)
        except Exception as e:
            raise SensorException(e,sys)