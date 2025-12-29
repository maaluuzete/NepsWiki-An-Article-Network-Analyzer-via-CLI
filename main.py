import json,os
from graph import Graph

F="data.json"

def load():
    if not os.path.exists(F):return Graph()
    try:
        with open(F,"r",encoding="utf-8") as f:
            s=f.read().strip()
            if not s:return Graph()
            return Graph.from_dict(json.loads(s))
    except:return Graph()

def save(g):
    with open(F,"w",encoding="utf-8") as f:
        json.dump(g.to_dict(),f,ensure_ascii=False,indent=2)

def menu():
    print("\nBem-vindo ao NepsWiki!\n")
    print("1. Adicionar Artigo")
    print("2. Vincular Artigos")
    print("3. Encontrar Caminho de Recomendação")
    print("4. Mostrar Grupo de Artigos Relacionados")
    print("5. Mostrar Artigo Mais Citado")
    print("6. Sair\n")
    print("Digite sua escolha:",end=" ")
    
def main():
    g=load()
    while True:
        menu()
        op=input().strip()
        if op=="1":
            print("OK"if g.add_article(input().strip())else"EXISTS")
        elif op=="2":
            print("OK"if g.add_link(input().strip(),input().strip())else"ERR")
        elif op=="3":
            p=g.shortest_path(input().strip(),input().strip())
            print("->".join(p)if p else"NO PATH")
        elif op=="4":
            r=g.connected_group(input().strip())
            print("\n".join(r)if r else"NOT FOUND")
        elif op=="5":
            r=g.most_cited_article()
            print("\n".join(r)if r else"EMPTY")
        elif op=="6":
            save(g);break
        else:
            print("INVALID")

if __name__=="__main__":
    main()
