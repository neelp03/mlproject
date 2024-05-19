from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    Read the requirements file and return list of requirements    
    '''
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.read().splitlines()
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Neel Patel',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
