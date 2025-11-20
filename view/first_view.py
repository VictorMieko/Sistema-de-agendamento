def introduction_page():
    message = """
    Seja bem vindo ao sistema de agendamento de consultas!
    Escolha uma das opções abaixo:
    [1] - Cadastrar novo cliente 
    [2] - procurar procurar paciente por CPF
    [3] - Agendar nova consulta
    [4] - Listar consultas marcadas
    [0] - Sair do sistema
    """

    print(message)
    command = input("Digite o número da opção desejada: ")

    return command