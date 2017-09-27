"""
setup.py

Setup script for msi compiler using cx_Freeze

Usage:
 $ python setup.py bdist_msi

"""
import sys
from cx_Freeze import setup, Executable

COMPANY_NAME = 'Schneider Electric'
PRODUCT_NAME = 'Medusa Middleware'
PRODUCT_DESCRIPTION = "A lightweight middleware service for StruxureWare Building Operation."
VERSION = "0.1.0"

include_files = [
    'config.ini',
    'struxureware',
    'README.md',
    'winservice',
    "interfaces",
    "middleware",
    "docs",
    "medusa.ico"
]

# Dependencies are automatically detected, but it might need fine tuning.
packages = [
    "falcon",
    "dicttoxml",
    "waitress",
    "configparser",
    "os",
    "http",
    "requests",
    "idna"
]

build_exe_options = {
    "packages": packages,
    "excludes": ["tkinter"],
    'include_files': include_files
}

bdist_msi_options = {
    'add_to_path': True,
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (COMPANY_NAME, PRODUCT_NAME),
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None

setup(
    name = PRODUCT_NAME,
    version = VERSION,
    description = PRODUCT_DESCRIPTION,
    options = {
        'build_exe': build_exe_options,
        'bdist_msi': bdist_msi_options
    },
    executables = [Executable("app.py", base=base)]
)
