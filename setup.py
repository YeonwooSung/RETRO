# RETRO :: Retrieval Enhanced Transformer
# Copyright 2022  Yeonwoo Sung. All rights reserved.

# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY
# without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.



"""
Simple check for pyretro repo: https://github.com/YeonwooSung/RETRO
"""

from setuptools import setup, find_packages

setup(
  name = 'pyretro',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='GNU',
  description = 'RETRO :: Retrieval Enhanced Transformer',
  author = 'Yeonwoo Sung',
  author_email = 'neos960518@gmail.com',
  url = 'https://github.com/YeonwooSung/RETRO',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'transformers',
    'attention-mechanism',
    'retrieval',
    'information retrieval',
    'IR'
  ],
  install_requires=[
    'autofaiss',
    'einops>=0.3',
    "fairscale>0.3",
    'huggingface-hub',
    'numpy',
    "nltk",
    "jax>=0.2.8",
    "onnxconverter-common",
    "onnxruntime-tools>=1.4.2",
    "onnxruntime>=1.4.0",
    "pytest",
    "pytest-timeout",
    "pytest-xdist",
    "scikit-learn",
    "sentencepiece>=0.1.91,!=0.1.92",
    "tensorflow-cpu>=2.3",
    "tensorflow>=2.3",
    "tf2onnx",
    "torch>=1.6",
    'tqdm'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: GNU License',
    'Programming Language :: Python :: 3.6',
  ],
)
