from PySide6.QtGui import QAction
def add_file_actions(main_window, file_menu):
    # Add "Exit" action to the "File" menu
    exit_action = QAction("Exit", main_window)
    exit_action.triggered.connect(main_window.close)
    file_menu.addAction(exit_action)
