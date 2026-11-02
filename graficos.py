from pathlib import Path

import matplotlib.pyplot as plt

SALIDA = Path(__file__).parent / "Data" / "processed" / "graficos"


def grafico_ventas_por_categoria(df):
    """Gráfico de barras: total vendido por categoría.

    Pistas:
    - Calcular datos = df.groupby("categoria")["total"].sum()
    - datos.plot(kind="bar") dibuja las barras.
    - plt.title, plt.xlabel y plt.ylabel ponen los textos.
    - plt.savefig(SALIDA / "ventas_por_categoria.png", bbox_inches="tight") guarda la imagen.
    - plt.show() la muestra en pantalla y plt.close() la cierra.
    """
    # TODO 13: dibujar, poner títulos, guardar y mostrar el gráfico.
    # Crear la carpeta de salida si no existe
    SALIDA.mkdir(parents=True, exist_ok=True)

    datos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)

    datos.plot(kind="bar", color="steelblue")
    plt.title("Total vendido por categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Total ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(SALIDA / "ventas_por_categoria.png", bbox_inches="tight")
    plt.show()
    plt.close()


def grafico_ventas_por_canal(df):
    """Gráfico de barras: total vendido por canal (Online contra Tienda).

    Usa los mismos pasos que la función anterior, cambiando la columna "categoria" por "canal".
    """
    # TODO 14: dibujar, poner títulos, guardar y mostrar el gráfico.
    SALIDA.mkdir(parents=True, exist_ok=True)

    datos = df.groupby("canal")["total"].sum().sort_values(ascending=False)

    datos.plot(kind="bar", color="seagreen")
    plt.title("Total vendido por canal")
    plt.xlabel("Canal")
    plt.ylabel("Total ($)")
    plt.xticks(rotation=0)
    plt.tight_layout()

    plt.savefig(SALIDA / "ventas_por_canal.png", bbox_inches="tight")
    plt.show()
    plt.close()


def graficar(df):
    grafico_ventas_por_categoria(df)
    grafico_ventas_por_canal(df)
