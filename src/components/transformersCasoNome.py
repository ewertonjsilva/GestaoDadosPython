import pandas as pd

def tratar_capitalizacao(nome_trecho):
    """
    Mantém preposições em minúsculo e o restante em maiúsculo (ou Capitalizado).
    Exemplo: 'ana da silva' -> 'ANA da SILVA'
    """
    particulas = ['de', 'da', 'do', 'das', 'dos', 'e']
    palavras = nome_trecho.lower().split()
    
    resultado = [p.upper() if p not in particulas else p.lower() for p in palavras]
    return " ".join(resultado)

def processar_usuarios_etl(df, estrategia='primeiro_termo'):
    """
    Transforma nomes complexos com tratamento de exceções brasileiras.
    Estratégias: 'primeiro_termo' ou 'ultimo_sobrenome'
    """
    # Limpeza inicial: remove espaços extras nas extremidades
    df['nome_completo'] = df['nome_completo'].str.strip()
    
    primeiros_nomes = []
    sobrenomes = []

    for nome in df['nome_completo']:
        partes = nome.split()
        
        if len(partes) <= 1:
            primeiros_nomes.append(nome.upper())
            sobrenomes.append('NÃO INFORMADO')
            continue

        if estrategia == 'primeiro_termo':
            # Caso: Ewerton | José da Silva
            p_nome = partes[0]
            s_nome = " ".join(partes[1:])
        else:
            # Caso: Ewerton José da | Silva (Citação Acadêmica)
            p_nome = " ".join(partes[:-1])
            s_nome = partes[-1]

        # Aplicando a regra de preposições
        primeiros_nomes.append(tratar_capitalizacao(p_nome))
        sobrenomes.append(tratar_capitalizacao(s_nome))

    # Criando o DataFrame final
    df_final = pd.DataFrame({
        'primeiro_nome': primeiros_nomes,
        'sobrenome': sobrenomes
    })
    
    return df_final