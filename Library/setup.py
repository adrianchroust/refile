from setuptools import setup

__project__= "Refile"
__version__ = "1.1.1"
__description__ = "a Python module for automated photo-sorting"
__packages__=["photo_sorting","PIL"]
__author__="Adrian"

setup(
    name = __project__,
    version = __version__,
    description = __description__,
    packages = __packages__,
    author=__author__
)
