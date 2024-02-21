
from setuptools import find_packages, setup

VERSION = "0.1.0"
setup(name="pysportradar",
      description="Wrapper for SportRadar APIs",
      version=VERSION,
      license="GNU",
      author="Chandler Hagan",
      packages=find_packages(exclude=["test"]),
      install_requires=["requests"],
      python_requires=">=3.12.1"
)