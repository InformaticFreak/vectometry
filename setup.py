from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md")) as file:
	README = "".join([ line for line in file.readlines() if not line.startswith("[!") ])
	print(README)

VERSION = "0.0.7"
DESCRIPTION = "A Python library for simple use of common vector and point operations in 3-dimensional space as well as for 2-dimensions."
LONG_DESCRIPTION = "# Documentation\n" + DESCRIPTION + "\n\nDocumentation for __**vectometry**__ on [GitHub.com](https://github.com/InformaticFreak/vectometry#documentation)"

setup(
    name="vectometry",
    version=VERSION,
    author="InformaticFreak",
	license="MIT",
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    keywords=["python", "vector", "point", "geometry", "analytic", "vector-math", "vectors-calculations", "vectorspace", "vectometry", "vectors", "2d", "3d"],
	url="https://github.com/InformaticFreak/vectometry",
	project_urls={
		"Documentation": "https://github.com/InformaticFreak/vectometry#documentation",
		"Source": "https://github.com/InformaticFreak/vectometry/blob/main/src/vectometry/__init__.py",
		"Bug Tracker": "https://github.com/InformaticFreak/vectometry/issues",
		"Change Log": "https://github.com/InformaticFreak/vectometry/blob/main/CHANGELOG.md"
	},
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    classifiers=[
		"Development Status :: 4 - Beta",
		"Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: OS Independent"
    ]
)