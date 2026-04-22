import pandas as pd

def processar_usuarios_etl(df):
    """
    Transforma a coluna 'nome_completo' em 'primeiro_nome' e 'sobrenome'.
    Também aplica a padronização para MAIÚSCULAS.
    """
    # Split no primeiro espaço: n=1 garante que "João Pedro Silva" vire ["João", "Pedro Silva"]
    df_split = df['nome_completo'].str.split(' ', n=1, expand=True)
    
    # Criando o novo DataFrame estruturado
    df_final = pd.DataFrame()
    df_final['primeiro_nome'] = df_split[0].str.upper()
    df_final['sobrenome'] = df_split[1].str.upper()
    
    # Tratando casos onde o sobrenome pode ser nulo
    df_final['sobrenome'] = df_final['sobrenome'].fillna('NÃO INFORMADO')
    
    return df_final