from setuptools import find_packages, setup
from typing import List
# This is the setup file for a machine learning project.
# It contains the metadata and dependencies required for the project.
# The file is used to package the project and make it installable.
# -e . is used to install the package in editable mode, which allows changes to the code to be reflected without reinstalling.

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path) -> List[str]:
    """
    This function will return the list of requirements
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='ML project',
    version='0.0.1', 
    author='Koushik',
    author_email='bandikoushi781@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)