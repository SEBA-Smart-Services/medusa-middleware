@echo off

rem install Medusa Middleware as Windows service for x86 machines

set relpath=Schneider Electric\Medusa Middleware
set app=app.exe
set servicename=medusa-middleware
set displayname=Medusa Middleware
set description=A lightweight middleware service for StruxureWare Building Operation.

echo "%programfiles%\%relpath%\%app%"

echo nssm install %servicename% "%programfiles%\%relpath%\%app%"
nssm install %servicename% "%programfiles%\%relpath%\%app%"

echo nssm set %servicename% Application "%programfiles%\%relpath%\%app%"
nssm set %servicename% Application "%programfiles%\%relpath%\%app%"

echo nssm set %servicename% AppDirectory "%programfiles%\%relpath%"
nssm set %servicename% AppDirectory "%programfiles%\%relpath%"

echo nssm set %servicename% DisplayName "%displayname%"
nssm set %servicename% DisplayName "%displayname%"

echo nssm set %servicename% Description "%description%"
nssm set %servicename% Description "%description%"

nssm set %servicename% Start SERVICE_AUTO_START
nssm set %servicename% AppExit Default Exit