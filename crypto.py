from packages import pyDes as pydes
def encriptar(archivo, passwd):
    f = open(archivo, "rb+")
    d = f.read()
    f.close()
    k = pydes.des(passwd)
    d = k.encrypt(d, ' ')
    f = open(archivo, 'wb+')
    f.write(d)
    f.close()
    return 1
def desencriptar(archivo, passwd):
    f = open(archivo, "rb+")
    d = f.read()
    f.close()
    k = pydes.des(passwd)
    d = k.decrypt(d, ' ')
    f = open(archivo, 'wb+')
    f.write(d)
    f.close()
    return 1
