##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
## 
import pandas as pd
data=pd.read_csv('tbl0.tsv',sep='\t')
print(data.groupby('_c1')['_c0'].count())
