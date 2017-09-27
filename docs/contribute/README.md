# Contributing to Medusa Middleware

TODO: instructions here

Feel free to clone a copy of the repo and tailor to your needs.

## Current technology
- Developed in [python 3.4](https://www.python.org/). At present, later versions are problematic compiling with cx_Freeze).
- Runs on a [waitress web server](http://docs.pylonsproject.org/projects/waitress/en/latest/).
- Serves XML Web API Service to StruxureWare using [Falcon Framework](https://falconframework.org/).
- Retrieves 3rd party data for transformation using [requests](http://docs.python-requests.org/en/master/).
- Compiled to exe/msi installer using [cx_Freeze]().
- Installed as a Windows Service using [the Non-Sucking Service Manager](http://nssm.cc).

## Compiling
- Compile python application to exe using [cx_Freeze](https://anthony-tuininga.github.io/cx_Freeze/)

 ```
 > python setup.py build
 # writes build to build/exe.win32-3.4/
 ```

- Run the built exe from command line to check output is error free.
- Compile installer using [Inno Setup](http://www.jrsoftware.org/isinfo.php)
  * Install Inno Setup
  * Run Inno Setup and open setup_installer.iss
  * Run compiler
  * Writes installer to `dist/`  
- Run the installer, start the service and test the application.
