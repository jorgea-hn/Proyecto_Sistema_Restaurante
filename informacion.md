# Pasos para el proyecto

1. Crear entorno virtual  ---- python -m venv entorno
2. Acceder al entorno     ---- entorno\Scripts\activate
3. Instalar PyQt5         ---- pip install PyQt5
4. Instalar el designer   ---- pip install pyqt5-tools
5. ruta designer.exe      ---- entorno\Lib\site-packages\qt5_applications\Qt\bin
6. Crear una nueva rama   ---- git checkout -b rama
7. Compilar tu interfaz en python ---- pyuic5 "Nombre.ui" > "Nombre.py"