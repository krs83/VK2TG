build:
	pyinstaller run.py
	cp settings.ini dist/

clean:
	rm -rf build/ dist/ __pycache__/ *.spec