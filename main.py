import random as r, string as s

elements = s.ascii_letters + s.ascii_uppercase + s.digits + s.punctuation 
psw = ""
lenght = int(input( "¿Cuántos caracteres tendra la contraseña? ")) 

for i in range (lenght):
    psw += r.choice (elements)

print (f"Hola tu contraseña ha sido generada: {psw}")