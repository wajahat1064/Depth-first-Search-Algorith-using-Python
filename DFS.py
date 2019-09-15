def dfs(begin, goal, jug1capacity, jug2capacity):
queue = []
front = []
front.append(begin)
# forming a one-element queue consisting of zero-length queue that contains only the root node
explored = []
explored.append(begin)
while(front):
present= front.pop()
x = present[0] # presentvalue of the first jug
y = present[1] # presentvalue of the second jug
queue.append(present)
if x == goal or y == goal:
print ("Found!")
# until the first queue in the queue terminates at the goal node or the queue is empty
return queue
# rule 1
if present[0] < jug1capacity and ([jug1capacity, present[1]] not in explored):
# remove the first queue from the queue (not in explored)
# create new queues by extending the first queue to all the neighbors of the terminal node
front.append([jug1capacity, present[1]])
explored.append([jug1capacity, present[1]])

# rule 2
if present[1] < jug2capacity and ([present[0], jug2capacity] not in explored):
front.append([present[0], jug2capacity])
explored.append([present[0], jug2capacity])

# rule 3
if present[1] > 0 and ([min(x + y, jug1capacity), max(0, x + y - jug1capacity)] not in explored):
diff1 = int(min(present[1], jug1capacity - present[0]))
front.append([present[0] + diff1, present[1] - diff1])
explored.append([present[0] + diff1, present[1] - diff1])


# rule 4
if present[0] > 0 and present[1] < jug1capacity and ([max(0, x + y - jug2capacity), min(x + y, jug2capacity)] not in explored):
diff2 = int(min(present[0], jug2capacity - present[1]))
front.append([present[0]-diff2, present[1]+diff2])
explored.append([present[0]-diff2, present[1]+diff2])

#rule 5
if present[0]>0 and ([0,present[1]] not in explored):
front.append([0,present[1]])
explored.append([0,present[1]])

#rule 6
if present[1]>0 and ([present[0],0] not in explored):
front.append([present[0],0])
explored.append([present[0],0])

return "No path found for this combination"

def gcd(a, b):
if a == 0:
return b
return gcd(b%a , a)

jug1capacity = int(input(" Please enter Jug 1 capacity:"))
jug2capacity = int(input("Enter Jug 2 capacity:"))
goal = int(input("Enter target volume:"))
begin = [0, 0]
# condition for getting a solution:
# the target volume 'goal' should be a multiple of gcd(a,b)
if goal % gcd(jug1capacity,jug2capacity) == 0:
print( dfs(begin, goal , jug1capacity, jug2capacity))
else:
print ("No solution possible")
