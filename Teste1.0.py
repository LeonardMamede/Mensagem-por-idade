nome = input('Qual é seu nome?')
idade = int(input('Qual é sua idade?'))

print ('Oii, prezer em conhecer você', nome)

if idade < 18:
    print ('Wont você ainda está descobrindo a vida')
elif idade == 18:
    print ('Agora tudo vai depenser somente se você!')
elif idade <= 29:
    print ('Nunca desista! Se acha que não vai dar certo mesmo persistindo, muda de caminho, mas sempre para o caminho do seu objetivo!')
elif idade <= 39:
    resposta = input('Como está os frutos até aqui?')
    if "bem" in resposta.lower() or "boa" in resposta.lower() or "otima" in resposta.lower():
        print ('Fico feliz em saber disso!')
    elif "mal" in resposta.lower() or "ruim" in resposta.lower():
        print ('Nunca desiste, tempos ruins iram passar!')
    else:
        print('Entendi')
elif idade <= 60:
    print('Só mais um pouco para de aponsentar!')
else:
    print('Bora curtir a vida poha')


