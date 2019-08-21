##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas as pd
data=pd.read_csv('tbl1.tsv',sep='\t')
print(sorted(list(set(df['_c4'].str.upper()))))

