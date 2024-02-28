vote_a = 0
vote_b = 0
vote_c = 0
vote_null = 0
vote_white = 0



i = True

with open('eleicao.csv', 'w') as arquivo_csv:
    arquivo_csv.write("A\t B\t C\t Nulo\t Branco\n")

while i is True:
    vote = input('Insira o seu voto: A, B, C, Nulo, Branco ou Sair').lower()
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
        case "sair":
            print('Votação encerrada.')
            i = False
            break
        case _:
            print("Valor {} inválido".format(vote))
            continue
    with open('eleicao.csv', 'a') as arquivo_csv:
        linha = f"{1 if vote == 'a' else 0}\t{1 if vote == 'b' else 0}\t{1 if vote == 'c' else 0}\t{1 if vote == 'nulo' else 0}\t{1 if vote == 'branco' else 0}\n"
        arquivo_csv.write(linha)
        print('Voto computado com sucesso.')

total_votes = vote_a + vote_b + vote_c + vote_null + vote_white

if total_votes != 0:
    with open('eleicao_total.csv', 'w') as arquivo_csv:
        arquivo_csv.write("A\t B\t C\t Nulo\t Branco\n")
        linha = f"{vote_a}\t{vote_b}\t{vote_c}\t{vote_null}\t{vote_white}\n"
        arquivo_csv.write(linha)
else:
    pass


    