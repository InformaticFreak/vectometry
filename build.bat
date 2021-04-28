@echo off
title build vectometry
cls
py setup.py sdist bdist_wheel
echo.
twine check dist/*