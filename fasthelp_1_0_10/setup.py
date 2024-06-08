from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

    
setup(
    name='fasthelp',
    version='1.0.10',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.26',
        'pandas>=2.2'
],
    author='Ziyan Zhou',
    author_email='unknownuserfrommars@protonmail.com',
    description = "A Python Helper",
    long_description=long_description, 
    long_description_content_type='text/markdown'
)
