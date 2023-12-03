from dataclasses import dataclass
@dataclass
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str
    test_file_path:str
@dataclass
class DataValidationArtifact:
    report_file_path:str

@ dataclass    
class DataTransformationArtifact:
    transform_object_path:str
    transfored_train_path:str
    transfored_test_path:str
    targate_encoder_path:str


class ModelTrainerArtifact:...
class ModelEvalutionArifact:...
class ModelTrainerArtifact:...