import networkx as nx
import sys
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

# Function to choose direction of travel

# Function to select all probable paths (opposite colored nodes) in a line

# Add nodes function to build base graph
def buildGraph(num1, num2):
    for i in range(num1):
        for j in range(num2):
            G.add_node(j + (i * num2))
        
# Edge/Node construction function that adds both the node color attribute and edge connections
def addColor(obj, curnode):
    # add color values to nodes
    #print(curnode)
    if obj[0] == 'R':
        G.nodes[curnode]["color"] = "red"
        G.nodes[curnode]["direction"] = str(obj[1])
    if obj[0] == 'B':
        G.nodes[curnode]["color"] = "blue"
        G.nodes[curnode]["direction"] = str(obj[1])
    if obj[0] == 'X':
        G.nodes[curnode]["color"] = "bulls"
        G.nodes[curnode]["direction"] = "bulls"

    
    #print( str(curnode) + " " + obj[0] + " " + G.nodes[curnode]["color"] + " " + G.nodes[curnode]["direction"])

def edgeBuilder(curnode, curcolor, curdir):
    nextnode = curnode

    #print("curnode: " + str(curnode) + " " + G.nodes[curnode]["direction"])

    if curdir == "E":
        # Search all nodes of opposite color for a possible next path
        while ((nextnode + 1) % (int(n2))) != 0:
            nextnode = (nextnode + 1)
            # if opposite color exits take path
            if G.nodes[nextnode]["color"] != curcolor and str(str(curnode) + "-" + str(nextnode)) not in edgelist:

                #print("tempnode: " + str(tempnode) + " " + G.nodes[curnode]["direction"] + " nextnode: " + str(nextnode))

                G.add_edge(curnode, nextnode)

                estr = str(curnode) + "-" + str(nextnode)
                edgelist.append(estr)

                edgeBuilder(nextnode, G.nodes[nextnode]["color"], G.nodes[nextnode]["direction"] )

    if curdir == "W":
        # Search all nodes of opposite color for a possible next path
        while (nextnode % int(n2)) != 0 and nextnode != 0:
            nextnode = (nextnode - 1)
            # If node of opposite color exists try that path
            if G.nodes[nextnode]["color"] != curcolor and str(str(curnode) + "-" + str(nextnode)) not in edgelist:

                #print("tempnode: " + str(tempnode) + " " + G.nodes[curnode]["direction"] + " nextnode: " + str(nextnode))

                G.add_edge(curnode, nextnode)

                estr = str(curnode) + "-" + str(nextnode)
                edgelist.append(estr)

                edgeBuilder(nextnode, G.nodes[nextnode]["color"], G.nodes[nextnode]["direction"] )

    if curdir == "S":
        # Search all nodes of opposite color for a possible next path
        while nextnode < ((int(n1) * int(n2)) - int(n2)):
            nextnode = nextnode + int(n2)
            if G.nodes[nextnode]["color"] != curcolor and str(str(curnode) + "-" + str(nextnode)) not in edgelist:

                #print("tempnode: " + str(tempnode) + " " + G.nodes[curnode]["direction"] + " nextnode: " + str(nextnode))

                G.add_edge(curnode, nextnode)

                estr = str(curnode) + "-" + str(nextnode)
                edgelist.append(estr)

                edgeBuilder(nextnode, G.nodes[nextnode]["color"], G.nodes[nextnode]["direction"] )

    if curdir == "N":
        # Search all nodes of opposite color for a possible next path
        while nextnode > int(n2):
            nextnode = nextnode - int(n2)
            if G.nodes[nextnode]["color"] != curcolor and str(str(curnode) + "-" + str(nextnode)) not in edgelist:

                #print("tempnode: " + str(tempnode) + " " + G.nodes[curnode]["direction"] + " nextnode: " + str(nextnode))

                G.add_edge(curnode, nextnode)

                estr = str(curnode) + "-" + str(nextnode)
                edgelist.append(estr)

                edgeBuilder(nextnode, G.nodes[nextnode]["color"], G.nodes[nextnode]["direction"] )

    if curdir == "SW":
        while nextnode < ((int(n1) * int(n2)) - int(n2)) and (nextnode % int(n2)) != 0 and nextnode != 0:
            nextnode = (nextnode + (int(n2) - 1))
            if G.nodes[nextnode]["color"] != curcolor and str(str(curnode) + "-" + str(nextnode)) not in edgelist:

                #print("tempnode: " + str(tempnode) + " " + G.nodes[curnode]["direction"] + " nextnode: " + str(nextnode))

                G.add_edge(curnode, nextnode)

                estr = str(curnode) + "-" + str(nextnode)
                edgelist.append(estr)

                edgeBuilder(nextnode, G.nodes[nextnode]["color"], G.nodes[nextnode]["direction"] )

    if curdir == "SE":
        # Search all nodes of opposite color for a possible next path
        while nextnode < ((int(n1) * int(n2)) - int(n2)) and ((nextnode + 1 ) % (int(n2))) != 0:
            nextnode = (nextnode + (int(n2) + 1))
            if G.nodes[nextnode]["color"] != curcolor and str(str(curnode) + "-" + str(nextnode)) not in edgelist:

                #print("tempnode: " + str(tempnode) + " " + G.nodes[curnode]["direction"] + " nextnode: " + str(nextnode))

                G.add_edge(curnode, nextnode)

                estr = str(curnode) + "-" + str(nextnode)
                edgelist.append(estr)

                edgeBuilder(nextnode, G.nodes[nextnode]["color"], G.nodes[nextnode]["direction"] )

    if curdir == "NE":
        # Search all nodes of opposite color for a possible next path
        while nextnode > int(n2) and ((nextnode + 1) % (int(n2))) != 0:
            nextnode = (nextnode - (int(n2) - 1))
            if G.nodes[nextnode]["color"] != curcolor and str(str(curnode) + "-" + str(nextnode)) not in edgelist:

                #print("tempnode: " + str(tempnode) + " " + G.nodes[curnode]["direction"] + " nextnode: " + str(nextnode))

                G.add_edge(curnode, nextnode)

                estr = str(curnode) + "-" + str(nextnode)
                edgelist.append(estr)

                edgeBuilder(nextnode, G.nodes[nextnode]["color"], G.nodes[nextnode]["direction"] )

    if curdir == "NW":
        # Search all nodes of opposite color for a possible next path
        while nextnode > int(n2) and (nextnode % int(n2) - 1) != 0:
            nextnode = (nextnode - (int(n2) + 1))
            if G.nodes[nextnode]["color"] != curcolor and str(str(curnode) + "-" + str(nextnode)) not in edgelist:

                #print("tempnode: " + str(tempnode) + " " + G.nodes[curnode]["direction"] + " nextnode: " + str(nextnode))

                G.add_edge(curnode, nextnode)

                estr = str(curnode) + "-" + str(nextnode)
                edgelist.append(estr)

                edgeBuilder(nextnode, G.nodes[nextnode]["color"], G.nodes[nextnode]["direction"] )


    #print(G.edges())


