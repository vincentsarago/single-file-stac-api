"""aiocogeo packaging"""
from setuptools import find_packages, setup

with open("README.md") as f:
    desc = f.read()

with open("./requirements.txt") as reqs:
    requirements = [line.rstrip() for line in reqs]

setup(
    name="single-file-stac-api",
    description="API for Single File STACs",
    long_description=desc,
    long_description_content_type="text/markdown",
    version="0.1.0",
    author=u"Jeff Albrecht",
    author_email="geospatialjeff@gmail.com",
    url="https://github.com/geospatial-jeff/single-file-stac-api",
    license="mit",
    python_requires=">=3.7",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="STAC",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=requirements,
)
