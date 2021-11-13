from string import digits, ascii_lowercase, ascii_uppercase

def VerificaCaracter(tipo, senha):
    v = 0
    n = 0
    while v == 0:
        for s in tipo:
            if s in senha:
                v += 1
                n += 1
            else:
                v += 1
    numero = False
    if n > 0:
        numero = True
    return numero

def RegrasSenha():
    regras = ['\nREGRAS PARA CADASTRO DA SENHA:\n',
    'Pelo menos uma letra minúscula;',
    'Pelo menos uma letra maiúscula;',
    'Pelo menos um caractere especial;',
    'Minímo de 8 caracteres.']
    for c in regras:
        print(f'\033[33m{c}\033[m')
    print('')

def MensagemInicial():
    mensagem_user = '####### CADASTRAMENTO DE USUARIO #######'
    print('\n\033[33m' + '#'*len(mensagem_user) + '\033[m')
    print(f'\033[33m{mensagem_user:^{len(mensagem_user)}}\033[m')
    print('\033[33m' + '#'*len(mensagem_user) + '\033[m')

MensagemInicial()
usuario = str(input('\nDigite o nome do usuario: '))

while True:
    RegrasSenha()
    senha = str(input("Digite uma senha: ")).replace(" ", "")

    if len(senha) >= 8:
        numero = VerificaCaracter(digits, senha)
        maiscula = VerificaCaracter(ascii_lowercase, senha)
        minuscula = VerificaCaracter(ascii_uppercase, senha)
        especiais = VerificaCaracter('$#@', senha)
        if numero and maiscula and especiais and minuscula == True:
            print("\n\033[32mSenha cadastrada com sucesso!\033[m")
            break
        else:
            print('\n\033[31m' + '#'*58)
            print("Senha invalidos! Por favor digite conforme as regras.\033[m")
    else:
        print('\n\033[31m' + '#'*46)
        print("Senha invalida! Digite no minímo 8 caracteres.\033[m")

salvar = open('login.txt', 'a', encoding="utf-8")
salvar.write(f'Username: {usuario}\n')
salvar.write(f'Senha: {senha}\n\n')
salvar.close()
