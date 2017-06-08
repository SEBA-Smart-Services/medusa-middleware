rem install Medusa Middleware as Windows service for x86_64 machines

set relpath = "Schneider Electric\Medusa Middleware"
set app = app.exe
set servicename = "medusa-middleware"

nssm install %servicename% "%programfiles(x86)%\$%relpath%\%app%"
nssm set %servicename% Application "%programfiles(x86)%\%relpath%\%app%"
nssm set %servicename% AppDirectory "%programfiles(x86)%\%relpath%"
nssm set %servicename% DisplayName "Medusa Middleware"
nssm set %servicename% Description "A lightweight middleware service for StruxureWare Building Operation."
nssm set %servicename% Start SERVICE_AUTO_START
nssm set %servicename% AppExit Default Exit