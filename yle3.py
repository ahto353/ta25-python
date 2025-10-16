#Kirjuta programm, mis küsib kasutajalt täisarvu n vahemikus 1-9. Arvu
# ta n + nn + nnn väärtus ja väljasta see. (Näiteks kui kasutaja sisestab 2, siis
#  on vaja väljastada tulemus 2 + 	22 + 222 = 246). Ära kasuta korrutamistehet. Ülesanne
#  on lahendatav ainult liitmise operaatorit kasuades

n = int(input('siste number '))
n = n + n
nn = n + n
nnn = n + n
print(n, '+', nn, '+', nnn, '=',sum)

