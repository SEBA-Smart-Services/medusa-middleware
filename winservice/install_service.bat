nssm install medusa-middleware "C:\Program Files (x86)\Schneider Electric\Medusa Middleware\app.exe"
nssm set medusa-middleware Application "C:\Program Files (x86)\Schneider Electric\Medusa Middleware\app.exe"
nssm set medusa-middleware AppDirectory "C:\Program Files (x86)\Schneider Electric\Medusa Middleware"
nssm set medusa-middleware Description "A lightweight middleware service for StruxureWare Building Operation."
nssm set medusa-middleware Start SERVICE_AUTO_START
nssm set medusa-middleware AppExit Default Exit