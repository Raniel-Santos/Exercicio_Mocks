## Execução do projeto

## Branches
Os exercícios estão separados por branches, sendo:

- Exercício_01 = Branch "Ex_01"
- Exercício_02 = Branch "Ex_02"

Para executar, basta selecionar a branch responsável por cada exercício.


#### 1. Criação do ambiente virtual.
Abra um terminal dentro da pasta do projeto e execute o comando abaixo.
```bash
python -m venv venv
```

#### 2. Ativar o ambiente virtual.
Para ativar o ambiente virtual execute o comando abaixo.
```bash
.\venv\Scripts\activate
```

#### 3. Instalação das dependências.
Para instalar todas as dependencias do projeto execute o comando abaixo.
```bash
pip install -r requirements.txt
```

#### 4. Realize a Cobertura e os Testes.
rode o comando abaixo 
```bash
pytest --cov .\test\