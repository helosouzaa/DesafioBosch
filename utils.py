from models import Line, User
def read_data(data):
    # Utilização listas para armazenar os objetos de usuários e linhas telefônicas
    users = []
    lines = []

    # Processa cada entrada na lista de dados
    for entry in data:
        name, email, adress, phone_line, plan = map(str.strip, entry.split(","))
        
                
        # Instâncias das classes com os dados processados
        user = User(name, email, adress)
        line = Line(phone_line, plan)

        # Adiciona os objetos criados às listas de cada um
        users.append(user)
        lines.append(line)

    return users, lines