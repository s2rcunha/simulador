@echo off
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0servidor_local.ps1"
if errorlevel 1 (
  echo.
  echo Nao foi possivel iniciar o servidor local.
  pause
)
