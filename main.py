from data.models import GRAPH, GRAPH_TEST, Stack
from collections import deque


class GRAPH_ALGS:

    # Depth-First Search
    @staticmethod
    def dfs(model, start_edge):
        current_edges_dfs = Stack([start_edge])
        visited_dfs = [start_edge]

        while current_edges_dfs.size():
            node = current_edges_dfs.pop()
            if node not in visited_dfs:
                visited_dfs.append(node)
            
            for ngh in model[node]:
                if ngh not in visited_dfs:
                    current_edges_dfs.push(ngh)
        return {
            "visited": visited_dfs,
            "result": len(visited_dfs) == len(model.keys())
        }

    # Breadth-First Search
    @staticmethod
    def bfs(model, start_edge):
        current_edges_bfs = deque(model[start_edge])
        visited_bfs = [start_edge]

        while len(current_edges_bfs):
            node = current_edges_bfs.popleft()
            print(node)
            if node not in visited_bfs:
                visited_bfs.append(node)

            for ngh in model[node]:
                if ngh not in visited_bfs:
                    current_edges_bfs.append(ngh)

        return {
            "visited": visited_bfs,
            "result": len(visited_bfs) == len(model.keys())
        }

    @staticmethod
    def top_sort(model, start_edge):
        visited = []
        stack = Stack()

        def dfs(node):
            visited.append(node)

            for ngh in model[node]:
                if ngh not in visited:
                    dfs(ngh)

            stack.push(node)

        dfs(start_edge)



print(GRAPH_ALGS.bfs(GRAPH_TEST, "A"))
print(GRAPH_ALGS.dfs(GRAPH_TEST, "A"))
print(GRAPH_ALGS.top_sort(GRAPH_TEST, "A"))