#Obtener email del user
email = input ("Cual es tu email?: ").strip()

# Cortar el nombre  del user

usuario  =  email[:email.index("@")]

# Contar el dominio 

dominio  =  email[email.index("@")+1:]

#Formatear el mensaje

salida  = "Tu nombre de usuario es {} y tu nombre de dominio es {}".format(usuario, dominio)

print(salida) 