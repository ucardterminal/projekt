import pandas as pd
import pickle
with open("ncbitree.pickle", 'rb') as f:  #takes 3 seconds to load
    loadedtree = pickle.load(f)

leafs = loadedtree.leaves 
print(type(leafs))

leafs_list = [] 

# for leaf in leafs: #buts all leafes in a list 
#     leafs_list.append(leaf.name)
# print(leafs_list)

nodes_with_children = [node for node in loadedtree.descendants if not node.is_leaf]


actual_leafes = []
for node in nodes_with_children:
    #print(node.name)
    actual_leafes.append(node.name)




# Example list
data = [['Alice', 25, 'Engineer'], ['Bob', 30, 'Doctor']]

# Create DataFrame from list
df = pd.DataFrame(actual_leafes, columns=['Leafes_ids'])

print(df)

# Save DataFrame to TSV file
df.to_csv('actual_leaves.tsv', sep='\t', index=False, header=True)
