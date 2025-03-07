Gerador de QR Code:


Este é um projeto de um Gerador de QR Code usando FastAPI para o backend e um site HTML/CSS/JavaScript para a interface. O usuário pode inserir um link e obter um QR Code correspondente.

---

- Tecnologias Utilizadas:
- Python (FastAPI, qrcode)
- HTML, CSS, JavaScript (Frontend simples)
- Uvicorn (Servidor ASGI para rodar o FastAPI)

---

📂 Estrutura do Projeto
```
gerador_qr/
│-- venv/                  # Ambiente Virtual (opcional)
│-- static/
│   │-- style.css          # Estilos do site
│-- templates/
│   │-- index.html         # Página principal
│-- qr_code_generator.py   # Código do Backend (FastAPI)
│-- README.md              # Documentação do projeto
```

---

Como Executar o Projeto

1 - Clonar o Repositório
```
git clone https://github.com/seu-usuario/gerador_qr.git
cd gerador_qr

```

2- Criar um Ambiente Virtual (Opcional, Recomendado)
```
python -m venv venv

```

Ativar o ambiente virtual:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

3 - Instalar as Dependências
```
pip install fastapi qrcode[pil] uvicorn
```

4 - Rodar o Backend
```
uvicorn qr_code_generator:app --reload

```
O servidor será iniciado em http://127.0.0.1:8000.

5 - Abrir o Frontend
Basta abrir o arquivo `index.html` no navegador e testar!

---


Desenvolvido com 💙 por José Renato. <3


 
