from sqlalchemy import create_engine

def get_engine():
    # Substitua 'root', 'senha' e 'gestaodados' pelos seus dados de usuário, senha e banco de dados do MySQL Workbench
    usuario = "root"
    senha = "senha"
    host = "localhost"
    banco = "gestaodados"
    
    url = f"mysql+mysqlconnector://{usuario}:{senha}@{host}/{banco}"
    return create_engine(url)