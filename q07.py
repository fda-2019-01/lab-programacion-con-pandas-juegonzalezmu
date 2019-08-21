##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 
import pandas as pd
import numpy as np
tbl0=pd.read_csv("tbl0.tvs"
suma2=tbl0[['_c0',
              '_c1',
              '_c2',
              '_c3']].copy()
suma2['suma']=suma2.apply(lambda x: x['_c0'] + x['_c2'], axis=1 )
print(suma2)
