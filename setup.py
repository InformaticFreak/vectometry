from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "1.0.0"
DESCRIPTION = "Simple use of vectors and points with vector operations"
LONG_DESCRIPTION = "Defines a vector and point object with vector operations as functions and with integration of built-in operators for bette usability."

# Setting up
setup(
    name="vector-geometry",
    version=VERSION,
    author="InformaticFreak",
    author_email="<yt.informaticfreak@gmail.com@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["math"],
    keywords=["python", "vector", "point", "geometry", "analytic geometry", "vector oberations", "vectors"],
	url="https://github.com/InformaticFreak/vector-geometry"
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)