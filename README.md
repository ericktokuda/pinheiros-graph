# Manipulating the streets graph from Pinheiros
Graph from pinheiros

## Pre-run
```pip install -r requirements.txt```

## Running
Simple as:

```jupyter notebook main.ipynb```

## Data
The graph of Pinheiros can be loaded from `data/`. Be G(V, E) such that n(V)=r and n(E)=s
 * `nodes` is a rx2 list of coordinates
 * `edges` is a sx2 list of lists, where each element represent the start node id, the end node id, and a list of intermediary segments

