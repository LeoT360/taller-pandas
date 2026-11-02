# Taller práctico: análisis de datos con Pandas

Programa de consola que lee datos de ventas y clientes, los limpia, los une y los analiza. Se ejecuta desde un menú en la terminal, y cada opción corresponde a un módulo que vas a completar paso a paso.

Recuerda consultar la guía adjunta en PDF donde se te dará el paso a paso del trabajo.

## Requisitos

- Python 3.10 o superior
- Git (para clonar el repositorio)
- Conocimientos básicos de variables, listas y funciones

## Cómo empezar

1. Clona el repositorio y entra a la carpeta del proyecto:

   ```
   git clone <URL-DEL-REPOSITORIO>
   cd <NOMBRE-DE-LA-CARPETA>
   ```

2. Crea y activa un ambiente virtual. Las instrucciones completas, para Windows y Mac/Linux, están en `LEEME_ambiente.txt`.

3. Instala las librerías:

   ```
   pip install -r requirements.txt
   ```

4. Ejecuta el programa:

   ```
   python main.py
   ```

Ejecuta siempre los comandos desde la carpeta del proyecto. Los módulos buscan los archivos a partir de su ubicación.

## Estructura del proyecto

```
├── main.py            Menú principal. No lo modifiques.
├── carga.py           Lee los CSV. Ya está completo.
├── limpieza.py        Limpia clientes y ventas. TODO 1 a 5.
├── merge.py           Valida y une las tablas. TODO 6 y 7.
├── analisis.py        Responde las preguntas de negocio. TODO 8 a 12.
├── graficos.py        Dibuja dos gráficos sencillos. TODO 13 y 14.
├── exploracion.py     Ejemplos de indexación, .loc, .iloc y concat. Se ejecuta por separado.
├── requirements.txt   Versiones de las librerías.
├── LEEME_ambiente.txt Pasos para crear el ambiente virtual.
└── Data/
    ├── raw/           Datos originales (cliente.csv, ventas.csv). No los modifiques.
    └── processed/     Resultados que genera el programa.
```

## Menú

| Opción | Qué hace |
|---|---|
| 1 | Carga los archivos CSV |
| 2 | Limpia los datos |
| 3 | Valida y une las tablas con merge |
| 4 | Muestra el análisis y las respuestas del desafío |
| 5 | Dibuja los gráficos de introducción |
| 6 | Sale del programa |

Las opciones se usan en orden: primero cargar (1), luego limpiar (2), después unir (3) y finalmente analizar (4) o graficar (5).

## Cómo completar el taller

1. Abre el archivo indicado en cada TODO. Cada función tiene un docstring con pistas.
2. Completa el TODO y ejecuta `python main.py` para probar la opción correspondiente.
3. Usa `exploracion.py` para practicar indexación, `.loc`, `.iloc` y `concat()` antes de aplicarlos en tu código.

Las funciones que aún no completaste no dan error: devuelven los datos sin cambios, así que el menú siempre funciona.

## Entregables

Consulta el documento del taller (`guia_Taller_Pandas.pdf`) para ver el detalle de cada entregable y la rúbrica. En resumen:

- Entregable 0: pantallazo del ambiente virtual activo y de la instalación.
- Entregable 1: pantallazos de `.shape`, `.info()` y `.describe()`, y salida de `exploracion.py`.
- Entregable 2: limpieza, con pantallazos antes y después y explicación.
- Entregable 3: validación, merge y análisis, con pantallazos de las opciones 3 y 4.
- Entregable 4: los dos gráficos (`.png`) y el código de `graficos.py`.
- Desafío final: respuestas a las cinco preguntas, con el criterio usado en cada una.

Para entregar, agrega al final de este `README.md` una sección con tu nombre y tus respuestas a las preguntas del desafío. Sube tus cambios al repositorio y envía el enlace por el formulario de entrega. La entrega es individual.

## Preguntas de negocio

1. ¿Qué categoría genera más ingresos?
2. ¿Qué canal vende más?
3. ¿Los clientes VIP compran más que los Regulares?
4. ¿Qué método de pago es el más usado?
5. ¿Cuáles son los cinco clientes con más compras?

---

## Entregable final

**Alumno:** Jesús Leonardo Torre Melgarejo | **Documento:** 1020497992

### Respuestas del Desafío Final

**1. ¿Qué categoría genera más ingresos?**  
La categoría **Tecnología** genera más ingresos, con un total de **$14.290.000**.

Criterio: Suma del campo `total` agrupado por `categoria`.

**2. ¿Qué canal vende más?**  
El canal **Online** vende más.  
- Online: 35 ventas = $14669000
- Tienda: 33 ventas = $4507000

Criterio: Ingresos totales.

**3. ¿Los clientes VIP compran más que los Regulares?**  
Si, los clientes VIP tienen un promedio de **1.21 compras**, mientras que los Regulares tienen **1.08 compras**.

Criterio: Se compararon promedios por cliente porque hay distinta cantidad de clientes.

**4. ¿Qué método de pago es el más usado?**  
El método de pago más usado es **Efectivo**.

Criterio: Conteo de ventas por método de pago.

**5. ¿Cuáles son los cinco clientes con más compras?**  
1. Nicolas Cardona   | 2 compras | $2.515.000  
2. Matias Rodriguez  | 2 compras | $1.278.000  
3. Mia Quintero      | 2 compras | $1.090.000  
4. Luna Montoya      | 2 compras | $1.007.000  
5. Luis Perez        | 2 compras | $730.000  

Criterio: número de compras y gasto total.