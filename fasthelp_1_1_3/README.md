(README.md File version: 1.10.4.11)

# About FastHelp

A fast and useful helper in Python. It just makes things much faster.

> I love FastHelp! It's really useful, You see.   -- The Leading dev of FastHelp

## Installation

You can install fasthelp using pip:
`pip install fasthelp`

Or, if you've installed it previously, upgrade to this version by running the code:
`pip install --upgrade fasthelp`

## Requiring Python version

Python >= 3.10

## Dependencies

- NumPy >= 1.26
- Pandas >= 2.2
- openai >= 1.51
- python-docx >= 1.1.0
- python-pptx >= 1.0.0
- distro >= 1.9.0
- psutil >= 6.0.0

## A sneak peak at the source code:

Okay... maybe not...

```py
import pandas as pd # type: ignore
import numpy as np
import pprint
import subprocess
import os
import warnings
import openai # type: ignore
from docx import Document
from pptx import Presentation
import string
import platform
import distro
import typing
```

## Usage

`import fasthelp as fh`
PS: `fh` is the common alias for FastHelp

## Changelog (Since 1.0.12)

### (For Changelogs from 1.0.12-1.0.25, see ancient releases. Have to make space for newer versions)

- 1.1.3: Bug fix and class enhancements
- 1.1.0.1: Major bug fix on the `ModuleNotFoundError` while importing
- 1.1.0: Major release. Added some functions, fixed `exec()` logic, added `@staticmethod` decorator to some of the functions. Added an additional file for detecting GPU info. Renamed some function/class names.
- 1.0.30: Added some functions in the `StringHelper` function, added a `OSHelper` function and fixed an ancient bug from 1.0.0. (Sorry 'bout that)
- 1.0.29: Insider Release, enhanced function defining and minor bug fixes.
- 1.0.28: Insider Release, Bug Fixes
- 1.0.27: Added a new class to the FileHelper main class.
- 1.0.26: Bug Fixes, enhanced Github repo page, and finer error messages.

## Version

FastHelp 1.1.3

## In-Development Versions:

- 1.1.4

## NEWS:
-  No News yet

## Roadmap

- In 1.2.x versions: Command Line Interface (CLI)
- In 1.3.x versions: Use subpackages and probably implement some of the tasks in the `Future` class

## License

This project is licensed under the MIT License:

MIT License

Copyright (c) 2024 ZIYAN ZHOU

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
