from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.1"
DESCRIPTION = "Simple use of common vector and point operations in 3-dimensional space."
LONG_DESCRIPTION = "Defines Vector and Point object with common vector operations as functions and with integration of built-in operators for better usability."

# Setting up
setup(
    name="vectometry",
    version=VERSION,
    author="InformaticFreak",
    author_email="<yt.informaticfreak@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    install_requires=[],
    keywords=["python", "vector", "point", "geometry", "analytic geometry", "vector operations", "vector geometry", "vectometry", "vectors"],
	url="https://github.com/InformaticFreak/vectometry",
	project_urls={
		"Bug Tracker": "https://github.com/InformaticFreak/vectometry/issues",
	},
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)