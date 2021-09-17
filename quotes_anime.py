from PyQt5 import QtCore, QtGui, QtWidgets

import requests


class Ui_Quotes(object):
    def setupUi(self, Quotes):
        Quotes.setObjectName("Quotes")
        Quotes.resize(447, 700)
        self.verticalLayoutWidget = QtWidgets.QWidget(Quotes)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 0, 371, 600))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(Quotes)
        self.pushButton.setGeometry(QtCore.QRect(150, 650, 158, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked)
        

        self.retranslateUi(Quotes)
        QtCore.QMetaObject.connectSlotsByName(Quotes)

    def retranslateUi(self, Quotes):
        _translate = QtCore.QCoreApplication.translate
        Quotes.setWindowTitle(_translate("Quotes", "Quotes"))
        self.label_3.setText(_translate("Quotes", 'Anime'))
        self.label_2.setText(_translate("Quotes", 'Character'))
        self.label.setText(_translate("Quotes", 'Quotes'))
        self.pushButton.setText(_translate("Quotes", "New"))
    
    def clicked(self):
        response = requests.get("https://animechan.vercel.app/api/quotes")

        response = response.json()
        response = response[1]
        anime = response['anime']
        char = response['character']
        quote = response['quote']
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("Quotes", anime))
        self.label_2.setText(_translate("Quotes", char))
        self.label.setText(_translate("Quotes", quote))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Quotes = QtWidgets.QDialog()
    ui = Ui_Quotes()
    ui.setupUi(Quotes)
    Quotes.show()
    sys.exit(app.exec_())
