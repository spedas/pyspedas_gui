from PySide6.QtGui import QAction
def add_file_actions(mainWindow,fileMenu):
    # Add "Exit" action to the "File" menu
    exit_action = QAction("Exit", mainWindow)
    exit_action.triggered.connect(mainWindow.close)
    fileMenu.addAction(exit_action)
