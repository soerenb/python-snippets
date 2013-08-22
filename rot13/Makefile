PYUIC = pyuic4

.PHONY: clean
all: rot13_gui.py popup.py

rot13_gui.py: rot13_gui.ui
	$(PYUIC) $< -o $@

popup.py: popup.ui
	$(PYUIC) $< -o $@

clean:
	rm -rf rot13_gui.py popup.py __pycache__
