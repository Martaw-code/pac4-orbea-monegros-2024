"""
Mòdul ex3 - Exercici 3 de la PAC4

Objectiu:
- Conversió d'un temps hh:mi:ss al format hh:00/hh:20/hh:40.
- Crear una nova columna amb aquest agrupament.
- Crear un histograma i guardar-lo a 'img/histograma.png'.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def minutes_002040(temps_str: str) -> str:
    """
    Rep un valor de temps en format 'hh:mi:ss' i retorna un valor 'hh:mi'
    on mi només pot ser 00, 20 o 40, segons la franja de 20 minuts.

    Ex:
        - '06:19:40' -> '06:00'
        - '06:29:40' -> '06:20'
        - '06:59:40' -> '06:40'

    :param temps_str: String amb el temps en format 'hh:mi:ss'.
    :return: String amb el temps agrupat en format 'hh:mi'.
    """
    hh, mi, ss = temps_str.split(':')
    hh = int(hh)
    mi = int(mi)
    ss = int(ss)

    # Calculem a quina franja pertany
    if 0 <= mi < 20:
        mi_group = '00'
    elif 20 <= mi < 40:
        mi_group = '20'
    else:
        mi_group = '40'

    return f"{hh:02d}:{mi_group}"


def crea_time_grouped(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Crea una nova columna 'time_grouped' aplicant la funció 'minutes_002040'
    a la columna 'time'.

    :param data_frame: DataFrame original.
    :return: DataFrame amb la columna 'time_grouped' afegida.
    """
    df_copia = data_frame.copy()
    df_copia['time_grouped'] = df_copia['time'].apply(minutes_002040)
    return df_copia


def groupby_time_grouped(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa el DataFrame per la columna 'time_grouped' i en compte quants ciclistes
    hi ha a cada franja de temps.

    :param data_frame: DataFrame que conté la columna 'time_grouped'.
    :return: DataFrame amb les columnes ['time_grouped', 'count'].
    """
    grouped = data_frame.groupby('time_grouped').size().reset_index(name='count')
    return grouped


def plot_histograma(
        grouped_df: pd.DataFrame,
        output_path: str = "../img/histograma.png") -> None:
    """
    Genera un histograma (o bé un bar plot) a partir de la informació agrupada
    en franges de 20 min i el desa a 'img/histograma.png'.

    :param grouped_df: DataFrame amb dues columnes: ['time_grouped', 'count'].
    :param output_path: Ruta on desar la imatge (png).
    """
    plt.figure(figsize=(8, 5))
    plt.bar(grouped_df['time_grouped'], grouped_df['count'], color='blue')
    plt.xlabel('Franja de temps (hh:mi)')
    plt.ylabel('Nombre de ciclistes')
    plt.title('Histogram de ciclistes per franja de 20 min')
    plt.savefig(output_path, dpi=150)
    plt.close()


def run_ex3(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Executa l'Exercici 3, rebent el df resultant de l'ex2.
    """
    print("\n--- EXERCICI 3 ---")
    data_frame = crea_time_grouped(data_frame)
    print("1) 15 primers valors amb columna time_grouped:")
    print(data_frame.head(15))

    grouped_df = groupby_time_grouped(data_frame)
    print("\n2) Agrupament per franges de 20 min:")
    print(grouped_df)

    print("\n3) Generant histograma i guardant a img/histograma.png...")
    plot_histograma(grouped_df, os.path.join("..", "img", "histograma.png"))
    print("   Fet!")

    return data_frame
