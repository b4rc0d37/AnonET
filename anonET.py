import os

def tor():
    print("El navegador debe configurarse manualmente ingresando el puerto 9050.")
    os.system("apt-get install tor && service tor start")
    os.system("clear")
    return main()

def proxychains():
    os.system("apt-get install proxychains")
    arquivo = open('/etc/proxychains.conf', 'r')
    conteudo = arquivo.readlines()

    conteudo.append('socks5 127.0.0.1 9050')
   
    arquivo = open('/etc/privoxy/config', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()
    print("En /etc/privoxy/config, elija la opcion de conexion que desea usar")
    os.system("clear")
    return main()

def prixoxy():
    print("El navegador debe configurarse manualmente ingresando el puerto 8118")
    os.system("apt-get install privoxy")
    arquivo = open('/etc/privoxy/config', 'r')
    conteudo = arquivo.readlines()

    conteudo.append('forward-socks5 / localhost:9050 . \n')
    conteudo.append('forward-socks4 / localhost:9050 . \n')
    conteudo.append('forward-socks4a / localhost:9050 .')

    arquivo = open('/etc/privoxy/config', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()
    os.system("service privoxy start")
    os.system("clear")
    return main()

def jondo():
    os.system("wget https://jondobrowser.jondos.de/releases/current/jondobrowser-linux64_en-US.tar.xz")
    os.system("apt-get install default-jre java-wrappers firefox")
    os.system("dpkg -i jondo_all.deb")
    os.system("dpkg -i jondofox-en_all.deb")
    os.system("clear")
    return main()

def torBrowser():
    os.system("wget https://www.torproject.org/dist/torbrowser/8.5.3/tor-browser-linux64-8.5.3_en-US.tar.xz")
    os.system("clear")
    return main()

logo = '''


--------------By:B4rc0d37--------------
    _                      _____ _____ 
   / \   _ __   ___  _ __ | ____|_   _|
  / _ \ | '_ \ / _ \| '_ \|  _|   | |  
 / ___ \| | | | (_) | | | | |___  | |  
/_/   \_\_| |_|\___/|_| |_|_____| |_|  


Canal Youtube: https://www.youtube.com/c/b4rc0d37/videos

Instagram: https://www.instagram.com/giines.zl/?hl=es

----------------------------------------


'''
	
def main():
        print('\033[31m'+ logo +'\033[0;0m')
	menu = '''
(1) Instalar Tor
(2) Instalar Proxychains
(3) Instalar Privoxy
(4) JonDo 64x
(5) Tor Browser	
	'''
	print('\033[33m' + menu + '\033[0;0m')	

	ent = raw_input("Ingrese el Numero deseado: ")

	if(ent == "1"):
	    tor()


	elif(ent == "2"):
	    proxychains()
	elif(ent == "3"):
	    prixoxy()
	elif(ent == "4"):
	    print("Jondo no funciona como usuario root")
	    jondo()
	elif(ent == "5"):
	    torBrowser()
	else:
	    exit()
main()
