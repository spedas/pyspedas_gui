from PySide6.QtGui import QAction
from .not_implemented_action import show_not_implemented_message


def add_plot_actions(main_window, plot_menu):
    # Add "Plot layout/options..." action to the "Plot" menu
    layout_action = QAction("Plot layout/options...", main_window)
    layout_action.triggered.connect(show_not_implemented_message)
    plot_menu.addAction(layout_action)

    # Add "Page options..." action to the "Plot" menu
    page_action = QAction("Page options...", main_window)
    page_action.triggered.connect(show_not_implemented_message)
    plot_menu.addAction(page_action)

    # Add "Panel options..." action to the "Plot" menu
    panel_action = QAction("Panel options...", main_window)
    panel_action.triggered.connect(show_not_implemented_message)
    plot_menu.addAction(panel_action)

    # Add "Line options..." action to the "Plot" menu
    line_action = QAction("Line options...", main_window)
    line_action.triggered.connect(show_not_implemented_message)
    plot_menu.addAction(line_action)

    # Add "Legend options..." action to the "Plot" menu
    legend_action = QAction("Line options...", main_window)
    legend_action.triggered.connect(show_not_implemented_message)
    plot_menu.addAction(legend_action)

    # Add "X Axis options..." action to the "Plot" menu
    x_axis_action = QAction("X Axis options...", main_window)
    x_axis_action.triggered.connect(show_not_implemented_message)
    plot_menu.addAction(x_axis_action)

    # Add "Y Axis options..." action to the "Plot" menu
    y_axis_action = QAction("Y Axis options...", main_window)
    y_axis_action.triggered.connect(show_not_implemented_message)
    plot_menu.addAction(x_axis_action)

    # Add "Z Axis options..." action to the "Plot" menu
    z_axis_action = QAction("Z Axis options...", main_window)
    x_axis_action.triggered.connect(show_not_implemented_message)
    plot_menu.addAction(x_axis_action)

    # Add "Variable options..." action to the "Plot" menu
    variable_action = QAction("Variable options...", main_window)
    variable_action.triggered.connect(show_not_implemented_message)
    plot_menu.addAction(variable_action)




