PYUIC = pyuic4

.PHONY: clean

rot13_gui.py: rot13_gui.ui
	$(PYUIC) $< -o $@

clean:
	rm -rf rot13_gui.py __pycache__
