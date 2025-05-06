from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QLCDNumber
class DigitalClock(QLCDNumber):

    def __init__(self, parent=None):

        super(DigitalClock, self).__init__(parent)
        self.setSegmentStyle(QLCDNumber.Filled)
        self.setDigitCount(8)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.showTime()
        self.setWindowTitle("Digital Clock")
        self.resize(200, 60)

    def showTime(self):

        time = QTime.currentTime()
        text = time.toString('h:mm a')
        self.display(text)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())