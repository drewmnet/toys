from loadbalancer import LoadBalancer
from node import Node

lb = LoadBalancer()
node1 = Node(lb)
node2 = Node(lb)
#node3 = Node(lb)

print(lb.nodes)
