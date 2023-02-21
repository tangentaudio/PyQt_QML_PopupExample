# Quick PyQt5 / QML popup message demo for BKG
# 2023-FEB-21 steve.richardson@makeitlabs.com

import sys
import signal
from datetime import datetime
import time
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtCore import QObject, QThread

class Worker(QThread):
    textReady = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)

    def run(self):
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            self.textReady.emit('It is now %s' % (current_time))
            time.sleep(5); 

class App(QObject):
    def __init__(self):
        super().__init__()
        
        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()

        self.worker = Worker()

        self.ctx = self.engine.rootContext()
        self.ctx.setContextProperty("worker", self.worker)
        self.engine.load('main.qml')
        self.worker.start()


    def exec(self):
        sys.exit(self.app.exec_())        

if __name__ == "__main__":
    # hack to accept ctrl-c from terminal; not the best way to do it with Qt but fine for now
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    
    app = App()
    app.exec()


