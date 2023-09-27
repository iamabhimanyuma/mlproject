from setuptools import find_packages,setup

def get_requirements(file_path):
    with open(file_path,'r') as file_obj:
        requirements = file_obj.readlines()
        requirements=[str(req.replace('\n','')) for req in requirements if req!='-e .']
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Abhimanyu',
    author_email='abhimanyuma75@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )