import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.janela = QWidget()
        self.layout = QVBoxLayout(self.janela)

        self.Janela_build()  # Chame o método para definir título e estilo
        self.setCentralWidget(self.janela)
        self.setGeometry(100, 100, 200, 300)  # Define a geometria da janela principal

    def Layout_build(self):
        # Aqui você pode adicionar widgets ao layout, se necessário
        pass

    def Janela_build(self):
        self.setWindowTitle("Janela Principal")  # Defina o título da janela principal
        self.janela.setStyleSheet("QWidget { background-color: white; }")  # Define o estilo

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = JanelaPrincipal()
    window.show()
    
    sys.exit(app.exec())
