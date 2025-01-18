"""
Mòdul ex5 - Exercici 5 de la PAC4

Objectiu:
- Trobar ciclistes de la UCSC.
- Quina persona va fer millor temps.
- Posició en la classificació i percentatge.
"""
import pandas as pd


def get_ucsc_ciclistes(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Retorna tots els ciclistes pertanyents al club UCSC (Unió Ciclista Sant Cugat).
    Es busca en la columna 'club_clean' la paraula 'UCSC' exacta.

    :param data_frame: DataFrame original amb 'club_clean'.
    :return: DataFrame filtrat dels ciclistes del club UCSC.
    """
    return data_frame[data_frame['club_clean'] == 'UCSC']


def get_millor_temps_ucsc(data_frame_ucsc: pd.DataFrame) -> pd.Series:
    """
    Retorna la fila (Series) del ciclista de la UCSC amb el millor temps,
    suposant que 'time' és un string 'hh:mm:ss' i que el millor temps 
    és el menor temps en format cronològic.

    :param data_frame_ucsc: DataFrame amb ciclistes de la UCSC.
    :return: Fila (Series) corresponent al ciclista amb millor temps.
    """
    df_ucsc_copia = data_frame_ucsc.copy()
    df_ucsc_copia['time_td'] = pd.to_timedelta(df_ucsc_copia['time'])
    df_ucsc_copia = df_ucsc_copia.sort_values('time_td', ascending=True)
    return df_ucsc_copia.iloc[0]


def get_posicio_i_percentatge(data_frame: pd.DataFrame, dorsal: int) -> tuple:
    """
    Retorna la posició d'un ciclista (ordenat per temps ascendent) 
    i el percentatge que aquesta posició representa sobre el total.

    :param data_frame: DataFrame original amb la columna 'time' que es pot convertir a Timedelta.
    :param dorsal: dorsal del ciclista de qui volem saber la posició.
    :return: (posicio, percentatge)
    """
    df_copia = data_frame.copy()
    df_copia['time_td'] = pd.to_timedelta(df_copia['time'])
    df_copia = df_copia.sort_values('time_td', ascending=True).reset_index(drop=True)
    total = len(df_copia)

    # busquem l'índex del dorsal
    posicio = df_copia.index[df_copia['dorsal'] == dorsal].tolist()
    if not posicio:
        return None, None
    posicio = posicio[0] + 1  # +1 perquè index comença a 0
    percentatge = (posicio / total) * 100
    return posicio, percentatge

def run_ex5(data_frame: pd.DataFrame) -> None:
    """
    Executa l'Exercici 5, rebent el data_frame resultant de l'ex4.
    """
    print("\n--- EXERCICI 5 ---")
    data_frame_ucsc = get_ucsc_ciclistes(data_frame)
    print("1) Ciclistes de la UCSC:")
    print(data_frame_ucsc)

    if len(data_frame_ucsc) > 0:
        best_ucsc = get_millor_temps_ucsc(data_frame_ucsc)
        print("\n2) Ciclista de la UCSC amb millor temps:")
        print(best_ucsc)

        posicio, percent = get_posicio_i_percentatge(data_frame, best_ucsc['dorsal'])
        print(f"\n3) Posició d'aquest ciclista: {posicio} / {len(data_frame)}  -> {percent:.2f}%")
    else:
        print("No hi ha ciclistes de la UCSC al dataset.")
