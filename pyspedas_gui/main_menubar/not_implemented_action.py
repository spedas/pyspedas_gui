from PySide6.QtWidgets import QMessageBox

def show_not_implemented_message():
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setText("Feature not yet implemented")
    msg_box.setWindowTitle("Info")
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec()

