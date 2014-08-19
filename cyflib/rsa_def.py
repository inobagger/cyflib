#Extraido de http://pastebin.com/ziaUdaw8
import random
import sys
import hashlib
import base64
def modular_exp(b, e, m): #Exponenciacion modular
    r = 1
    while e > 0:
        if e & 1:
            r = (r * b) % m
        e >>= 1
        b = (b ** 2) % m
    return r
def lista_primos(t): #Genera t numeros primos
    l = [2]
    i = 3
    while i < t:
        primo = 1
        for c in l:
            if i % c == 0:
                primo = 0
                break
        if primo:
            l.append(i)
        i += 2
    return l
primelist = lista_primos(5000)
def firstcheck(n):
    for p in primelist:
        if n%p==0:
            if n==p:
                return 1
            else:
                return 0
    return 1
def fermat(n,k=100):
    for i in range(0, k):
        a = random.randint(1,n-1)
        if modular_exp(a,n-1,n) !=1:
            return 0
    return 1
def binary(n):
    l = []
    while (n > 0):
        l.append(n % 2)
        n /= 2
    return l
    
def miller_rabin(a, n): #1 = Complex, 0 = Primo
    b = binary(n - 1)
    d = 1
    for i in xrange(len(b) - 1, -1, -1):
        x = d
        d = (d**2) % n
        if d == 1 and x != 1 and x != n -1:
            return 1
        if b[i] == 1:
            d = (d*a) % n
    if d != 1:
        return 1
    return 0
def check_prime(n, k=100):
    if (not firstcheck(n)):
        return 0
    if (not fermat(n,k)):
        return 0
    for iteration in range(0,k):
        i = random.randint(1, n-1)
        if miller_rabin(i, n):
            return 0
    return 1
def modular_mi_extended(a, b):
    x, last_x = 0, 1
    y, last_y = 1, 0
    while b:
        q = a // b
        a, b = b, a % b
        x, last_x = last_x - q*x, x
        y, last_y = last_y - q*y, y
    return (last_x, last_y, a)
def modular_mi(a, m):
    x, q, gcd = modular_mi_extended(a, m)
    if gcd == 1:
        return (x + m) % m
    else:
        return None
def generar_primo(bitn=512, k=100):
    primo = random.randint(2**(bitn-1), 2**bitn)
    primo |= 1
    while not check_prime(primo, k):
        primo += 2
    return primo
try:
    import psyco #Acelera el programa
    psyco.full()
except ImportError:
    pass
def generar_claves(bitn=512):
    e=65537 #Numero 4 de Fermat, 2**(2**4)+1
    p = generar_primo(bitn)
    q = generar_primo(bitn)
    n = p * q #DECLARACION DE LA CLAVE PUBLICA
    phi = (p - 1) * (q - 1)
    while (phi%e) == 0:
        e = generar_primo(17)
    d = modular_mi(e, phi) #DECLARACION DE LA CLAVE PRIVADA
    public = n
    private = d
    return base64.b64encode(str(public)), base64.b64encode(str(private))
def str_to_int(s):
    n = 0
    for c in s:
        n <<= 8
        n += ord(c)
    return n
def int_to_str(n):
    s = []
    while n > 0:
        s.insert(0, chr(n & 255))
        n >>= 8
    return ''.join(s)
def encriptar(s, public):
    public = int(base64.b64decode(public))
    n = str_to_int(s)
    c = modular_exp(n, 65537, public)
    return base64.b64encode(str(c))
def desencriptar(n, private, public):
    n = int(base64.b64decode(n))
    public = int(base64.b64decode(public))
    private = int(base64.b64decode(private))
    p = modular_exp(n, private, public)
    s = int_to_str(p)
    return s
def sign(msg, private, public):
    private = int(base64.b64decode(private))
    public = int(base64.b64decode(public))
    s = int(hashlib.sha1(msg).hexdigest(), 16)
    return base64.b64encode(str(modular_exp(s, private, public)))
def checksign(msg, sign, pub):
    sign = int(base64.b64decode(sign))
    pub = int(base64.b64decode(pub))
    s = modular_exp(sign,65537,pub)
    h = int(hashlib.sha1(msg).hexdigest(), 16)
    return s == h