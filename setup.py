from setuptools import setup, find_packages

# Read the README.md for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="fasthelp",
    version="1.2.0a2",
    author="FastHelp Dev Team",
    description="A fast and useful helper in Python. It just makes things much faster.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Unknownuserfrommars/fasthelp", 
    packages=find_packages(),  # Automatically finds all subpackages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",  # Ensure compatibility with your required Python version
    install_requires=[
        "numpy>=1.26",
        "pandas>=2.2",
        "openai>=1.51",
        "python-docx>=1.1.0",
        "python-pptx>=1.0.0",
        "distro>=1.9.0",
        "psutil>=6.0.0",
        "packageimporter>=1.4.0",
        "plotly>=5.10.0",  # Required for plots
    ],
    include_package_data=True,  # Includes non-Python files like LICENSE.md
    # No CLI entry points in the alpha2 version yet... I'll add it in the future alpha releases.
    license="MIT",
)
