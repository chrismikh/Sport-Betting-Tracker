from PyQt5.QtWidgets import QApplication, QLabel, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('My First App')
window.setGeometry(100, 100, 280, 80)

label = QLabel('<h1>Hello World!</h1>', parent=window)
label.move(60, 15)

window.show()
sys.exit(app.exec_())
