from setuptools import setup, find_packages

def get_requirements(file_path):
    HYPHEN_E_DOT = '-e .'
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/aaravmat1209/ml_projects',
    author='Aarav Matalia',
    install_requires=get_requirements('requirements.txt'),
)

