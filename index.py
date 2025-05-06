from bancodados import conexao

cursor = conexao.cursor()

def obterdado():

    todos_os_valoeres = []

    while True:

        nome = input("Qual é o seu nome: ")

        if nome == "sair":
            cursor.close()
            conexao.close()
            break

        else:
            altura = int(input("Qual é a sua altura em centimetros: "))
            valores = [nome, altura]
            todos_os_valoeres.append(valores)

            query = "INSERT INTO altura (nome, altura) VALUES (%s, %s)"
            cursor.execute(query, valores)
            conexao.commit()

            print(f"{cursor.rowcount} registros inseridos.")

obterdado()











print("teste")