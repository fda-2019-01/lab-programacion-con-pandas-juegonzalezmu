##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
import pandas as pd
tbl2 = pd.read_csv('tbl2.tsv', sep='\t')
tbl2['_c5a'] = tbl2['_c5a'].astype(str)
tbl2['_c5b'] = tbl2['_c5b'].astype(str)

data = pd.DataFrame({
    'lista': tbl2.groupby(['_c0']).apply(lambda x: ','.join(sorted(x['_c5a'] + ':' + x['_c5b'])))
}).reset_index()
print(data)
