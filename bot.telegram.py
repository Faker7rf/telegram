import random
import telebot

chave_api = '6363962561:AAEF0U1gqK-LNH57gAIqLYcOy3J8-kRWBpc'

bot = telebot.TeleBot(chave_api)

#opção 1

@bot.message_handler(commands = ['A'])
def A(mensagem):

    a = int(random.randint(0 , 9))
    b = int(random.randint(0 , 9)) 
    c = int(random.randint(0 , 9)) 
    d = int(random.randint(0 , 9)) 
    e = int(random.randint(0 , 9)) 
    f = int(random.randint(0 , 9)) 
    g = int(random.randint(0 , 9))
    h = int(random.randint(0 , 9))

    #unidade federal
    i = 1


    #calculo digito A

    soma_a = (a * 10) + (b * 9) + (c * 8) + (d * 7)  + (e * 6) + (f * 5) + (g * 4) + (h * 3) + (i * 2)
    resto_a = soma_a % 11
    digito_a = 0 if resto_a < 2 else 11 - resto_a

    #calculo digito B

    soma_b = (b * 10) + (c * 9) + (d * 8)  + (e * 7) + (f * 6) + (g * 5) + (h * 4) + (i * 3) + (digito_a * 2)
    resto_b = soma_b % 11
    digito_b = 0 if resto_b < 2 else 11 - resto_b

    cpf = ('{}{}{}.{}{}{}.{}{}{}-{}{}'.format(a , b , c , d , e , f , g , h , i , digito_a , digito_b))
    

    bot.reply_to(mensagem , cpf + '''

Para verificar a situação do CPF, recomendamos @SituacaoCadastralBot !!''')


    bot.send_message(mensagem.chat.id , '''Deseja gerar outro?
/SIM 
/NAO

Clique na opção desejada!!
''')
    
@bot.message_handler(commands = ['SIM'])
def SIM(mensagem):
    return responder(mensagem)

@bot.message_handler(commands = ['NAO'])
def NAO(mensagem):
   bot.send_message(mensagem.chat.id , 'Até mais!!')


#opção 2
@bot.message_handler(commands = ['B'])
def B(mensagem):

    a = int(random.randint(0 , 9))
    b = int(random.randint(0 , 9)) 
    c = int(random.randint(0 , 9)) 
    d = int(random.randint(0 , 9)) 
    e = int(random.randint(0 , 9)) 
    f = int(random.randint(0 , 9)) 
    g = int(random.randint(0 , 9))
    h = int(random.randint(0 , 9))

    #unidade federal
    i = 2


    #calculo digito A

    soma_a = (a * 10) + (b * 9) + (c * 8) + (d * 7)  + (e * 6) + (f * 5) + (g * 4) + (h * 3) + (i * 2)
    resto_a = soma_a % 11
    digito_a = 0 if resto_a < 2 else 11 - resto_a

    #calculo digito B

    soma_b = (b * 10) + (c * 9) + (d * 8)  + (e * 7) + (f * 6) + (g * 5) + (h * 4) + (i * 3) + (digito_a * 2)
    resto_b = soma_b % 11
    digito_b = 0 if resto_b < 2 else 11 - resto_b

    cpf = ('{}{}{}.{}{}{}.{}{}{}-{}{}'.format(a , b , c , d , e , f , g , h , i , digito_a , digito_b))

    bot.reply_to(mensagem, cpf + '''

Para verificar a situação do CPF, recomendamos @SituacaoCadastralBot !!''')

    bot.send_message(mensagem.chat.id , '''Deseja gerar outro?
/SIM 
/NAO

Clique na opção desejada!!
''')
    
@bot.message_handler(commands = ['SIM'])
def SIM(mensagem):
    return responder(mensagem)

@bot.message_handler(commands = ['NAO'])
def NAO(mensagem):
   bot.send_message(mensagem.chat.id , 'Até mais!!')



#opção 3
@bot.message_handler(commands = ['C'])
def C(mensagem):
    a = int(random.randint(0 , 9))
    b = int(random.randint(0 , 9)) 
    c = int(random.randint(0 , 9)) 
    d = int(random.randint(0 , 9)) 
    e = int(random.randint(0 , 9)) 
    f = int(random.randint(0 , 9)) 
    g = int(random.randint(0 , 9))
    h = int(random.randint(0 , 9))

    #unidade federal
    i = 3


    #calculo digito A

    soma_a = (a * 10) + (b * 9) + (c * 8) + (d * 7)  + (e * 6) + (f * 5) + (g * 4) + (h * 3) + (i * 2)
    resto_a = soma_a % 11
    digito_a = 0 if resto_a < 2 else 11 - resto_a

    #calculo digito B

    soma_b = (b * 10) + (c * 9) + (d * 8)  + (e * 7) + (f * 6) + (g * 5) + (h * 4) + (i * 3) + (digito_a * 2)
    resto_b = soma_b % 11
    digito_b = 0 if resto_b < 2 else 11 - resto_b

    cpf = ('{}{}{}.{}{}{}.{}{}{}-{}{}'.format(a , b , c , d , e , f , g , h , i , digito_a , digito_b))

    bot.reply_to(mensagem, cpf + '''

Para verificar a situação do CPF, recomendamos @SituacaoCadastralBot !!''')

    bot.send_message(mensagem.chat.id , '''Deseja gerar outro?
/SIM 
/NAO

Clique na opção desejada!!
''')
    
