@echo off
title Toontown_BR - Game Client
cd..

set LOGIN_TOKEN=dev

p3d\python\ppython.exe -m toontown.launcher.StartToontownLauncher
pause
