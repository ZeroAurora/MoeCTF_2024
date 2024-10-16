# EzPack

离散对数求出密文然后就是最简单的超递增序列knapsack了

```py
p = 2050446265000552948792079248541986570794560388346670845037360320379574792744856498763181701382659864976718683844252858211123523214530581897113968018397826268834076569364339813627884756499465068203125112750486486807221544715872861263738186430034771887175398652172387692870928081940083735448965507812844169983643977
g=7
s=1210552586072154479867426776758107463169244511186991628141504400199024936339296845132507655589933479768044598418932176690108379140298480790405551573061005655909291462247675584868840035141893556748770266337895571889128422577613223452797329555381197215533551339146807187891070847348454214231505098834813871022509186
Fp = IntegerModRing(p)
g_modp = Fp(g) 
s_modp = Fp(s)
x = discrete_log(s_modp, g_modp)
print(x)
```
```py
from Crypto.Util.number import *
key=
c=363965742933281351259442199216117822475210003294088371760914916341815880641228470807683148775152284520244
answer=[]
for k in key.__reversed__():
    if c>k:
        answer.append('1')
        c-=k
    else:
        answer.append('0')
result=int(''.join(answer)[::-1],2)
print(long_to_bytes(result))
```