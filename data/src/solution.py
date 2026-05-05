import pandas as pd
import networkx as nx

df = pd.read_csv('../data/network_data.csv')
G = nx.DiGraph()

for index, row in df.iterrows():
    G.add_edge(row['Source'], row['Target'], capacity=row['Capacity_Mbps'])

source_node = 'Istanbul_DC'
target_node = 'Anadolu_HQ'

flow_value, flow_dict = nx.maximum_flow(G, source_node, target_node)
print(f"Algorithm executed successfully. Max flow is {flow_value} Mbps.")
