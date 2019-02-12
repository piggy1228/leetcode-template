    def dfs(self,G,node,visited,visiting):
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        visited.add(node)
        for nextnode in G[node]:
            if self.dfs(G,nextnode, visited, visiting):
                return True
        visiting.remove(node)
        return False