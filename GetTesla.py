# Calvin Todd
# CS 325
# 5.29.21
# Portfolio Project: Get Tesla

def getTesla(M):
    """
    This method takes a 2d array and we return the minimum hit points one would need to get from the starting point to
    the finishing point.
    """
    score_array = [[None for i in range(len(M[j]))] for j in range(len(M))]
    lowest_hp = M[0][0]
    running_total = M[0][0]
    neighbors = []
    visited = []

    m = len(M) - 1
    n = len(M[m]) - 1


    last_vertex = (n, m)
    current_vertex = (0, 0)
    score_array[current_vertex[1]][0] = running_total
    visited.append(current_vertex)

    while last_vertex not in neighbors:
        if current_vertex[0] + 1 <= n:
            neighbors.append((current_vertex[0]+1, current_vertex[1]))
            score_array[current_vertex[1]][current_vertex[0]+1] = running_total + M[current_vertex[1]][current_vertex[0]+1]
        if current_vertex[1] + 1 <= m:
            neighbors.append((current_vertex[0], current_vertex[1]+1))
            score_array[current_vertex[1]+1][current_vertex[0]] = running_total + M[current_vertex[1]+1][
                current_vertex[0]]

        next = None
        for vertex in neighbors:
            if next is None:
                next = vertex
            if score_array[vertex[1]][vertex[0]] > score_array[next[1]][next[0]] and vertex not in visited:
                next = vertex

        neighbors.remove(next)
        visited.append(next)

        if score_array[next[1]][next[0]] < lowest_hp:
            lowest_hp = score_array[next[1]][next[0]]

        current_vertex = next
        running_total = score_array[current_vertex[1]][current_vertex[0]]

    running_total = score_array[m][n]
    if running_total < lowest_hp:
        lowest_hp = running_total

    if lowest_hp > 0:
        return 1
    else:
        return abs(lowest_hp) + 1


M = [[-2, 10, -5, -8], [6, -3, 2, 1], [-11, 14, 8, 0], [3, 20, 6, -3]]
print(getTesla(M))
