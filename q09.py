##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 
import pandas as pd
import numpy as np
tbl0 = pd.read_csv("tbl0.tsv",
                          sep = '\t',
                          thousands = None,
                          decimal = '.')
tbl0['_c2'] = tbl0['_c2'].astype(str)
data = pd.DataFrame({'x' : tbl0.groupby( ["_c1"] ).apply(lambda x: ':'.join(sorted(x['_c2']))) }).reset_index()
data.columns = ['_c0', 'x']
print(data)

