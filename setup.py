from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Read the requirements.txt file and return a list of requirements."""
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines= file.readlines()
            for line in lines:
                requirement = line.strip()

                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Sujeevan',
    author_email="yogarajansujeevan2002@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)