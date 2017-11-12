"""Setup file."""

# external imports
from setuptools import setup

# long description
with open("README.md", 'r') as f:
    long_description = f.read()

# requirements
with open('requirements.txt', 'r') as f:
    requirements = list(filter(None, f.read().split('\n')))

setup(
    name='py-scu-ugr',
    version='0.1',
    description='Simple python scu scrapper.',
    long_description=long_description,
    license="GPLv3",
    author='Luis Liñán',
    author_email='luislivilla@gmail.com',
    url="https://github.com/lulivi/py-scu-ugr",
    install_requires=requirements, )
