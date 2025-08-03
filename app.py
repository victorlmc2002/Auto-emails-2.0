from config import QTD
from arquivos import ler_planilha
from interface.gui import EmailInterface

def main():
    devedores = ler_planilha(QTD)
    app = EmailInterface(devedores)
    app.run()

if __name__ == "__main__":
    main()