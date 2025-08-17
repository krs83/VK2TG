build:
	pyinstaller --onefile --add-data "settings.ini:." run.py
	cp settings.ini dist/

clean:
	rm -rf build/ dist/ __pycache__/ *.spec