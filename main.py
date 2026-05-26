# ==========================================
# Sistema de Validação de Senhas
# ==========================================
# Objetivo:
# Cadastrar 5 funcionários validando:
# - Senhas iguais
# - Mínimo de 6 caracteres
# ==========================================

print("===================================")
print(" SISTEMA DE CADASTRO DE SENHAS ")
print("===================================")

# FOR para repetir o cadastro de 5 funcionários
for funcionario in range(1, 6):

    print(f"\nFuncionário {funcionario}")

    # Variável de controle
    senha_valida = False

    # WHILE executa enquanto a senha for inválida
    while senha_valida == False:

        # Entrada da senha
        senha = input("Digite a senha: ")

        # Confirmação da senha
        confirmacao = input("Confirme a senha: ")

        # Verifica se:
        # 1. As senhas são iguais
        # 2. A senha possui pelo menos 6 caracteres
        if senha == confirmacao and len(senha) >= 6:

            print("Senha cadastrada com sucesso!")
            senha_valida = True

        else:
            print("\nERRO!")
            print("As senhas devem ser iguais")
            print("e possuir no mínimo 6 caracteres.\n")

print("\nTodos os funcionários foram cadastrados!")
