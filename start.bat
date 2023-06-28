@echo off
:top

python GAP_cal.py


:retry
SET /P a=Continue?(y/n):

if "%a%" == "y" (
    echo restarting...
    goto top
) else if "%a%" == "n" (
    pause
    exit
) else (
    echo unknown input
    goto retry
)