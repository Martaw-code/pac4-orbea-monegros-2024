"""
Mòdul ex2 - Exercici 2 de la PAC4

Objectiu:
- Anonimitzar el nom dels ciclistes (columna 'biker') amb Faker.
- Eliminar ciclistes amb temps 00:00:00.
- Recuperar ciclista amb dorsal=1000 (exemple).

"""

import pandas as pd
from faker import Faker

fake = Faker('es_ES')


def name_surname(df: pd.DataFrame) -> pd.DataFrame:
    """
    Retorna una còpia del DataFrame on la columna 'biker' ha estat
    substituïda per noms i cognoms falsos.

    :param df: DataFrame original.
    :return: DataFrame amb la columna 'biker' anonimitzada.
    """
    df_copy = df.copy()
    # Suposem que la columna amb el nom del ciclista es diu 'biker'
    df_copy['biker'] = df_copy['biker'].apply(lambda x: fake.name())
    return df_copy


def remove_zero_time(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina els registres on el temps sigui '00:00:00'.

    :param df: DataFrame original.
    :return: DataFrame sense els registres amb temps zero.
    """
    df_copy = df.copy()
    df_copy = df_copy[df_copy['time'] != '00:00:00']
    return df_copy


def get_cyclist_by_dorsal(df: pd.DataFrame, dorsal: int) -> pd.DataFrame:
    """
    Retorna les dades del ciclista amb el dorsal indicat.

    :param df: DataFrame a consultar.
    :param dorsal: Dorsal del ciclista.
    :return: DataFrame (filtat) amb les dades del ciclista trobat.
    """
    return df[df['dorsal'] == dorsal]

def run_ex2(df: pd.DataFrame) -> pd.DataFrame:
    """
    Executa l'Exercici 2, rebent el df resultant de l'ex1.
    """
    print("\n--- EXERCICI 2 ---")
    df = name_surname(df)
    print("1) 5 primers valors un cop anonimitzat:")
    print(df.head(5))

    df = remove_zero_time(df)
    print("\n2) Quants ciclistes queden després d'eliminar '00:00:00'?")
    print(len(df))
    print("   5 primers:")
    print(df.head(5))

    print("\n3) Recupera dades del ciclista amb dorsal=1000 (si existeix):")
    print(get_cyclist_by_dorsal(df, 1000))

    return df
