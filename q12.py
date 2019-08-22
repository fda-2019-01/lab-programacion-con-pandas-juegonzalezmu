##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 

import pandas as pd
tbl2 = pd.read_csv("tbl2.tsv",
	sep = '\t',         
	thousands = None,  
	decimal = '.')
tbl0 = pd.read_csv("tbl0.tsv",
	sep = '\t',         
	thousands = None,  
	decimal = '.')
x=pd.merge(tbl0, tbl2, on='_c0')
print((x.groupby('_c5a')['_c5b'].sum()))
