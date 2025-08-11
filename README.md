# Auto_emails_Vigor

_Automatize o envio de boletos por e-mail para inquilinos e proprietários da empresa Vigor - Gestão de Negócios Imobiliários._

## Objetivo

Este projeto facilita o envio automático de boletos e relatórios financeiros para inquilinos e proprietários, utilizando uma interface gráfica simples e a planilha já utilizada pela empresa.

## Pré-requisitos

- Python 3 instalado na máquina
- Biblioteca `openpyxl` instalada  
  Instale com:
  ```sh
  pip install openpyxl
  ```

## Como usar

1. Certifique-se de que a planilha `BoletosFormatados.xlsx` está no diretório correto (`C:/Users/victo/Desktop/boletos/`).
2. Coloque os arquivos PDF dos boletos, taxas de condomínio e repasses nas pastas correspondentes, conforme o mês vigente.
3. Execute o arquivo principal:
   ```sh
   python app.py
   ```
4. Utilize a interface gráfica para selecionar os imóveis e enviar os e-mails.

## Estrutura do Projeto

- [`app.py`](app.py): Script principal com a interface gráfica e lógica de envio.
- [`devedores.py`](devedores.py): Classe para manipulação dos dados dos devedores.
- `lg.png`: Imagem utilizada nos e-mails.
- `README.md`: Este arquivo.

## Observações

- O sistema utiliza a planilha já existente da empresa, sem necessidade de adaptações.
- Os e-mails são enviados utilizando as credenciais configuradas no código.

---
=======
Automatize o envio de boletos e relatórios financeiros por e-mail para inquilinos e proprietários da Vigor - Gestão de Negócios Imobiliários.

## ✨ Objetivo

Este projeto tem como objetivo agilizar o processo de envio de boletos, taxas condominiais e repasses, por meio de uma interface gráfica simples que utiliza a planilha já adotada pela empresa.

## ⚙️ Pré-requisitos

- Python 3 instalado
- Biblioteca `openpyxl`  
  Instale com:
  ```bash
  pip install openpyxl
  ```

## 🚀 Como usar

1. Certifique-se de que a planilha `BoletosFormatados.xlsx` está localizada na pasta correta:  
   `C:/Users/victo/Desktop/boletos/`
2. Adicione os arquivos PDF correspondentes aos boletos, taxas de condomínio e repasses nas pastas apropriadas, conforme o mês vigente.
3. Execute o script principal com o seguinte comando:
   ```bash
   python app.py
   ```
4. Use a interface gráfica para:
   - Selecionar os imóveis desejados
   - Visualizar os dados
   - Enviar os e-mails automaticamente

## 📁 Estrutura do Projeto

- `app.py`: Script principal com interface gráfica e lógica de envio de e-mails.
- `devedores.py`: Classe auxiliar para tratamento dos dados da planilha.
- `lg.png`: Imagem utilizada como logotipo nos e-mails.
- `README.md`: Este arquivo de instruções.

## 📝 Observações

- O sistema utiliza a planilha já existente da empresa, sem necessidade de adaptações.
