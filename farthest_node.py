import copy
def search_ptr(edges2, count, location):
    global max_count, edges

    goto = []
    print(location)
    for i, edge in enumerate(edges):
        if location == edge[0]:
            if edge in edges2:
                goto.append(edge[1])
                edges2.remove(edge)
        elif location == edge[1]:
            if edge in edges2:
                goto.append(edge[0])
                edges2.remove(edge)
    print(edges2)
    if goto:
       for i in goto:
           search_ptr(edges2, count+1, i)
    else:
        print(count)
        max_count = max(max_count, count)
n = 10
edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]
max_counts = []
for i in range(1, n+1):
    edges2 = copy.copy(edges)
    max_count = 0
    search_ptr(edges2, 0, i)
    max_counts.append(max_count)

print(min(max_counts))