from utils import read_data

# Dados de entrada com informações dos usuários e suas linhas telefônicas
data = [
    "Bob, bob@xyzzzzzz.com, Rua 12 de Abril, +5500000000000, 40GB",
    "Alice, alice@xyzzzzzz.com, Rua Brasil, +5500111111111, 10GB"
]

# Chamada da função read_data para processar os dados e obter listas de objetos

users, lines = read_data(data)

# Percorre simultaneamente as listas e imprime a frase formatada para cada usuário e linha
for user, line in zip(users, lines):
    print(f"O cliente, {user.name}, com email, {user.email}, morador do endereço, {user.adress}, "
          f"dono da linha, {line.phone_line} com plano contratado de {line.plan}")