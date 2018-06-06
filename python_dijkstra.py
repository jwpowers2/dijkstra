# dijkstra basics in python
# from 'grokking algorithms by Aditya Bhargava

def find_lowest_cost_node(costs):

    lowest_cost = float("inf")
    lowest_cost_node = None

    # go through each node
    for node in costs:

        cost = costs[node]

        # if its the lowest cost so far and hasn't been processed yet
        if cost < lowest_cost and node not in processed:

            # set it as the new lowest cost node
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
processed = []

# find the lowest cost node that you haven't processed yet
node = find_lowest_cost_node(costs)

# end loop when all nodes are processed
while node is not None:

    cost = costs[node]
    neighbors = graph[node]
    
    # go through all the neighbors of this node
    for n in neighbors.keys():

        new_cost = cost + neighbors[n]

        # if this route is cheaper, use it
        if costs[n] > new_cost: 

            # update cost for this node
            costs[n] = new_cost
            # this node becomes the new parent for this neighbor
            parents[n] = node

    # mark the node as processed
    processed.append(node)
    # find the next node to process, and loop
    node = find_lowest_cost_node(costs)

print costs
