SET PATH_TO_HERE=%~dp0
python -m venv ./venv
SET PATH_TO_ACTIVATE=%PATH_TO_HERE%\venv\Scripts\activate.bat
CALL "%PATH_TO_ACTIVATE%" 
SET PATH_TO_VENV_PYTHON=%PATH_TO_HERE%\venv\Scripts\python.exe
"%PATH_TO_VENV_PYTHON%" -m pip install -r requirements.txt
