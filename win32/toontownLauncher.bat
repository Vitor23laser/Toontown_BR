@echo off
title Toontown_BR - Game Client
cd..

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

set LOGIN_TOKEN=playToken

%PPYTHON_PATH% -m toontown.launcher.QuickStartLauncher
pause
