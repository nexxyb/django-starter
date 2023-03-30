#!/usr/bin/env python3

import os

TERMINATOR = "\x1b[0m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

project_slug = os.path.basename(os.getcwd())
print(SUCCESS + f"Project {project_slug} initialized, keep up the good work!" + TERMINATOR)

