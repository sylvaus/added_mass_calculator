from setuptools import setup, find_packages

import added_mass_calculator

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name='added_mass_calculator',
    version=added_mass_calculator.__version__,
    packages=find_packages(),
    url='https://github.com/sylvaus/added_mass_calculator',
    license='',
    author='sylvaus',
    author_email='',
    description='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], install_requires=['numpy', 'numpy-stl']
)
