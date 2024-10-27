from sage.all import *
from random import getrandbits, randint
from secrets import randbelow
from Crypto.Util.number import getPrime,isPrime,inverse
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from secret import priKey, flag
from hashlib import sha1
import os


q = getPrime(160)
while True:
    t0 = q*getrandbits(864)
    if isPrime(t0+1):
        p = t0 + 1
        break


x = priKey
assert p % q == 1
h = randint(1,p-1)
g = pow(h,(p-1)//q,p)
y = pow(g,x,p)


def sign(z, k):
    r = pow(g,k,p) % q
    s = (inverse(k,q)*(z+r*priKey)) % q
    return (r,s)


def verify(m,s,r):
    z = int.from_bytes(sha1(m).digest(), 'big')
    u1 = (inverse(s,q)*z) % q
    u2 = (inverse(s,q)*r) % q
    r0 = ((pow(g,u1,p)*pow(y,u2,p)) % p) % q
    return r0 == r


def lcg(a, b, q, x):
    while True:
        x = (a * x + b) % q
        yield x


msg = [os.urandom(16) for i in range(5)]

a, b, x = [randbelow(q) for _ in range(3)]
prng = lcg(a, b, q, x)
sigs = []
for m, k in zip(msg,prng):
    z = int.from_bytes(sha1(m).digest(), "big") % q
    r, s = sign(z, k)
    assert verify(m, s, r)
    sigs.append((r,s))


print(f"{g = }")
print(f"{h = }")
print(f"{q = }")
print(f"{p = }")
print(f"{msg = }")
print(f"{sigs = }")
key = sha1(str(priKey).encode()).digest()[:16]
iv = os.urandom(16)
cipher = AES.new(key, AES.MODE_CBC,iv)
ct = cipher.encrypt(pad(flag,16))
print(f"{iv = }")
print(f"{ct = }")


'''
g = 81569684196645348869992756399797937971436996812346070571468655785762437078898141875334855024163673443340626854915520114728947696423441493858938345078236621180324085934092037313264170158390556505922997447268262289413542862021771393535087410035145796654466502374252061871227164352744675750669230756678480403551
h = 13360659280755238232904342818943446234394025788199830559222919690197648501739683227053179022521444870802363019867146013415532648906174842607370958566866152133141600828695657346665923432059572078189013989803088047702130843109809724983853650634669946823993666248096402349533564966478014376877154404963309438891
q = 1303803697251710037027345981217373884089065173721
p = 135386571420682237420633670579115261427110680959831458510661651985522155814624783887385220768310381778722922186771694358185961218902544998325115481951071052630790578356532158887162956411742570802131927372034113509208643043526086803989709252621829703679985669846412125110620244866047891680775125948940542426381
msg = [b'I\xf0\xccy\xd5~\xed\xf8A\xe4\xdf\x91+\xd4_$', b'~\xa0\x9bCB\xef\xc3SY4W\xf9Aa\rO', b'\xe6\x96\xf4\xac\n9\xa7\xc4\xef\x82S\xe9 XpJ', b'3,\xbb\xe2-\xcc\xa1o\xe6\x93+\xe8\xea=\x17\xd1', b'\x8c\x19PHN\xa8\xbc\xfc\xa20r\xe5\x0bMwJ']
sigs = [(913082810060387697659458045074628688804323008021, 601727298768376770098471394299356176250915124698), (406607720394287512952923256499351875907319590223, 946312910102100744958283218486828279657252761118), (1053968308548067185640057861411672512429603583019, 1284314986796793233060997182105901455285337520635), (878633001726272206179866067197006713383715110096, 1117986485818472813081237963762660460310066865326), (144589405182012718667990046652227725217611617110, 1028458755419859011294952635587376476938670485840)]
iv = b'M\xdf\x0e\x7f\xeaj\x17PE\x97\x8e\xee\xaf:\xa0\xc7'
ct = b"\xa8a\xff\xf1[(\x7f\xf9\x93\xeb0J\xc43\x99\xb25:\xf5>\x1c?\xbd\x8a\xcd)i)\xdd\x87l1\xf5L\xc5\xc5'N\x18\x8d\xa5\x9e\x84\xfe\x80\x9dm\xcc"
'''