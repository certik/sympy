#! /usr/bin/env python

import os
from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext

from Cython.Compiler.Main import compile

compiled_modules = [
        "sympy.ntheory.divisors",
        ]

source_root = os.path.dirname(__file__)
extensions = []
for module in compiled_modules:
    source_file = os.path.join(source_root, *module.split('.')) + ".py"
    print("Compiling module %s ..." % module)
    result = compile(source_file)
    if result.c_file is None:
        raise Exception("Compilation failed")
    extensions.append(
            Extension(module, sources = [result.c_file])
            )

ext_modules = extensions
cmdclass = {"build_ext": build_ext}
