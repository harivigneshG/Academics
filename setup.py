from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in academics/__init__.py
from academics import __version__ as version

setup(
	name="academics",
	version=version,
	description="academics",
	author="hari",
	author_email="hari@a.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
