import sys

from PyQt5.QtWidgets import *

import fonts
import pyfiglet.fonts


class FigletForm(QMainWindow):
    """
    Form of the User Interface
    """
    def __init__(self):
        super(FigletForm, self).__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        entry_label = QLabel("Introduce el banner que quieres escribir: ")
        self.entry_edit = QLineEdit()
        self.entry_edit.setText("hola")

        font_label = QLabel("Selecciona el tipo de letra: ")
        self.font_combo = QComboBox()
        self.font_combo.addItems(font for font in fonts.fonts)

        self.view = QTextEdit()
        self.view.setFontFamily("Consolas")

        lay = QVBoxLayout()
        lay.addWidget(entry_label)
        lay.addWidget(self.entry_edit)
        lay.addWidget(font_label)
        lay.addWidget(self.font_combo)
        lay.addWidget(self.view)

        self.setGeometry(300, 300, 600, 500)
        widget.setLayout(lay)

        # connections
        self.entry_edit.textEdited.connect(self.update_view)
        self.font_combo.currentIndexChanged.connect(self.update_view)
        self.update_view()

    def update_view(self):
        """
        Update TextEdit view when the LineEdit field or the Font selection has 
        changed.
        """
        text = str(self.entry_edit.text())
        if self.font_combo.currentIndex() == 0:
            self.view.setText(pyfiglet.figlet_format(text))
        else:
            _font = self.font_combo.currentText()
            self.view.setText(pyfiglet.figlet_format(text, font=_font))


if __name__ == '__main__':
    app = QApplication([sys.argv])
    app.setApplicationName("PyFigletUI")
    form = FigletForm()
    try:
        import qdarkstyle
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    except:
        app.setStyle(QProxyStyle("Fusion"))
    form.show()
    sys.exit(app.exec_())