@bot.message_handler(commands = ['SIM'])
def SIM(mensagem):
    return responder(mensagem)

@bot.message_handler(commands = ['NAO'])
def NAO(mensagem):
   bot.send_message(mensagem.chat.id , 'Até mais!!')



#opção 4
@bot.message_handler(commands = ['D'])
def D(mensagem):
    a = int(random.randint(0 , 9))
    b = int(random.randint(0 , 9)) 
    c = int(random.randint(0 , 9)) 
    d = int(random.randint(0 , 9)) 
    e = int(random.randint(0 , 9)) 
    f = int(random.randint(0 , 9)) 
    g = int(random.randint(0 , 9))
    h = int(random.randint(0 , 9))

    #unidade federal
    i = 4


    #calculo digito A

    soma_a = (a * 10) + (b * 9) + (c * 8) + (d * 7)  + (e * 6) + (f * 5) + (g * 4) + (h * 3) + (i * 2)
    resto_a = soma_a % 11
    digito_a = 0 if resto_a < 2 else 11 - resto_a

    #calculo digito B

    soma_b = (b * 10) + (c * 9) + (d * 8)  + (e * 7) + (f * 6) + (g * 5) + (h * 4) + (i * 3) + (digito_a * 2)
    resto_b = soma_b % 11
    digito_b = 0 if resto_b < 2 else 11 - resto_b

    cpf = ('{}{}{}.{}{}{}.{}{}{}-{}{}'.format(a , b , c , d , e , f , g , h , i , digito_a , digito_b))

    bot.reply_to(mensagem, cpf + '''

Para verificar a situação do CPF, recomendamos @SituacaoCadastralBot !!''')

    bot.send_message(mensagem.chat.id , '''Deseja gerar outro?
/SIM 
/NAO

Clique na opção desejada!!
''')
    
@bot.message_handler(commands = ['SIM'])
def SIM(mensagem):
    return responder(mensagem)

@bot.message_handler(commands = ['NAO'])
def NAO(mensagem):
   bot.send_message(mensagem.chat.id , 'Até mais!!')



#opção 5
@bot.message_handler(commands = ['E'])
def E(mensagem):
    a = int(random.randint(0 , 9))
    b = int(random.randint(0 , 9)) 
    c = int(random.randint(0 , 9)) 
    d = int(random.randint(0 , 9)) 
    e = int(random.randint(0 , 9)) 
    f = int(random.randint(0 , 9)) 
    g = int(random.randint(0 , 9))
    h = int(random.randint(0 , 9))

    #unidade federal
    i = 5


    #calculo digito A

    soma_a = (a * 10) + (b * 9) + (c * 8) + (d * 7)  + (e * 6) + (f * 5) + (g * 4) + (h * 3) + (i * 2)
    resto_a = soma_a % 11
    digito_a = 0 if resto_a < 2 else 11 - resto_a

    #calculo digito B

    soma_b = (b * 10) + (c * 9) + (d * 8)  + (e * 7) + (f * 6) + (g * 5) + (h * 4) + (i * 3) + (digito_a * 2)
    resto_b = soma_b % 11
    digito_b = 0 if resto_b < 2 else 11 - resto_b

    cpf = ('{}{}{}.{}{}{}.{}{}{}-{}{}'.format(a , b , c , d , e , f , g , h , i , digito_a , digito_b))

    bot.reply_to(mensagem, cpf + '''

Para verificar a situação do CPF, recomendamos @SituacaoCadastralBot !!''')

    bot.send_message(mensagem.chat.id , '''Deseja gerar outro?
/SIM 
/NAO

Clique na opção desejada!!
''')
    
@bot.message_handler(commands = ['SIM'])
def SIM(mensagem):
    return responder(mensagem)

@bot.message_handler(commands = ['NAO'])
def NAO(mensagem):
   bot.send_message(mensagem.chat.id , 'Até mais!!')



