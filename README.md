# PyQt_QML_PopupExample
Steve Richardson (steve.richardson@makeitlabs.com)

Quick example of how to do a PyQt/QML desktop always-on-top popup message.  Not guaranteed to be pretty or proper.

The thread in `main.py` could be replaced with anything (e.g. receiving messages via MQTT), and the graphical styling and positioning of the message can be adjusted in the QML.

The main thing of note is the `Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint` flags applied to the window.  This makes it appear as a popup on top of all other desktop windows.

