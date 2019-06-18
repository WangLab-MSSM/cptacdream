import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cptacdream",
    version="0.0.1",
    author="Anna Calinawan",
    author_email="anna.calinawan@mssm.edu",
    description="A package from the NCI-CPTAC DREAM Proteogenomics Challenge",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WangLab-MSSM/cptacdream",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Operating System :: OS Independent",
    ],
)