#opção 6
@bot.message_handler(commands = ['F'])
def F(mensagem):
    a = int(random.randint(0 , 9))
    b = int(random.randint(0 , 9)) 
    c = int(random.randint(0 , 9)) 
    d = int(random.randint(0 , 9)) 
    e = int(random.randint(0 , 9)) 
    f = int(random.randint(0 , 9)) 
    g = int(random.randint(0 , 9))
    h = int(random.randint(0 , 9))

    #unidade federal
    i = 6


    #calculo digito A

    soma_a = (a * 10) + (b * 9) + (c * 8) + (d * 7)  + (e * 6) + (f * 5) + (g * 4) + (h * 3) + (i * 2)
    resto_a = soma_a % 11
    digito_a = 0 if resto_a < 2 else 11 - resto_a

    #calculo digito B

    soma_b = (b * 10) + (c * 9) + (d * 8)  + (e * 7) + (f * 6) + (g * 5) + (h * 4) + (i * 3) + (digito_a * 2)
    resto_b = soma_b % 11
    digito_b = 0 if resto_b < 2 else 11 - resto_b

    cpf = ('{}{}{}.{}{}{}.{}{}{}-{}{}'.format(a , b , c , d , e , f , g , h , i , digito_a , digito_b))

    bot.reply_to(mensagem, cpf + '''

Para verificar a situação do CPF, recomendamos @SituacaoCadastralBot !!''')

    bot.send_message(mensagem.chat.id , '''Deseja gerar outro?
/SIM 
/NAO

Clique na opção desejada!!
''')
    
@bot.message_handler(commands = ['SIM'])
def SIM(mensagem):
    return responder(mensagem)

@bot.message_handler(commands = ['NAO'])
def NAO(mensagem):
   bot.send_message(mensagem.chat.id , 'Até mais!!')

  

#opção 7
@bot.message_handler(commands = ['G'])
def G(mensagem):
    a = int(random.randint(0 , 9))
    b = int(random.randint(0 , 9)) 
    c = int(random.randint(0 , 9)) 
    d = int(random.randint(0 , 9)) 
    e = int(random.randint(0 , 9)) 
    f = int(random.randint(0 , 9)) 
    g = int(random.randint(0 , 9))
    h = int(random.randint(0 , 9))

    #unidade federal
    i = 7


    #calculo digito A

    soma_a = (a * 10) + (b * 9) + (c * 8) + (d * 7)  + (e * 6) + (f * 5) + (g * 4) + (h * 3) + (i * 2)
    resto_a = soma_a % 11
    digito_a = 0 if resto_a < 2 else 11 - resto_a

    #calculo digito B

    soma_b = (b * 10) + (c * 9) + (d * 8)  + (e * 7) + (f * 6) + (g * 5) + (h * 4) + (i * 3) + (digito_a * 2)
    resto_b = soma_b % 11
    digito_b = 0 if resto_b < 2 else 11 - resto_b

    cpf = ('{}{}{}.{}{}{}.{}{}{}-{}{}'.format(a , b , c , d , e , f , g , h , i , digito_a , digito_b))

    bot.reply_to(mensagem, cpf + '''

Para verificar a situação do CPF, recomendamos @SituacaoCadastralBot !!''')

    bot.send_message(mensagem.chat.id , '''Deseja gerar outro?
/SIM 
/NAO

Clique na opção desejada!!
''')
    
@bot.message_handler(commands = ['SIM'])
def SIM(mensagem):
    return responder(mensagem)

@bot.message_handler(commands = ['NAO'])
def NAO(mensagem):
   bot.send_message(mensagem.chat.id , 'Até mais!!')



#opção 8
@bot.message_handler(commands = ['H'])
def H(mensagem):
    a = int(random.randint(0 , 9))
    b = int(random.randint(0 , 9)) 
    c = int(random.randint(0 , 9)) 
    d = int(random.randint(0 , 9)) 
    e = int(random.randint(0 , 9)) 
    f = int(random.randint(0 , 9)) 
    g = int(random.randint(0 , 9))
    h = int(random.randint(0 , 9))

    #unidade federal
    i = 8


    #calculo digito A

    soma_a = (a * 10) + (b * 9) + (c * 8) + (d * 7)  + (e * 6) + (f * 5) + (g * 4) + (h * 3) + (i * 2)
    resto_a = soma_a % 11
    digito_a = 0 if resto_a < 2 else 11 - resto_a

    #calculo digito B

    soma_b = (b * 10) + (c * 9) + (d * 8)  + (e * 7) + (f * 6) + (g * 5) + (h * 4) + (i * 3) + (digito_a * 2)
    resto_b = soma_b % 11
    digito_b = 0 if resto_b < 2 else 11 - resto_b

    cpf = ('{}{}{}.{}{}{}.{}{}{}-{}{}'.format(a , b , c , d , e , f , g , h , i , digito_a , digito_b))

    bot.reply_to(mensagem, cpf + '''

Para verificar a situação do CPF, recomendamos @SituacaoCadastralBot !!''')

    bot.send_message(mensagem.chat.id , '''Deseja gerar outro?
/SIM 
/NAO

Clique na opção desejada!!
''')
    