#---------------------------- MAIN CODE ----------------------------
sys.setrecursionlimit(1500)
infile, outfile = sys.argv[1], sys.argv[2]

f = open(infile, 'r')

G = nx.DiGraph()

nodes = f.readline().strip().split(" ")
n1 = nodes[0]
n2 = nodes[1]
curnode = 0
edgelist = []

buildGraph(int(n1), int(n2))

# Build the base graph of edges and colored nodes.
for i in f.readlines():
    thing = i.strip().split(" ")
    for j in range(int(n2)):
        if thing[j] == 'O':
            thing2 = "X"
            addColor(thing2, curnode)
            #print(thing2)
        else:
            thing2 = thing[j].split('-')
            addColor(thing2, curnode)
            curnode += 1
            #print(thing2[0] + " " + thing2[1])

f.close()

# Now it's time to transverse the graph starting at the upper left node
curnode = 0
curcolor = G.nodes[curnode]["color"]
curdir = G.nodes[curnode]["direction"]

edgeBuilder(curnode, curcolor, curdir)
paths = nx.all_simple_paths(G, source=0, target=(int(n1) * int(n2) - 1))

#print(list(paths))

finalstr = ""

flag = 0
prev = 0
for path in paths:  
    for node in path:
        #print(str(node) + " " + G.nodes[node]["direction"])
        #print(G.nodes[node]["direction"])

        if node != 0:
            if printhelper == "S":
                temp = int((node - prev) / int(n2))
                #print(str(temp) + printhelper)
                finalstr += (str(temp) + printhelper + " ")

            if printhelper == "N":
                temp = int((prev - node) / int(n2))
                #print(str(temp) + printhelper)
                finalstr += (str(temp) + printhelper + " ")

            if printhelper == "E":
                temp = int(node - prev)
                #print(str(temp) + printhelper)
                finalstr += (str(temp) + printhelper + " ")

            if printhelper == "W":
                temp = int(prev - node)
                    #print(str(temp) + printhelper)
                finalstr += (str(temp) + printhelper + " ")

            if printhelper == "NW":
                temp = int((prev - node) / (int(n2) + 1))
                #print(str(temp) + printhelper)
                finalstr += (str(temp) + printhelper + " ")
            
            if printhelper == "NE":
                temp = int((prev - node) / (int(n2) - 1))
                #print(str(temp) + printhelper)
                finalstr += (str(temp) + printhelper + " ")

            if printhelper == "SW":
                temp = int((node - prev) / (int(n2) - 1))
                #print(str(temp) + printhelper)
                finalstr += (str(temp) + printhelper + " ")

            if printhelper == "SE":
                temp = int( (node - prev) / (int(n2) + 1))
                #print(str(temp) + printhelper)
                finalstr += (str(temp) + printhelper + " ")

        printhelper = G.nodes[node]["direction"]
        prev = node
    print(finalstr)

    o = open(outfile, 'w')
    o.write(finalstr)
    o.close()


    break