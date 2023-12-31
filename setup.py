from setuptools import find_packages,setup

from typing import List

REQUIREMENTS_FILE_NAME="requirements.txt"
HYPEN_E_DOT="-e ."

def get_requirements()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list=requirement_file.readlines()
    requirement_list=[requirement_name.replace("\n","")for requirement_name in requirement_list]
    if HYPEN_E_DOT in requirement_list:
        requirement_list.remove(HYPEN_E_DOT)
    return requirement_list


setup(
    name="sensor",
    version="0.0.1",
    author="sachin",
    author_email="sachinmane1222@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)