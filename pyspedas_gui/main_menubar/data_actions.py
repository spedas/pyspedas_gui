from PySide6.QtGui import QAction
from .not_implemented_action import show_not_implemented_message
from pyspedas_gui.panels import cdagui

def add_data_actions(main_window, data_menu):
    # Add "Load data from plugin..." action to the "Data" menu
    load_plugin_action = QAction("Load data from plugin...", main_window)
    load_plugin_action.triggered.connect(show_not_implemented_message)
    data_menu.addAction(load_plugin_action)

    # Add "Load data from CDAWeb..." action to the "Data" menu
    load_cdaweb_action = QAction("Load data from CDAWeb...", main_window)
    load_cdaweb_action.triggered.connect(cdagui)
    data_menu.addAction(load_cdaweb_action)

    # Add "Load data via HAPI..." action to the "Data" menu
    load_hapi_action = QAction("Load data via HAPI...", main_window)
    load_hapi_action.triggered.connect(show_not_implemented_message)
    data_menu.addAction(load_hapi_action)

    # Add "Manage tplot variables..." action to the "Data" menu
    tplot_action = QAction("Manage tplot variables...", main_window)
    tplot_action.triggered.connect(show_not_implemented_message)
    data_menu.addAction(tplot_action)
