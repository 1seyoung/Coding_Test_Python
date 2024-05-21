def dfs(graph, v, visited):

    #방문처리
    graph[v]=True
    print(v,end=' ')

    #연결노드 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,viited)
