# Recebe a hora do usuário
hora = input("Digite a hora no formato HH:MM:SS: ")

# Verifica se a hora está no formato correto (HH:MM:SS)
if len(hora) == 8 and hora[2] == ':' and hora[5] == ':':
    # Extrai horas, minutos e segundos da string de hora
    horas = int(hora[0:2])  # Pega os primeiros 2 caracteres e converte para inteiro
    minutos = int(hora[3:5])  # Pega os caracteres do meio (3 e 4) e converte para inteiro
    segundos = int(hora[6:8])  # Pega os últimos 2 caracteres e converte para inteiro

    # Verifica se as horas, minutos e segundos são válidos
    if 0 <= horas <= 23 and 0 <= minutos <= 59 and 0 <= segundos <= 59:
        print("A hora é válida ")
    else:
        print("A hora não é válida ")
else:
    print("A hora é não válida ")
