### 4

_Show that using a single bit to store each vertex of color suffices..._

My solution is a little bit different. I think we cannot just remove `u.color = GRAY` and leave the rest as it is. 

```
DFS-visit(G, u)
    time = time + 1
    u.d = time
    u.color = GRAY
    for each v \in G.adj[u]:
        if v.color == white
            v.pi = u
            DFS-visit(G, v)
    u.color = BLACK
    time = time + 1
    u.f = time
```

The purpose of line 3 `u.color = GRAY` here is to prevent `u` from being visited again if we are currently vising `u`. `Gray` and `Black` is to differentiate two states of a node: 1) being visited 2) have already finished visiting. But these two states, if our goal is to visit all nodes and not to repeat ourselves, are the same.

Hence, we can replace `u.color = GRAY` by `u.color = BLACK`, and remove `u.color= BLACK`, the result would be the same. 

