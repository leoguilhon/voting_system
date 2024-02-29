
votes = [0, 0, 0, 0, 0]

i = True

with open('eleicao.csv', 'w') as arquivo_csv:
    arquivo_csv.write("A\t B\t C\t Nulo\t Branco\n")

while i is True:
    vote = input('Insira o seu voto: A, B, C, Nulo, Branco ou Sair').lower()
    match vote:
        case "a":
            votes[0] += 1
        case "b":
            votes[1] += 1
        case "c":
            votes[2] += 1
        case "nulo":
            votes[3] += 1
        case "branco":
            votes[4] += 1
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

total_votes = votes[0] + votes[1] + votes[2] + votes[3] + votes[4]

if total_votes != 0:
    with open('eleicao_total.csv', 'w') as arquivo_csv:
        arquivo_csv.write("A\t B\t C\t Nulo\t Branco\n")
        linha = f"{votes[0]}\t{votes[1]}\t{votes[2]}\t{votes[3]}\t{votes[4]}\n"
        arquivo_csv.write(linha)
else:
    pass


    