"""
setup.py

Setup script for msi compiler using cx_Freeze

Usage:
 $ python setup.py bdist_msi

"""
import sys
from cx_Freeze import setup, Executable

company_name = 'Schneider Electric'
product_name = 'Medusa Middleware'

include_files = [
    'config.ini',
    'struxureware',
    'README.md',
    'winservice',
    "interfaces",
    "middleware"
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

# include = [
    
# ]

build_exe_options = {
    "packages": packages,
    "excludes": ["tkinter"],
    'include_files': include_files
}

bdist_msi_options = {
    'add_to_path': True,
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None

setup(
    name = "Medusa Middleware",
    version = "0.1",
    description = "A lightweight middleware service for StruxureWare Building Operation.",
    options = {
        'build_exe': build_exe_options,
        'bdist_msi': bdist_msi_options
    },
    executables = [Executable("app.py", base=base)]
)