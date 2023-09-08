from PySide6.QtGui import QAction
from .not_implemented_action import show_not_implemented_message


def add_file_actions(main_window, file_menu):
    # Add "Configuration settings..." action to the "File" menu
    config_action = QAction("Configuration settings...", main_window)
    config_action.triggered.connect(show_not_implemented_message)
    file_menu.addAction(config_action)

    # Add "Exit" action to the "File" menu
    exit_action = QAction("Exit", main_window)
    exit_action.triggered.connect(main_window.close)
    file_menu.addAction(exit_action)
