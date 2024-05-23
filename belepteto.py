adatok =[]
with open("bedat.txt",'r',encoding='utf-8') as file:
    for i in file:
        adatok.append(i.strip().split(' '))

print("2. feladat: ")
print(f"Az első tanuló {adatok[0][1]}-kor lépett be a főkapun. ")
print(f"Az utolsó tanuló {adatok[-1][1]}-kor lépett ki a főkapun. ")

with open('kesok.txt','w') as kesok_file:
    for i in adatok:
        if(i[2] == '1' and i[1] < '08:15' and i[1] > '07:50'):
            print(f"{i[1]} {i[0]}", file= kesok_file)


print("4. feladat: ")

ebedelt = 0
for i in adatok:
    if i[2] == '3':
        ebedelt +=1
print(f"A menzán aznap {ebedelt} tanuló ebédelt.")

print("5. feladat: ")


kolcsonzott_db = 0
kolcsonzott = []
for i in adatok:
    if (i[2] == '4' and i[0] not in kolcsonzott):
        kolcsonzott_db +=1
        kolcsonzott.append(i[0])
print(f"A menzán aznap {kolcsonzott_db} tanuló kölcsönzött.")

if kolcsonzott_db > ebedelt:
    print("Többen voltak, mint a menzán.")
elif kolcsonzott_db < ebedelt:
    print("Nem voltak többen, mint a menzán.")
else:
    print("Ugyanannyian voltak.")

print("6. feladat: ")

beleptek = []
for i in adatok:
    if (i[2] == '1' and i[1] < '10:50' and i not in beleptek):
        beleptek.append(i[0])
    elif (i[2] == '2' and i[1] < '10:50'):
        beleptek.remove(i[0])

    if i[2] == "1" and i[1] > '10:50' and  i[1] < '11:00' and i[0] in beleptek:
        print(i[0], end=' ')

print("\n7. feladat: ")

belepes = ''
kilepes = ''

diak = str(input('Egy tanuló azonosítója='))

for i in adatok:
    if i[0] == diak and i[2] == '1':
        belepes = i[1].split(':')
        break
for i in adatok:
    if i[0] == diak and i[2] == '2':
        kilepes = i[1].split(':')

if (belepes == '' and kilepes == ''):
    print('Ilyen azonosítójú tanuló aznap nem volt az iskolában.')
else:
    ido_percben = ((int(kilepes[0])*60) + int(kilepes[1])) - ((int(belepes[0])*60) + int(belepes[1]))

    orak = round(ido_percben/60)
    percek = ido_percben % 60
    print(f"A tanuló érkezése és távozása között {orak} óra {percek} perc telt el.")

