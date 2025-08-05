# E-commerce

## 🚀 Como começar

Siga estas etapas para configurar e executar o projeto na sua máquina local.

### 📋 Pré-requisitos

Certifique-se de ter o Python 3.x e o Git instalados.

### 💻 Instalação

1.  **Clone o repositório:**
    Abra o seu terminal e execute o seguinte comando para baixar o projeto.

    ```bash
    git clone [https://github.com/LzGuimaraes/E-commerce.git](https://github.com/LzGuimaraes/E-commerce.git)
    cd E-commerce
    ```

    > **Nota:** Se o projeto já estiver clonado e você precisar apenas atualizar para a versão mais recente, use `git pull` na pasta raiz do projeto.
    >
    > ```bash
    > git pull origin main
    > ```

2.  **Crie e ative o ambiente virtual:**
    É uma boa prática isolar as dependências do projeto.

    ```bash
    python -m venv venv
    # No Windows:
    venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    Instale todas as bibliotecas necessárias para o projeto.

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuração do banco de dados:**
    Aplique as migrações para configurar o banco de dados.

    ```bash
    python manage.py migrate
    ```

### 🏃 Executando o servidor

Para iniciar o servidor de desenvolvimento, execute o seguinte comando na pasta do projeto:

```bash
python manage.py runserver