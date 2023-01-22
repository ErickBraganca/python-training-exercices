def code_verification():
    inputed_code = input("Digite o código:")
    # Armazena a quantidade de digitos no código imputado
    code_lenght = len(inputed_code)

    if code_lenght == 15:
        try:
            converted_code = int(inputed_code)
            print("Código Validado")

        except ValueError:
            print("Inválido: Código não é formado por números")
    else:
       print("Inválido: Quantidade Incorreta de Digitos") 


code_verification()
