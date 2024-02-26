vote_a = 0
vote_b = 0
vote_c = 0
vote_null = 0
vote_white = 0

i = 0

with open('eleicao.csv', 'w') as arquivo_csv:
    arquivo_csv.write("A\t B\t C\t Nulo\t Branco\n")

while i < 10:
    vote = input('Insira o seu voto: A, B, C, Nulo ou Branco').lower()
    match vote:
        case "a":
            vote_a += 1
        case "b":
            vote_b += 1
        case "c":
            vote_c += 1
        case "nulo":
            vote_null += 1
        case "branco":
            vote_white += 1
            print('Voto computado com sucesso.')
        case _:
            print("Valor {} inválido".format(vote))
            continue

    with open('eleicao.csv', 'a') as arquivo_csv:
        linha = f"{1 if vote == 'a' else 0}\t{1 if vote == 'b' else 0}\t{1 if vote == 'c' else 0}\t{1 if vote == 'nulo' else 0}\t{1 if vote == 'branco' else 0}\n"
        arquivo_csv.write(linha)
    print('Voto computado com sucesso.')
    i += 1

    