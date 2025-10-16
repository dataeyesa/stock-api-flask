import pandas as pd
import sqlite3

# Cargar Excel
df = pd.read_excel("Stock.xlsx")
df = df.dropna(how='all')
df.columns = [str(col).strip() for col in df.columns]

# Limitar columnas útiles
columnas_utiles = [
    "Referencia", "Nombre producto", "Medellin", "Bogota", "Cali", "Barranquilla",
    "Cartagena", "Producción", "Precio lista", "Desc", "Precio con Descuento", "Min_Med", "Max_Med", 
    "Min_Bog", "Max_Bog", "Min_Cal", "Max_Cal", "Min_Baq", "Max_Baq", "Min_Crt", "Max_Crt"
]
df = df[columnas_utiles] 

# Crear DB 
conn = sqlite3.connect("stock.db") 
df.to_sql("inventario", conn, if_exists="replace", index=False) 
conn.close() 

print("✅ stock.db creado") 