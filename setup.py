import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pandas-linear-regression-ThomasJewson", # Replace with your own username
    version="0.0.1",
    author="Thomas Jewson",
    author_email="tjewson1@gmail.com",
    description="A small package that includes a few functions for linear regression specifically for pandas DataFrames",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThomasJewson/pandas-linear-regression",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
