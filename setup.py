from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

with open('License.md', 'r') as f:
    license = f.read()

    
setup(
    name='fasthelp',
    version='1.0.13',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.26',
        'pandas>=2.2'
],
    author='Ziyan Zhou',
    author_email='unknownuserfrommars@protonmail.com',
    description = "A Python Helper",
    long_description=long_description, 
    long_description_content_type='text/markdown',
    url='https://www.github.com/Unknownuserfrommars/fasthelp',
    maintainer="Unknownuserfrommars",
    maintainer_email="unknownuserfrommars@protonmail.com",
    license=license
)
