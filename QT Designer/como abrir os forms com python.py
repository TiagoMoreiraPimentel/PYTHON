# Comando para converter um arquivo formato .ui para .py:   pyuic5 arquivo.ui -o arquivo.py




#Codigo que vai no final do arquivo ''py'' gerado. responsavel por ler o grafico e chamar:


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())