from pathlib import Path
from setuptools import find_packages, setup
from credits import PYTHINGS

'''Get parent directory of pythings'''
HERE = Path(__file__).parent

'''All setup constants goes here'''
PACKAGE_NAME = PYTHINGS["package_name"]
DESCRIPTION = PYTHINGS["description"]
VERSION = PYTHINGS["version"]
AUTHOR = PYTHINGS["author"]["name"]
EMAIL = PYTHINGS["author"]["email"]
GIT = PYTHINGS["author"]["git"]
LICENSE = PYTHINGS["license"]
REQUIRES = PYTHINGS["requires"]
DOCUMENTATION = (HERE / "README.md").read_text(encoding="utf-8")
DESCTYPE = PYTHINGS["desc-type"]

'''Setup with constants created below'''
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=DOCUMENTATION,
    long_description_content_type=DESCTYPE,
    author=AUTHOR,
    author_email=EMAIL,
    url=GIT,
    requires=REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)