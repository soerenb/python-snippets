PYUIC = pyuic4

.PHONY: clean

hello_gui.py: hello.ui
	$(PYUIC) $< -o $@

clean:
	rm -rf hello_gui.py __pycache__
	
