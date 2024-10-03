import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QPushButton
from PyQt6.QtCore import QSize

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.janela = QWidget()
        self.layout = QVBoxLayout(self.janela)

        self.Janela_build()  # Chama o método para definir título e estilo
        self.Layout_build()   # Chama o método para construir o layout
        self.botoes_build()
        self.setCentralWidget(self.janela)
        self.setGeometry(100, 100, 300, 400)  # Define a geometria da janela principal
        self.setMaximumSize(QSize(300, 400))

        self.calculo = ""  # Inicializa uma string para armazenar a expressão

    def Layout_build(self):
        # Cria um rótulo para o visor
        self.visor_numeros = QLabel("Calculadora")
        self.visor_numeros.setStyleSheet("QLabel { color: gray; font-size: 24px; }")
        self.layout.addWidget(self.visor_numeros)

        # Layouts para botões
        self.layout_botaos = QVBoxLayout()
        self.layout_botaos_numeros = QGridLayout()
        self.layout_botaos_operadores = QHBoxLayout()

        # Adiciona os layouts de botões ao layout principal
        self.layout_botaos.addLayout(self.layout_botaos_numeros)
        self.layout_botaos.addLayout(self.layout_botaos_operadores)
        self.layout.addLayout(self.layout_botaos)

    def botoes_build(self):
        botoes = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
            ('0', 3, 1), ('C', 3, 0), ('=', 3, 2)
        ]

        for texto, linha, coluna in botoes:
            botao = QPushButton(texto)
            botao.setMinimumSize(40, 20)
            botao.setStyleSheet("""
            QPushButton {font-size: 14px; background-color: blue;}
            QPushButton:hover {background-color: green;}
            """)
            botao.clicked.connect(lambda _, txt=botao.text(): self.editor(txt))  # Passa o texto corretamente
            self.layout_botaos_numeros.addWidget(botao, linha, coluna)

        operadores = ["+", "-", "x", "/"]
        for texto in operadores:
            botao = QPushButton(texto)
            botao.setMinimumSize(40, 20)
            botao.setStyleSheet("""
            QPushButton {font-size: 14px; background-color: blue;}
            QPushButton:hover {background-color: green;}
            """)
            botao.clicked.connect(lambda _, txt=botao.text(): self.editor(txt))
            self.layout_botaos_operadores.addWidget(botao)

    def Janela_build(self):
        self.setWindowTitle("Janela Principal")  # Define o título da janela principal
        self.janela.setStyleSheet("QWidget { background-color: white; }")  # Define o estilo

    def editor(self, texto):
        # Se o visor estiver com o texto padrão, inicia com o novo texto
        if texto == "C":
            self.calculo = ""  # Limpa a expressão
            self.visor_numeros.setText("Calculadora")
        elif texto == "=":
            try:
                # Avalia a expressão e exibe o resultado
                resultado = eval(self.calculo.replace("x", "*"))  # Troca 'x' por '*' para avaliação
                self.visor_numeros.setText(str(resultado))
                self.calculo = str(resultado)  # Atualiza a expressão com o resultado
            except Exception as e:
                self.visor_numeros.setText("Erro")
                self.calculo = ""
        else:
            # Adiciona o novo texto ao visor e à expressão
            if self.visor_numeros.text() == "Calculadora":
                self.calculo = texto  # Inicia a expressão com o texto
                self.visor_numeros.setText(texto)
            else:
                self.calculo += texto  # Adiciona à expressão
                self.visor_numeros.setText(self.calculo)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = JanelaPrincipal()
    window.show()

    sys.exit(app.exec())
