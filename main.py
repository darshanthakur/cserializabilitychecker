import matplotlib.pyplot as plt
import networkx as net

class myClass:
 def __init__(self,a,b,c):
  self.op = a;
  self.transaction = b;
  self.var = c;

G = net.DiGraph() 
C = net.DiGraph()

## INPUT PHASE
schedule = []
temp = str(input("Enter the operations\nGuide:\nr: read\nw: write\n1-9:transaction id\nAt last mention the variable on which transaction is working\nExample: r1x w1x r2y\n"))

for x in range(0,len(temp)-1,4):
	schedule.append(myClass(temp[x],temp[x+1],temp[x+2]))

## CONFLICTS IDENTIFICATION
for outer in range(0,len(schedule)-2):
	if schedule[outer].op=="r":
		for inner in range(outer+1,len(schedule)):
			if schedule[inner].op=="w":
				if schedule[outer].var==schedule[inner].var and schedule[outer].transaction!=schedule[inner].transaction:
					G.add_edge(schedule[outer].transaction,schedule[inner].transaction)
					#print(schedule[outer].transaction,"->",schedule[inner].transaction)
					continue
				else:
					continue
			else:
				continue

	elif schedule[outer].op=="w":
		for inner in range(outer+1,len(schedule)):
			if schedule[inner].op=="w" or schedule[inner].op=="r":
				if schedule[outer].var==schedule[inner].var and schedule[outer].transaction!=schedule[inner].transaction:
					G.add_edge(schedule[outer].transaction,schedule[inner].transaction)
					#print(schedule[outer].transaction,"->",schedule[inner].transaction)
					continue
				else:
					continue
			else:
				print("This should never print 1")
		
	else:
		print("This should never print 2")

## DISPLAY OF GRAPH USING networkx and matplotlit.pyplot libraries


lay = net.spring_layout(G)   #Specifies the layout in which graph is to be shown


net.draw_networkx_nodes(G,lay,node_size=500)
net.draw_networkx_edges(G,lay,edgelist=G.edges(), edge_color='black')
net.draw_networkx_labels(G,lay)

cycle =[]

try:
	cycle = net.find_cycle(G,orientation="original")        #Throws an exception if no cycle is found, hence we need to handle it using try
except:
	pass

if not cycle:                                   #If not cycle means if list Cycle is NULL
	print("\n\nGiven schedule is Conflict Serializable\n\n")
else:
	print("\n\nGiven schedule is NOT Conflict Serializable as the precedence graph contains cycle(highlighted in red)\n\n")
	for item in range(0,len(cycle)):
		C.add_edge(cycle[item][0],cycle[item][1])
	net.draw_networkx_nodes(C,lay,node_size=350,node_color='yellow')
	net.draw_networkx_edges(C,lay,edgelist=C.edges(), edge_color='red')
	net.draw_networkx_labels(C,lay)
	
	
plt.show()
