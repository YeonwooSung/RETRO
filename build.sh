#!/bin/bash

# remove pre-built files
rm -rf pyretro.egg-info
rm -rf dist
rm -rf build

# build by using wheel
python3 setup.py bdist_wheel

# deploy by using twine
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose