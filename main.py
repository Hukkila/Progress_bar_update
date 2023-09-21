import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar

#Important includes
from PyQt5.QtCore import QTimer
import time

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        loadUi("MainWindow.ui", self)
        self.progressBar = self.findChild(QProgressBar, 'progressBar')  
        self.data = [['first', 10], ['second', 20, 5.0], ['third', 10],
                     ['fourth', 30, 20.0], ['fifth', 20], ['sixth', 10]]


        # Everything below is important
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateProgressBar)
        self.timer.start(1000)  # Update every second
        
        self.total_percent = 0
        self.current_percent = 0


    def updateProgressBar(self):
        for item in self.data:
            percent_item = item[1]
            if len(item) >= 3:
                time_item = item[2]
                time_sleep = time_item / percent_item
            else: 
                time_sleep = 0.01

            self.total_percent = self.total_percent + percent_item
            self.current_percent = self.total_percent - percent_item

            while self.current_percent < self.total_percent:
                self.current_percent += 1
                self.progressBar.setValue(self.current_percent)
                time.sleep(time_sleep)
    
        # Until here
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

