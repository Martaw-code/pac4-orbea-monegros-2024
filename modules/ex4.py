"""
Mòdul ex4 - Exercici 4 de la PAC4

Objectiu:
- Netejar els noms dels clubs seguint unes regles determinades.
- Crear la nova columna 'club_clean'.
- Agrupar per 'club_clean' per comptar ciclistes.
"""

import re
import pandas as pd


def clean_club(club: str) -> str:
    """
    Neteja el nom del club seguint les regles:
    1. Convertir a majúscules
    2. Eliminar les subcadenes: 'PEÑA CICLISTA ', 'PENYA CICLISTA ', 
       'AGRUPACIÓN CICLISTA ', 'AGRUPACION CICLISTA ', 'AGRUPACIÓ CICLISTA ',
       'AGRUPACIO CICLISTA ', 'CLUB CICLISTA ', 'CLUB '
    3. Eliminar (si estan al principi) les subcadenes amb expressió regular:
       'C.C. ', 'C.C ', 'CC ', 'C.D. ', 'C.D ', 'CD ', 'A.C. ', 'A.C ', 'AC ',
       'A.D. ', 'A.D ', 'AD ', 'A.E. ', 'A.E ', 'AE ', 'E.C. ', 'E.C ', 'EC ',
       'S.C. ', 'S.C ', 'SC ', 'S.D. ', 'S.D ', 'SD '
    4. Eliminar (si estan al final) ' T.T.', ' T.T', ' TT', ' T.E.', ' T.E',
       ' TE', ' C.C.', ' C.C', ' CC', ' C.D.', ' C.D', ' CD', ' A.D.', ' A.D',
       ' AD', ' A.C.', ' A.C', ' AC'
    5. Eliminar espais en blanc al principi i final.

    :param club: Nom original del club.
    :return: Nom del club netejat.
    """
    # Pas 1
    club = club.upper()

    # Pas 2 - Eliminar subcadenes fixes
    remove_list_2 = [
        'PEÑA CICLISTA ', 'PENYA CICLISTA ', 'AGRUPACIÓN CICLISTA ',
        'AGRUPACION CICLISTA ', 'AGRUPACIÓ CICLISTA ', 'AGRUPACIO CICLISTA ',
        'CLUB CICLISTA ', 'CLUB '
    ]
    for pattern in remove_list_2:
        club = club.replace(pattern, '')

    # Pas 3 - Eliminar subcadenes si estan al principi
    remove_list_3 = [
        r'^C\.C\. ', r'^C\.C ', r'^CC ', r'^C\.D\. ', r'^C\.D ', r'^CD ',
        r'^A\.C\. ', r'^A\.C ', r'^AC ', r'^A\.D\. ', r'^A\.D ', r'^AD ',
        r'^A\.E\. ', r'^A\.E ', r'^AE ', r'^E\.C\. ', r'^E\.C ', r'^EC ',
        r'^S\.C\. ', r'^S\.C ', r'^SC ', r'^S\.D\. ', r'^S\.D ', r'^SD '
    ]
    for pattern in remove_list_3:
        club = re.sub(pattern, '', club)

    # Pas 4 - Eliminar subcadenes si estan al final
    remove_list_4 = [
        r' T\.T\.$', r' T\.T$', r' TT$', r' T\.E\.$', r' T\.E$', r' TE$',
        r' C\.C\.$', r' C\.C$', r' CC$', r' C\.D\.$', r' C\.D$', r' CD$',
        r' A\.D\.$', r' A\.D$', r' AD$', r' A\.C\.$', r' A\.C$', r' AC$'
    ]
    for pattern in remove_list_4:
        club = re.sub(pattern, '', club)

    # Pas 5 - Eliminar espais en blanc
    club = club.strip()

    return club


def afegir_columna_clean_club(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Retorna un nou DataFrame amb la columna 'club_clean' netejada.

    :param data_frame: DataFrame original.
    :return: DataFrame amb la nova columna 'club_clean'.
    """
    df_copia = data_frame.copy()
    df_copia['club_clean'] = df_copia['club'].apply(clean_club)
    return df_copia


def groupby_club_clean(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa pel camp 'club_clean' i retorna un dataframe amb el nom del club
    i el número de ciclistes de cada club, ordenat de més a menys.

    :param data_frame: DataFrame amb la columna 'club_clean'.
    :return: DataFrame amb ['club_clean', 'count'] ordenat desc.
    """
    grouped = data_frame.groupby('club_clean').size().reset_index(name='count')
    grouped = grouped.sort_values('count', ascending=False)
    return grouped

def run_ex4(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Executa l'Exercici 4, rebent el df resultant de l'ex3.
    """
    print("\n--- EXERCICI 4 ---")
    data_frame = afegir_columna_clean_club(data_frame)
    print("1) 15 primers valors amb columna 'club_clean':")
    print(data_frame.head(15)[['club', 'club_clean']])

    club_grouped = groupby_club_clean(data_frame)
    print("\n2) DataFrame ordenat per número de ciclistes a cada club:")
    print(club_grouped)

    return data_frame
