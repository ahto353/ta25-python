#Kirjuta programm, mis küsib kasutajalt täisarvu n vahemikus 1-9. Arvu
# ta n + nn + nnn väärtus ja väljasta see. (Näiteks kui kasutaja sisestab 2, siis
#  on vaja väljastada tulemus 2 + 	22 + 222 = 246). Ära kasuta korrutamistehet. Ülesanne
#  on lahendatav ainult liitmise operaatorit kasuades

n = int(input('siste number '))
n = n + n
nn = n + n
nnn = n + n
print(n, '+', nn, '+', nnn, '=',sum)
n = int(input(" 2 " )"))
n1 = 2
n2 = 22
n3 = 222
print( n + nn + nnn, "=" ,sum" )
n = input("Sisesta täisarv vahemikus 1-9: ")

# moodustame nn ja nnn liitmise asemel stringide abil
n1 = int(n)
n2 = int(n + n)      # '2' + '2' -> '22'
n3 = int(n + n + n)  # '2' + '2' + '2' -> '222'

tulemus = n1 + n2 + n3

print(f"{n1} + {n2} + {n3} = {tulemus}")