numero = int(input("Digite os segundos: "))

a = numero//86400 #dias
b = (numero%86400)//3600 #horas
c = ((numero%86400)%3600)//60 #minutos
d = ((numero%86400)%3600)%60
print (a,'dias',b,'horas',c,'minutos e',d,'segundos.')
