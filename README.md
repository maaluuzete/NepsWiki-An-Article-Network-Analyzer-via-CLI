# NepsWiki

*(Based on the exercise [Graph Traversal Visualizer in Python](https://neps.academy/br/course/algoritmos-em-grafos/lesson/visualizador-de-travessia-de-grafos-em-python) from [Neps Academy](https://neps.academy))*

## About the Project
**NepsWiki** is a **learning project** developed in **Python** to practice fundamental concepts of **graph algorithms** and **data structures**. The application simulates a network of interconnected articles using a **directed graph**, where each article is represented as a node and each citation is represented as a directed edge.  
This project was created **for learning purposes only**, following the structure and ideas proposed in the referenced Neps Academy exercise.

---

## Purpose
This project was created as a **learning exercise** to practice basic **graph concepts** in Python, including graph traversal, connectivity, and simple data persistence.

---

## Features
- Add and link articles using a directed graph;  
- Find the shortest path between articles;  
- Display related articles through graph traversal;  
- Identify the most cited article;  
- Save and load data using a JSON file.  

---
## Command-Line Interface

The application runs in a continuous loop and displays the following menu:
```
Bem-vindo ao NepsWiki!

1. Adicionar Artigo
2. Vincular Artigos
3. Encontrar Caminho de Recomendação
4. Mostrar Grupo de Artigos Relacionados
5. Mostrar Artigo Mais Citado
6. Sair

Digite sua escolha:
```

---
## How to Run

```bash
git clone https://github.com/your-username/nepswiki.git](https://github.com/maaluuzete/NepsWiki-An-Article-Network-Analyzer-via-CLI.git
cd NepsWiki-An-Article-Network-Analyzer-via-CLI
python -m venv venv
python main.py
```
## Project Structure
```
nepswiki/
│── main.py      # CLI and application logic
│── graph.py     # Graph structure and algorithms
│── data.json    # Persistent graph storage (auto-generated)
│── README.md
```
## Educational Disclaimer
This project was developed exclusively for learning purposes and is not intended for production use.
