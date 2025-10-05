import random
import screenfun
def createKeyPair ():
  print("Generating RSA key pair...")
  keys = genKeys()
  print("Keys sucessfully generated!")
  while True:
    print("1. View public key")
    print("2. View private key")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
      print("Public key: ", keys[0])
      input("Press enter to continue...")
      screenfun.clear()
    elif choice == "2":
      print("Private key: ", keys[1])
      input("Press enter to continue...")
      screenfun.clear()
    elif choice == "3":
      break
  
def fastmod2 (numb, expo, mod, expos):
  x=1
  store= numb%mod
  if x in expos:
    ret = [store]
    x+=1
  else:
    x+=1
    ret = []
  while x<expo:  
    store = (store%mod * store%mod)%mod
    if x in expos:
      ret.append(store)
    x*=2
  return ret

def fastmodany(numb, mod, expo):
  binexpo = bin(expo)[2:]
  k=0
  expos = []
  for num in binexpo[::-1]:
    if num=='1':
      expos.append(2**k)
    k+=1

  pow2 = fastmod2(numb, expo, mod, expos)
  result = 1

  for x in pow2:
    result *= x
  return result%mod

def fermat_primality_test(p):
  for x in range(1,20):
    a = random.randint(1,p-2)

    if not(fastmodany(a,p,p-1) == 1):
      return False
  return True
isprime = False


def genPrime():
  print("serching for prime...")
  isprime = False
  while not(isprime):
    prime = random.getrandbits(512)
    isprime = fermat_primality_test(prime)
  return prime


def egcd(a, b):
  x,y, u,v = 0,1, 1,0
  while a != 0:
      q, r = b//a, b%a
      m, n = x-u*q, y-v*q
      b,a, x,y, u,v = a,r, u,v, m,n
  gcd = b
  return gcd, x, y


def genKeys(p=None,q=None):
  if p==None or q==None:
    p = genPrime()
  if q==None:
    q = genPrime()
  n = p*q
  phin = (p-1) * (q-1)
  e = random.randint(2,phin)
  goode = False
  while (not goode):
    e = random.randint(2,phin-1)
    if (egcd(e,phin)[0] == 1):
      goode = True
  pubkey = [e,n]
  d = egcd(phin,e)[2]
  if d < 0:
    d += phin
  privkey = [int(d),n]
  return pubkey, privkey

def encrypt(m,e,n):
  return fastmodany(m,n,e)

def decrpyt(c,d,n):
  return fastmodany(c,n,d)