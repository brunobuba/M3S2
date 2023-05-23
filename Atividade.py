# Atividade com o objetivo de criar um decorator para imprir as informações de funções para cálculo de juros

# Criação do decorator para impressão
def decorator_imprimir(func):
    def inner(capital, taxa, tempo):
        print('CAPITAL: {} TAXA: {} TEMPO: {}'.format(capital, taxa, tempo))
        print(func(capital, taxa, tempo))
    return inner

# Exemplo de função para cálculo de juros
@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo


juros_simples(1000, 5, 6)
