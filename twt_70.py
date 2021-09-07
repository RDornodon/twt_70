B='ABCDEFGHIJKLMNOPQRSTUVWXYZ';B+=B.lower()+'0123456789+/=';V=0
for _ in'_'*int(input()):
 for c in(Q:=input()):V=V*64+B.index(c)
 while V:_=chr(V%256)+_;V//=256
 print(_[:~Q.count('=')])

'''7
aGk=
Ynll
bGlnaHQgdw==
bGlnaHQgd4==
bGlnaHQgd28=
bGlnaHQgd2+=
bGlnaHQgd29y
'''