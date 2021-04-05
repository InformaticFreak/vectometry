from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    README = "\n" + fh.read()

VERSION = "0.0.5"
DESCRIPTION = "A Python3 library for simple use of common vector and point operations in 3-dimensional space."
LONG_DESCRIPTION = "# Documentation\n" + DESCRIPTION + "\n\nDocumentation for __**vectometry**__ on [GitHub.com](https://github.com/InformaticFreak/vectometry#documentation)"

# Setting up
setup(
    name="vectometry",
    version=VERSION,
    author="InformaticFreak",
	license="MIT",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    keywords=["python", "vector", "point", "geometry", "analytic", "vector-math", "vectors-calculations", "vectorspace", "vectometry", "vectors"],
	url="https://github.com/InformaticFreak/vectometry",
	project_urls={
		"Documentation": "https://github.com/InformaticFreak/vectometry#documentation",
		"Source": "https://github.com/InformaticFreak/vectometry/blob/main/src/vectometry/__init__.py",
		"Bug Tracker": "https://github.com/InformaticFreak/vectometry/issues",
		"Change Log": ""
	},
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3",
    classifiers=[
		"Development Status :: 4 - Beta",
		"Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)