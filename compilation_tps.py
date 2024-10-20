import sys

from PyQt5.QtWidgets import (QAction, QApplication, QHBoxLayout, QMainWindow,
                             QMenuBar, QPushButton, QTextEdit, QVBoxLayout,
                             QWidget)


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Editor")
        self.setGeometry(100, 100, 800, 600)

        # Create central widget and main layout
        central_widget = QWidget()
        main_layout = QHBoxLayout()

        # Create left panel with buttons
        left_panel = QWidget()
        left_layout = QVBoxLayout()
        
        open_button = QPushButton("Open")
        save_button = QPushButton("Save")
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)

        left_layout.addWidget(open_button)
        left_layout.addWidget(save_button)
        left_layout.addStretch()
        left_layout.addWidget(exit_button)
        
        left_panel.setLayout(left_layout)

        # Create right panel with text areas
        right_panel = QWidget()
        right_layout = QHBoxLayout()
        
        text_area1 = QTextEdit()
        text_area2 = QTextEdit()

        right_layout.addWidget(text_area1)
        right_layout.addWidget(text_area2)
        
        right_panel.setLayout(right_layout)

        # Add panels to main layout
        main_layout.addWidget(left_panel, 1)
        main_layout.addWidget(right_panel, 4)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Create menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        analysis_menu = menu_bar.addMenu("Analysis")

        # Add actions to File menu
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())