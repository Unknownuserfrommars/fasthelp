(README.md File version: 1.9.4.11)

# About FastHelp

A fast and useful helper in Python. It just makes things much faster.

> I love FastHelp! It's really useful, You see.   -- The Founder of JVSC, leading dev of FastHelp

## Installation

You can install fasthelp using pip:
`pip install fasthelp`

## Upgrades

You can also upgrade fasthelp to a newer version using pip:
`pip install --upgrade fasthelp`

## Requiring Python version

Python >= 3.9

## Dependencies

- NumPy >= 1.26
- Pandas >= 2.2

## A sneak peak at the source code:

Okay... maybe not...

```py
import pandas as pd
import numpy as np
import pprint
import subprocess
import os
import warnings
import openai
from docx import Document
from ppts import Presentation
import string
```

## Usage

`import fasthelp as fh`
PS: `fh` is the common alias for FastHelp

## Changelog (Since 1.0.12)

### For Changelogs from 1.0.12-1.0.20, see ancient releases. Have to make space for newer versions. (Sorry about that)

- 1.0.30: Added some functions in the `StringHelper` function, added a `OSHelper` function and fixed an ancient bug from 1.0.0. (Sorry 'bout that)
- 1.0.29: Insider Release, enhanced function defining and minor bug fixes.
- 1.0.28: Insider Release, Bug Fixes
- 1.0.27: Added a new class to the FileHelper main class.
- 1.0.26: Bug Fixes, enhanced Github repo page, and finer error messages.
- 1.0.25: Insider Release. Bug Fix and Security Updates.
- 1.0.24: Planned Public Release. Ended up as Insider Release. Minor Bug Fixes and a change to the almost-forgotten README.md file (oops)
- 1.0.23: Insider Release. Some tweaks to functions and their descriptions.
- 1.0.22: Insider Release. Minor Bug Fixes.
- 1.0.21: Planned Public Release. Ended up as Insider Release. Minor Bug Fixes.

## Version

FastHelp 1.0.30

## In-Development Versions:

- 1.1.0

## NEWS:

- This is the last 1.0.x line releases
- 1.1.0rc2 released.

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
