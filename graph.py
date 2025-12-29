from collections import deque,defaultdict

class Graph:
    def __init__(self):
        self.g=defaultdict(list)

    def add_article(self,a):
        if a in self.g:return False
        self.g[a]=[]
        return True

    def add_link(self,u,v):
        if u not in self.g or v not in self.g:return False
        if v not in self.g[u]:self.g[u].append(v)
        return True

    def shortest_path(self,s,t):
        if s not in self.g or t not in self.g:return None
        q=deque([(s,[s])]);vis={s}
        while q:
            u,p=q.popleft()
            if u==t:return p
            for v in self.g[u]:
                if v not in vis:
                    vis.add(v)
                    q.append((v,p+[v]))
        return None

    def connected_group(self,s):
        if s not in self.g:return []
        st=[s];vis=set()
        while st:
            u=st.pop()
            if u not in vis:
                vis.add(u)
                st+=self.g[u]
        return list(vis)

    def most_cited_article(self):
        indeg=defaultdict(int)
        for u in self.g:indeg[u]=0
        for u in self.g:
            for v in self.g[u]:indeg[v]+=1
        if not indeg:return []
        m=max(indeg.values())
        return [u for u in indeg if indeg[u]==m]

    def to_dict(self):
        return dict(self.g)

    @staticmethod
    def from_dict(d):
        gr=Graph()
        for k,v in d.items():gr.g[k]=v
        return gr
