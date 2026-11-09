@echo off
rem Lancador local: corre a CLI sem instalar o pacote.
setlocal
set "PYTHONPATH=%~dp0src;%PYTHONPATH%"
py -3 -X utf8 -m wot_extractor %*
exit /b %ERRORLEVEL%
