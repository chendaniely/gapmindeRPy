import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gapmindeRPy",
    version="0.0.1",
    description="Finding project directories in Python (data science) projects, just like there R rprojroot and here packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Daniel Chen",
    author_email="chendaniely@gmail.com",
    url="https://github.com/chendaniely/gapmindeRPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
