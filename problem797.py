class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        path = []

        def dfs(node, temp):
            if node == len(graph) - 1:
                path.append(temp)
            else:
                for adj_node in graph[node]:
                    dfs(adj_node, temp + [adj_node])

        dfs(0, [0])
        return path