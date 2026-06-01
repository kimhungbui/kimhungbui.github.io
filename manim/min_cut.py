import networkx as nx
import matplotlib.pyplot as plt

def visualize_flow_cut_theorem():
    # 1. Define the Network N = (G, c, s, t)
    G = nx.DiGraph()
    edges = [
        ('s', 'v1', {'cap': 11, 'flow': 6}),
        ('s', 'v2', {'cap': 6, 'flow': 0}),
        ('v1', 'v3', {'cap': 3, 'flow': 3}),
        ('v1', 'v4', {'cap': 4, 'flow': 3}),
        ('v2', 'v1', {'cap': 2, 'flow': 0}),
        ('v2', 'v3', {'cap': 2, 'flow': 0}),
        ('v2', 'v5', {'cap': 1, 'flow': 0}),
        ('v3', 't', {'cap': 7, 'flow': 2}),
        ('v4', 'v3', {'cap': 3, 'flow': 0}),
        ('v4', 't', {'cap': 6, 'flow': 4}),
        ('v5', 'v4', {'cap': 3, 'flow': 0}),
        ('v5', 't', {'cap': 2, 'flow': 2}),
    ]
    G.add_edges_from(edges)
    
    # 2. Define a Cut (S, S_bar)
    # Based on the text: s must be in S, t must be in S_bar
    S = {'s', 'v1', 'v2'}
    nodes = set(G.nodes())
    S_bar = nodes - S
    
    # 3. Calculate Theorem Values
    # val(f) = net flow out of source s
    val_f = sum(G['s'][v]['flow'] for v in G.neighbors('s'))
    
    # f(S, S_bar) = flow(S->S_bar) - flow(S_bar->S)
    flow_out = 0
    flow_in = 0
    cap_out = 0
    
    crossing_out = []
    crossing_in = []
    
    for u, v, data in G.edges(data=True):
        if u in S and v in S_bar:
            flow_out += data['flow']
            cap_out += data['cap'] # c(S, S_bar)
            crossing_out.append((u, v))
        elif u in S_bar and v in S:
            flow_in += data['flow']
            crossing_in.append((u, v))
            
    net_flow_S = flow_out - flow_in
    
    # 4. Visualization
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 7))
    
    # Draw nodes: S in light blue, S_bar in light red
    nx.draw_networkx_nodes(G, pos, nodelist=list(S), node_color='lightblue', node_size=800, label='Set S')
    nx.draw_networkx_nodes(G, pos, nodelist=list(S_bar), node_color='salmon', node_size=800, label='Set S_bar')
    
    # Draw edges: highlighting those crossing the cut
    nx.draw_networkx_edges(G, pos, edgelist=list(G.edges() - set(crossing_out) - set(crossing_in)), 
                           edge_color='gray', alpha=0.3)
    nx.draw_networkx_edges(G, pos, edgelist=crossing_out, edge_color='blue', width=2, label='S -> S_bar (Capacity)')
    nx.draw_networkx_edges(G, pos, edgelist=crossing_in, edge_color='red', width=2, label='S_bar -> S (Negative Flow)')
    
    # Labels
    nx.draw_networkx_labels(G, pos)
    edge_labels = {(u, v): f"{d['flow']}/{d['cap']}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.title(f"Visualization of Lemma 2.2\nval(f)={val_f} | f(S, S_bar)={net_flow_S} | c(S, S_bar)={cap_out}")
    plt.legend(scatterpoints=1)
    plt.axis('off')
    
    # Verify theorem in console
    print(f"--- Theorem Verification ---")
    print(f"1. val(f) = {val_f}")
    print(f"2. f(S, S_bar) = {flow_out} (out) - {flow_in} (in) = {net_flow_S}")
    print(f"3. c(S, S_bar) = {cap_out}")
    print(f"Result: {val_f} = {net_flow_S} <= {cap_out} is {val_f == net_flow_S <= cap_out}")
    
    plt.show()

if __name__ == "__main__":
    visualize_flow_cut_theorem()