import pandas as pd

from carga import cargar_datos

_, ventas = cargar_datos()

# Indexación: usamos id_venta como índice
ventas = ventas.set_index("id_venta")

print("Primeras filas con índice id_venta:")
print(ventas.head())

# .loc busca por ETIQUETA (el ID de venta)
print("\n.loc['V003', 'total']:")
print(ventas.loc["V003", "total"])

# .iloc busca por POSICIÓN (empieza en 0)
print("\n.iloc[2, 6]:")
print(ventas.iloc[2, 6])

# Rangos: .loc incluye el final, .iloc no
print("\n.loc['V001':'V006'] (por etiqueta, incluye V006):")
print(list(ventas.loc["V001":"V006"].index))

print("\n.iloc[0:5] (por posición, NO incluye la posición 5, que es V006):")
print(list(ventas.iloc[0:5].index))

# concat: unir de nuevo partes de la misma tabla
ventas["fecha_venta"] = pd.to_datetime(ventas["fecha_venta"])
abril = ventas[ventas["fecha_venta"].dt.month == 4]
mayo = ventas[ventas["fecha_venta"].dt.month == 5]
print("\nFilas de abril:", len(abril), "| filas de mayo:", len(mayo))

total = pd.concat([abril, mayo])
print("Filas tras concat:", len(total), "| filas originales:", len(ventas))

print("===== CLIENTES =====")
clientes = pd.read_csv("Data/raw/cliente.csv")
print("\n.shape:")
print(clientes.shape)
print("\n.info():")
clientes.info()
print("\n.describe():")
print(clientes.describe())

print("\n\n===== VENTAS =====")
ventas = pd.read_csv("Data/raw/ventas.csv")
print("\n.shape:")
print(ventas.shape)
print("\n.info():")
ventas.info()
print("\n.describe():")
print(ventas.describe())