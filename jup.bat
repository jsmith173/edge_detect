@setlocal
@set PYTHONVER=Python310_a
@set PYTHONHOME=%USERPROFILE%\AppData\Local\Programs\Python\%PYTHONVER%
@set PATH=%PYTHONHOME%\Scripts;%PATH%
jupyter notebook %1
