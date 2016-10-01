f = open('lt2.txt')
al = f.read()
txt = al.split('\n')
b = []
for a in txt:
    c = a.split('\t')
    b.append(c)
#print b

saga = 0
elm = 0
cendana = 0

for a in b:
    elif a[5].find('Saga')>=0:
        saga += int(a[6])
    elif a[5].find('Elm')>=0:
        elm += int(a[6])
    elif a[5].find('Cendana')>=0:
        cendana += int(a[6])
    else:
        print('exception')
        print a
    
print ('saga')
print (saga)
print ('elm')
print elm
print ('cendana')
print cendana

    