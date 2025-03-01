@echo off
title Toontown_BR - AI (District) Server
cd..

:main
p3d/python/ppython.exe -m toontown.ai.AIStart --base-channel 401000000 ^
               --max-channels 999999 --stateserver 4002 ^
               --messagedirector-ip 127.0.0.1:7199 ^
               --eventlogger-ip 127.0.0.1:7197 ^
               --district-name "Vila dos Idiotas"
goto main
