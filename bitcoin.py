from packages import ecdsa as ecdsa
import binascii, hashlib, random, urllib2, sys, md5, math, base64
secp256k1curve=ecdsa.ellipticcurve.CurveFp(115792089237316195423570985008687907853269984665640564039457584007908834671663,0,7)
secp256k1point=ecdsa.ellipticcurve.Point(secp256k1curve,0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141)
secp256k1=ecdsa.curves.Curve('secp256k1',secp256k1curve,secp256k1point,(1,3,132,0,10))
class BitCoin:
  def addy(self, pk):
   pko=ecdsa.SigningKey.from_secret_exponent(pk,secp256k1)
   pubkey=binascii.hexlify(pko.get_verifying_key().to_string())
   pubkey2=hashlib.sha256(binascii.unhexlify('04'+pubkey)).hexdigest()
   pubkey3=hashlib.new('ripemd160',binascii.unhexlify(pubkey2)).hexdigest()
   pubkey4=hashlib.sha256(binascii.unhexlify('00'+pubkey3)).hexdigest()
   pubkey5=hashlib.sha256(binascii.unhexlify(pubkey4)).hexdigest()
   pubkey6=pubkey3+pubkey5[:8]
   pubnum=int(pubkey6,16)
   pubnumlist=[]
   while pubnum!=0: pubnumlist.append(pubnum%58); pubnum/=58
   address=''
   for l in ['123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'[x] for x in pubnumlist]:
    address=l+address
   return '1'+address

  def GetAddress(self, seed):
    return str(self.addy(int(hashlib.sha256(seed).hexdigest(),16)))
  def GetPrivKey(self, seed):
    return str(hashlib.sha256(seed).hexdigest())  
  def TransformBTC(self, balanceprocesar):
    length = len(str(balanceprocesar))
    if length >= 9:
      btc = str(balanceprocesar)[:-8]
      decimal = str(balanceprocesar)[-8:]
      cantidad = btc + "." + decimal + " BTC"
      return cantidad
    else:
      nrceros = 8-length
      temp = str(balanceprocesar)
      a = 0
      while a!=nrceros:
        temp = "0" + temp
        a = a + 1
      cantidad = "0." + temp + " BTC"
      return cantidad
      
  def CheckBalance(self, address):
    try:
      f = urllib2.urlopen("http://blockchain.info/address/"+address+"?format=json")
      af = f.read()
      f.close()
    except:
      return 0
    patrones = af.split(",")
    a = 0
    while a<10:
      patron = patrones[a]
      if "final_balance" in patron:
        b1 = patron.split(":")
        balance = b1[1]
        break
      a = a +1
    balance = int(balance)
    if balance > 0:
      return balance
    else:
      return 0
  def AddressByPrivateKey(self, privkey):
    return str(self.addy(int(privkey,16)))
  def RandomSeed(self):
    patron = md5.new()
    math.fi = (1+math.sqrt(5))/2
    math.random = int(math.fi ** random.randint(1, 100))
    math.random = int(math.sqrt(math.random)+(random.randint(10,99)**8))
    math.random = (random.random()*(10**random.randint(1,5)))*math.random
    math.random = math.random - math.sqrt(math.random)
    math.random = math.random * (math.random/2) - (math.random/3)
    patron.update(str(int(math.random)))
    patron_2 = patron.hexdigest()
    op = random.randint(0,4)
    integer = random.randint(5,25)
    patron_3 = ""
    if op==0:
      patron_3 = patron_2[:integer]
    elif op==1:
      patron_3 = patron_2[integer:]
    elif op==2:
      patron_3 = patron_2[:-integer]
    elif op==4:
      patron_3 = patron_2[-integer:]
    patron_4 = hashlib.sha224(patron_3 + str(random.randint(0,10000000)) ).hexdigest()
    patron_5 = base64.b64encode(patron_4)
    patron.update(patron_5 + patron_4 + patron_3 + str(random.randint(0,10000000)))
    patron_6 = patron.hexdigest()
    patron_7 = base64.b64encode(patron_6 + str(math.random + random.randint(1,99999)))
    return hashlib.sha224(patron_7).hexdigest()
