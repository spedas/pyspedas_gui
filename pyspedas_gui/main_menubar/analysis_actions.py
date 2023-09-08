from PySide6.QtGui import QAction
from .not_implemented_action import show_not_implemented_message


def add_analysis_actions(main_window, analysis_menu):
    # Add "Data processing..." action to the "Analysis" menu
    data_processing_action = QAction("Data processing...", main_window)
    data_processing_action.triggered.connect(show_not_implemented_message)
    analysis_menu.addAction(data_processing_action)

    # Add "Magnetic field models..." action to the "Analysis" menu
    field_models_action = QAction("Magnetic field models...", main_window)
    field_models_action.triggered.connect(show_not_implemented_message)
    analysis_menu.addAction(field_models_action)

    # Add "Neutral sheet models..." action to the "Analysis" menu
    neutral_action = QAction("Neutral sheet models...", main_window)
    neutral_action.triggered.connect(show_not_implemented_message)
    analysis_menu.addAction(neutral_action)

