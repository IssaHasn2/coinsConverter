import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from converter import Ui_Converter

class ConverterLogic(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Converter()
        self.window = None

        self.coins = {
                "Dollar": 15000,
                "Euro": 16000,
                "SaudiRial": 4000,
                "KuwaitDinar": 50000,
                "UAEDirham": 28000,
                "JordanDinar": 22000,
                "SyrianPound" : 1
            }
        
    def ShowWindow(self):
        window = QMainWindow()
        self.window = window
        window.show()
        self.ui.setupUi(window)
        self.initialize()
        window.show()

    def initialize(self):
        self.ui.convertButton.clicked.connect(lambda: self.convert())

    # The conversion is based on the Syrian pound
    def convert(self):
        coinsInput = self.ui.coinsInput.text()
        currency = self.ui.coinsBox.currentText()
        toCurrency = self.ui.coinsBox_2.currentText()

        try:
            self.ui.couinsValueLabel.setText( f"{coinsInput} [{currency}] = {float(coinsInput) * float(self.coins[currency]) / float(self.coins[toCurrency])} [{toCurrency}]")
        except KeyError:
            self.ui.couinsValueLabel.setText("Invalid Currency !")
        except ValueError:
            self.ui.couinsValueLabel.setText("Invalid inputs !")
            
app = QApplication([sys.argv])
converter = ConverterLogic()
converter.ShowWindow()
app.exec()
