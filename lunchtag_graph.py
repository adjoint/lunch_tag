import networkx as nx
import matplotlib.pyplot as plt
import csv

lst = [] 
people = []
peoplecount = 0
activepeoplecount = 0
mealcount = 0
saga = []
elm = []
cend = []
with open('meals.txt', 'rb') as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        lst.append(row)     
with open('people.txt', 'rb') as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        peoplecount += 1
        people.append([row[2] + " " + row[3], row[5]])
        if row[6]!="0":
            activepeoplecount += 1
slist = []
elist = []
clist = []
values = []
        
for person in people:
    if (person[1].find('Saga') != -1):
        saga.append(person[0])
        slist.append('b')
    elif (person[1].find('Elm') != -1):
        elm.append(person[0])
        elist.append('r')
    elif (person[1].find('Cendana') != -1):
        cend.append(person[0])
        clist.append('g')
    else:
        print person
      
G=nx.Graph()
G.add_nodes_from(saga)
G.add_nodes_from(elm)
G.add_nodes_from(cend)

for a in lst:
    if a[0]!='Cancel':
        G.add_edge(a[2], a[4])
        #print a[2] + " " + a[4]
        mealcount += 1

values = slist + elist + clist
print "meals " + str(mealcount)
print "participants " + str(peoplecount)
print "active participants " + str(activepeoplecount)
nx.draw_circular(G, node_color=values, alpha=0.5)
plt.savefig("network.png") # save as png
plt.show() # display