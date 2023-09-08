import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from main_menubar import add_file_actions, add_data_actions


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the main layout
        layout = QVBoxLayout()

        # Create a Matplotlib canvas for plotting
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Create a central widget for the main window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Create the menu bar
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Add menus to the menu bar
        self.file_menu = QMenu("File", self)
        self.data_menu = QMenu("Data", self)
        self.plot_menu = QMenu("Plot", self)
        self.help_menu = QMenu("Help", self)
        self.about_menu = QMenu("About", self)

        self.menu_bar.addMenu(self.file_menu)
        self.menu_bar.addMenu(self.data_menu)
        self.menu_bar.addMenu(self.plot_menu)
        self.menu_bar.addMenu(self.help_menu)
        self.menu_bar.addMenu(self.about_menu)

        # Add actions to each pull-down menu on the main menu bar
        add_file_actions(self, self.file_menu)
        add_data_actions(self, self.data_menu)

        # Set the main window properties
        self.setWindowTitle("pyspedas GUI")
        self.setGeometry(100, 100, 800, 600)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
