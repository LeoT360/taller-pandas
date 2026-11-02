import pandas as pd

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def analizar(df):
    print("\nInfo general:")
    df.info()
    print("\nEstadísticas numéricas:")
    print(df.describe())

    ingresos_por_categoria(df)
    canal_que_mas_vende(df)
    clientes_vip_vs_regular(df)
    metodo_pago_mas_usado(df)
    top5_clientes(df)


def ingresos_por_categoria(df):
    """Pregunta 1: ¿Qué categoría genera más ingresos?

    Pista: df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    """
    # TODO 8: calcular e imprimir los ingresos por categoría y la categoría que más ingresa.
    ingresos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    print("\n--- Ingresos por categoría ---")
    print(ingresos)
    print(f"\nLa categoría que más ingresos genera es: {ingresos.index[0]} con ${ingresos.iloc[0]:,.0f}")


def canal_que_mas_vende(df):
    """Pregunta 2: ¿Qué canal vende más?

    Pista: agrupar por "canal" y usar .agg(ventas=("id_venta", "count"), ingresos=("total", "sum")).
    """
    # TODO 9: calcular e imprimir ventas e ingresos por canal.
    canal = df.groupby("canal").agg(
        ventas=("id_venta", "count"),
        ingresos=("total", "sum")
    ).sort_values("ingresos", ascending=False)

    print("\n--- Ventas e ingresos por canal ---")
    print(canal)
    print(f"\nEl canal que más vende (por ingresos) es: {canal.index[0]}")


def clientes_vip_vs_regular(df):
    """Pregunta 3: ¿Los clientes VIP compran más que los Regulares?

    Pista: como hay más clientes Regular que VIP, compare promedios por cliente, no totales.
    Calcular: número de clientes (nunique), compras y gasto total por segmento,
    y luego dividir compras y gasto entre el número de clientes.
    """
    # TODO 10: calcular e imprimir compras y gasto promedio por cliente según segmento_cliente.
    resumen = df.groupby("segmento_cliente").agg(
        num_clientes=("id_cliente", "nunique"),
        compras=("id_venta", "count"),
        gasto_total=("total", "sum")
    )

    # Calculamos promedios por cliente
    resumen["compras_por_cliente"] = resumen["compras"] / resumen["num_clientes"]
    resumen["gasto_por_cliente"] = resumen["gasto_total"] / resumen["num_clientes"]

    print("\n--- Comparación VIP vs Regular ---")
    print(resumen[["num_clientes", "compras_por_cliente", "gasto_por_cliente"]])


def metodo_pago_mas_usado(df):
    """Pregunta 4: ¿Qué método de pago es más usado?

    Pista: df["metodo_pago"].value_counts()
    """
    # TODO 11: calcular e imprimir el conteo por método de pago y cuál es el más usado.
    metodos = df["metodo_pago"].value_counts()
    print("\n--- Métodos de pago ---")
    print(metodos)
    print(f"\nEl método de pago más usado es: {metodos.index[0]} ({metodos.iloc[0]} veces)")


def top5_clientes(df):
    """Pregunta 5: ¿Top 5 clientes con más compras?

    Pista: agrupar por ["id_cliente", "nombre_cliente"], contar compras y sumar total,
    ordenar por compras (y por gasto como desempate) y tomar las primeras 5 con .head(5).
    """
    # TODO 12: calcular e imprimir el top 5.
    top5 = (
        df.groupby(["id_cliente", "nombre_cliente"])
        .agg(compras=("id_venta", "count"), gasto=("total", "sum"))
        .sort_values(["compras", "gasto"], ascending=[False, False])
        .head(5)
    )

    print("\n--- Top 5 clientes con más compras ---")
    print(top5)
