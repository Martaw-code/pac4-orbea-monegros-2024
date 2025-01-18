"""
Mòdul ex5 - Exercici 5 de la PAC4

Objectiu:
- Trobar ciclistes de la UCSC.
- Quina persona va fer millor temps.
- Posició en la classificació i percentatge.
"""

import pandas as pd


def get_ucsc_cyclists(df: pd.DataFrame) -> pd.DataFrame:
    """
    Retorna tots els ciclistes pertanyents al club UCSC (Unió Ciclista Sant Cugat).
    Es busca en la columna 'club_clean' la paraula 'UCSC' exacta.

    :param df: DataFrame original amb 'club_clean'.
    :return: DataFrame filtrat dels ciclistes del club UCSC.
    """
    return df[df['club_clean'] == 'UCSC']


def get_best_time_ucsc(df_ucsc: pd.DataFrame) -> pd.Series:
    """
    Retorna la fila (Series) del ciclista de la UCSC amb el millor temps,
    suposant que 'time' és un string 'hh:mm:ss' i que el millor temps 
    és el menor temps en format cronològic.

    :param df_ucsc: DataFrame amb ciclistes de la UCSC.
    :return: Fila (Series) corresponent al ciclista amb millor temps.
    """
    # Convertim la columna 'time' a Timedelta per poder ordenar
    df_ucsc_copy = df_ucsc.copy()
    df_ucsc_copy['time_td'] = pd.to_timedelta(df_ucsc_copy['time'])
    df_ucsc_copy = df_ucsc_copy.sort_values('time_td', ascending=True)
    return df_ucsc_copy.iloc[0]


def get_position_and_percentage(df: pd.DataFrame, dorsal: int) -> tuple:
    """
    Retorna la posició d'un ciclista (ordenat per temps ascendent) 
    i el percentatge que aquesta posició representa sobre el total.

    :param df: DataFrame original amb la columna 'time' que es pot convertir a Timedelta.
    :param dorsal: dorsal del ciclista de qui volem saber la posició.
    :return: (posicio, percentatge)
    """
    df_copy = df.copy()
    df_copy['time_td'] = pd.to_timedelta(df_copy['time'])
    df_copy = df_copy.sort_values('time_td', ascending=True).reset_index(drop=True)
    total = len(df_copy)

    # busquem l'índex del dorsal
    posicio = df_copy.index[df_copy['dorsal'] == dorsal].tolist()
    if not posicio:
        return None, None
    posicio = posicio[0] + 1  # +1 perquè index comença a 0
    percentatge = (posicio / total) * 100
    return posicio, percentatge

def run_ex5(df: pd.DataFrame) -> None:
    """
    Executa l'Exercici 5, rebent el df resultant de l'ex4.
    """
    print("\n--- EXERCICI 5 ---")
    df_ucsc = get_ucsc_cyclists(df)
    print("1) Ciclistes de la UCSC:")
    print(df_ucsc)

    if len(df_ucsc) > 0:
        best_ucsc = get_best_time_ucsc(df_ucsc)
        print("\n2) Ciclista de la UCSC amb millor temps:")
        print(best_ucsc)

        posicio, percent = get_position_and_percentage(df, best_ucsc['dorsal'])
        print(f"\n3) Posició d'aquest ciclista: {posicio} / {len(df)}  -> {percent:.2f}%")
    else:
        print("No hi ha ciclistes de la UCSC al dataset.")
