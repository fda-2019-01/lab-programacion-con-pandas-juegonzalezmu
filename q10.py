##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 

import pandas as pd
import numpy as np
tbl1 = pd.read_csv("tbl1.tsv",
                          sep = '\t',
                          thousands = None,
                          decimal = '.')
data = pd.DataFrame({'x' : tbl1.groupby( ["_c0"] ).apply(lambda x: ':'.join(sorted(x['_c4']))) }).reset_index()
print(data)
