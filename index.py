estoque_atual = {
    "canetas": 150,
    "cadernos": 95,
    "lapis": 200,
    "livros": 100,
    "notebook": 300,
    "mochilas": 75,
    "borracha": 180,
    "marcadores": 120,
    "réguas": 90,
    "calculadoras": 40,
    "agendas": 60,
    "post-its": 250,
    "tesouras": 85,
    "clipes": 500,
    "grampeadores": 70,
    "fichários": 55,
    "papel Sulfite": 1000,
    "pendrives": 130,
    "lousas": 20,
    "apontadores": 100
}

movimentacoes_dia = [
    ("canetas", "saida", 25),
    ("cadernos", "entrada", 25),
    ("lapis", "entrada", 40),
    ("livros", "saida", 10),
    ("notebook", "entrada", 50),
    ("mochilas", "saida", 75),
    ("borracha", "entrada", 180),
    ("marcadores", "entrada", 20),
    ("réguas", "saida", 10),
    ("calculadoras", "saida", 40),
    ("agendas", "saida", 50),
    ("post-its", "entrada", 20),
    ("tesouras", "entrada", 60),
    ("clipes", "entrada", 80),
    ("grampeadores", "entrada", 300),
    ("fichários", "saida", 500),
    ("papel Sulfite", "saida", 300),
    ("pendrives", "entrada", 700),
    ("lousas", "saida", 5),
    ("apontadores", "entrada", 20),
]

while True:
    print('\n************************** Seja bem-vindo a papelaria dos BUGHUNTERS **************************')
    menu = int(input('Digite sua opção: \n[1]Ver estoque\n[2]Ler movimentações\n[3]Sair\n:'))
    match menu:
        case 1:
            for produto, valor in estoque_atual.items():
                print(f'Produto: {produto} | Quantidade: {valor}')
        case 2:
            for produto, operacao, valor in movimentacoes_dia:
                print(f'Produto: {produto} | Operação: {operacao} | Quantidade: {valor}')
                
                if produto not in estoque_atual:
                    estoque_atual[produto] = 0  

                if operacao == "entrada":
                    estoque_atual[produto] += valor
                elif operacao == "saida":
                    estoque_atual[produto] -= valor
                    
                    if(valor<50):
                        print(f'Nivel Báixo, por favor reponha o produto: {produto}')
        case 3:
            break