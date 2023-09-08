from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMessageBox
from .not_implemented_action import show_not_implemented_message

def show_about_message():
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setText("pyspedas_gui version 0.0.0")
    msg_box.setWindowTitle("About pyspedas_gui")
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec()

def add_help_actions(main_window, help_menu):
    # Add "Help" action to the "Data" menu
    help_action = QAction("Help", main_window)
    help_action.triggered.connect(show_not_implemented_message)
    help_menu.addAction(help_action)

    # Add "About" action to the "Data" menu
    about_action = QAction("About pyspedas_gui", main_window)
    about_action.triggered.connect(show_about_message)
    help_menu.addAction(about_action)
