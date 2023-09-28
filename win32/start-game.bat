@echo off
title Toontown BR Offline - Game Client
cd..

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

set LOGIN_TOKEN=dev

%PPYTHON_PATH% -m toontown.launcher.QuickStartLauncher
pause
