from pathlib import Path

PROCESSED = Path(__file__).parent / "Data" / "processed"


def validar_premerge(clientes, ventas):
    """Revisa que el merge se pueda hacer. Devuelve True si todo está bien, False si no.

    Revisar:
    - Que exista la columna "id_cliente" en los dos dataframes.
    - Que "id_cliente" no esté repetido en clientes.
    - Que "id_cliente" tenga el mismo tipo en los dos dataframes.
    - Cuántas ventas no tienen cliente asociado (esto solo se informa, no falla).
    """
    # TODO 6: escribir las validaciones y devolver True o False.
    # 1. Verificar que exista la columna id_cliente en ambos
    if "id_cliente" not in clientes.columns or "id_cliente" not in ventas.columns:
        print("Error: falta la columna 'id_cliente' en alguna de las tablas.")
        return False

    # 2. Verificar que no haya id_cliente repetidos en clientes
    if clientes["id_cliente"].duplicated().any():
        print("Error: hay id_cliente repetidos en la tabla de clientes.")
        return False

    # 3. Verificar que el tipo de dato sea el mismo
    if clientes["id_cliente"].dtype != ventas["id_cliente"].dtype:
        print("Error: el tipo de 'id_cliente' es diferente en las dos tablas.")
        return False

    # 4. Informar cuántas ventas no tienen cliente asociado (solo informa, no falla)
    clientes_ids = set(clientes["id_cliente"])
    ventas_sin_cliente = ventas[~ventas["id_cliente"].isin(clientes_ids)]
    print(f"Ventas sin cliente asociado: {len(ventas_sin_cliente)}")

    print("Validación pre-merge: OK")
    return True


def unir(clientes, ventas):
    """Une ventas con clientes usando "id_cliente" y guarda el resultado en Data/processed/merge.csv.

    Pistas:
    - Usar pd.merge(...) o ventas.merge(...).
    - Usar how="left" para no perder ventas.
    - Usar validate="m:1" para confirmar que cada venta tiene un solo cliente.
    - Guardar con df.to_csv(...) en PROCESSED / "merge.csv".
    """
    # TODO 7: validar con validar_premerge(), hacer el merge, guardar el CSV y devolver el dataframe.
    # Validar antes de unir
    if not validar_premerge(clientes, ventas):
        print("No se puede realizar el merge por errores de validación.")
        return None

    # Hacer el merge (left para no perder ventas)
    df_merge = ventas.merge(
        clientes,
        on="id_cliente",
        how="left",
        validate="m:1"
    )

    # Crear la carpeta processed si no existe
    PROCESSED.mkdir(parents=True, exist_ok=True)

    # Guardar el resultado
    df_merge.to_csv(PROCESSED / "merge.csv", index=False)
    print(f"Merge guardado en: {PROCESSED / 'merge.csv'}")
    print(f"Filas del merge: {len(df_merge)}")

    return df_merge