@bot.message_handler(commands = ['SIM'])
def SIM(mensagem):
    return responder(mensagem)

@bot.message_handler(commands = ['NAO'])
def NAO(mensagem):
   bot.send_message(mensagem.chat.id , 'Até mais!!')



#opção 9
@bot.message_handler(commands = ['I'])
def I(mensagem):
    a = int(random.randint(0 , 9))
    b = int(random.randint(0 , 9)) 
    c = int(random.randint(0 , 9)) 
    d = int(random.randint(0 , 9)) 
    e = int(random.randint(0 , 9)) 
    f = int(random.randint(0 , 9)) 
    g = int(random.randint(0 , 9))
    h = int(random.randint(0 , 9))

    #unidade federal
    i = 9


    #calculo digito A

    soma_a = (a * 10) + (b * 9) + (c * 8) + (d * 7)  + (e * 6) + (f * 5) + (g * 4) + (h * 3) + (i * 2)
    resto_a = soma_a % 11
    digito_a = 0 if resto_a < 2 else 11 - resto_a

    #calculo digito B

    soma_b = (b * 10) + (c * 9) + (d * 8)  + (e * 7) + (f * 6) + (g * 5) + (h * 4) + (i * 3) + (digito_a * 2)
    resto_b = soma_b % 11
    digito_b = 0 if resto_b < 2 else 11 - resto_b

    cpf = ('{}{}{}.{}{}{}.{}{}{}-{}{}'.format(a , b , c , d , e , f , g , h , i , digito_a , digito_b))

    bot.reply_to(mensagem, cpf + '''

Para verificar a situação do CPF, recomendamos @SituacaoCadastralBot !!''')

    bot.send_message(mensagem.chat.id , '''Deseja gerar outro?
/SIM 
/NAO

Clique na opção desejada!!
''')
    
    @bot.message_handler(commands = ['SIM'])
    def SIM(mensagem):
        return responder(mensagem)

    @bot.message_handler(commands = ['NAO'])
    def NAO(mensagem):
     bot.send_message(mensagem.chat.id , 'Até mais!!')




#opção 0
@bot.message_handler(commands = ['J'])
def J(mensagem):
    a = int(random.randint(0 , 9))
    b = int(random.randint(0 , 9)) 
    c = int(random.randint(0 , 9)) 
    d = int(random.randint(0 , 9)) 
    e = int(random.randint(0 , 9)) 
    f = int(random.randint(0 , 9)) 
    g = int(random.randint(0 , 9))
    h = int(random.randint(0 , 9))

    #unidade federal
    i = 0


    #calculo digito A

    soma_a = (a * 10) + (b * 9) + (c * 8) + (d * 7)  + (e * 6) + (f * 5) + (g * 4) + (h * 3) + (i * 2)
    resto_a = soma_a % 11
    digito_a = 0 if resto_a < 2 else 11 - resto_a

    #calculo digito B

    soma_b = (b * 10) + (c * 9) + (d * 8)  + (e * 7) + (f * 6) + (g * 5) + (h * 4) + (i * 3) + (digito_a * 2)
    resto_b = soma_b % 11
    digito_b = 0 if resto_b < 2 else 11 - resto_b

    cpf = ('{}{}{}.{}{}{}.{}{}{}-{}{}'.format(a , b , c , d , e , f , g , h , i , digito_a , digito_b))

    bot.reply_to(mensagem, cpf + '''

Para verificar a situação do CPF, recomendamos @SituacaoCadastralBot !!''')

    bot.send_message(mensagem.chat.id , '''Deseja gerar outro?
/SIM 
/NAO

Clique na opção desejada!!
''')
    
    @bot.message_handler(commands = ['SIM'])
    def SIM(mensagem):
        return responder(mensagem)

    @bot.message_handler(commands = ['NAO'])
    def NAO(mensagem):
        bot.send_message(mensagem.chat.id , 'Até mais!!')













def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = '''Deseja emitir o cpf de qual estado?

    /A - DF, GO, MS, MT e TO

    /B - AC, AM, AP, PA, RO e RR

    /C - CE, MA e PI

    /D - AL, PB, PE e RN

    /E - BA e SE
    
    /F - MG

    /G - ES e RJ

    /H - SP

    /I - PR e SC

    /J - RS

CLIQUE NA OPÇÃO DESEJADA, QUALQUER OUTRO COMANDO NÃO IRÁ FUNCIONAR!!
    '''''
    bot.reply_to (mensagem , texto)






bot.polling()