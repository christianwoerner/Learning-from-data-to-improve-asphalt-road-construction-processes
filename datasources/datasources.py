# %%
import plotly.graph_objects as go
import pandas as pd
from matplotlib import pyplot as plt

def get_sankey(data,path,value_col):
    sankey_data = {
    'label':[],
    'source': [],
    'target' : [],
    'value' : []
    }
    counter = 0
    while (counter < len(path) - 1):
        for parent in data[path[counter]].unique():
            sankey_data['label'].append(parent)
            for sub in data[data[path[counter]] == parent][path[counter+1]].unique():
                sankey_data['source'].append(sankey_data['label'].index(parent))
                sankey_data['label'].append(sub)
                sankey_data['target'].append(sankey_data['label'].index(sub))
                sankey_data['value'].append(data[data[path[counter+1]] == sub][value_col].sum())
                
        counter +=1
    return sankey_data
    
#%%
df = pd.read_csv("datasources.csv", sep=";")

my_sankey = get_sankey(df,['DS','DF','IM','UF'],'V')


fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 50,
      thickness = 20,
      line = dict(color = "black", width = 1),
      label = my_sankey['label'],
      color = "orange"
    ),
    link = dict(
        source = my_sankey['source'],
        target = my_sankey['target'],
        value = my_sankey['value']
  ))])

fig.update_layout(title_text="Data sources, data fields and utilization", font_size=14, width = 1000)
fig.show()


fig.write_image("datasources.png") 

# %%
