"""
Mòdul ex2 - Exercici 2 de la PAC4

Objectiu:
- Anonimitzar el nom dels ciclistes (columna 'biker') amb Faker.
- Eliminar ciclistes amb temps 00:00:00.
- Recuperar ciclista amb dorsal=1000 (exemple).

"""
import pandas as pd
from faker import Faker


fake = Faker()


def name_surname(
        data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Retorna una còpia del DataFrame on la columna 'biker' ha estat
    substituïda per noms i cognoms falsos.

    :param data_frame: DataFrame original.
    :return: DataFrame amb la columna 'biker' anonimitzada.
    """
    df_copia = data_frame.copy()
    df_copia['biker'] = df_copia['biker'].apply(lambda x: fake.name())
    return df_copia


def elimina_temps_zero(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina els registres on el temps sigui '00:00:00'.

    :param data_frame: DataFrame original.
    :return: DataFrame sense els registres amb temps zero.
    """
    df_copia = data_frame.copy()
    df_copia = df_copia[df_copia['time'] != '00:00:00']
    return df_copia


def get_ciclista_per_dorsal(
        data_frame: pd.DataFrame,
        dorsal: int) -> pd.DataFrame:
    """
    Retorna les dades del ciclista amb el dorsal indicat.

    :param data_frame: DataFrame a consultar.
    :param dorsal: Dorsal del ciclista.
    :return: DataFrame (filtat) amb les dades del ciclista trobat.
    """
    return data_frame[data_frame['dorsal'] == dorsal]

def run_ex2(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Executa l'Exercici 2, rebent el data_frame resultant de l'ex1.
    """
    print("\n--- EXERCICI 2 ---")
    data_frame = name_surname(data_frame)
    print("1) 5 primers valors un cop anonimitzat:")
    print(data_frame.head(5))

    data_frame = elimina_temps_zero(data_frame)
    print("\n2) Quants ciclistes queden després d'eliminar '00:00:00'?")
    print(len(data_frame))
    print("   5 primers:")
    print(data_frame.head(5))

    print("\n3) Recupera dades del ciclista amb dorsal=1000 (si existeix):")
    print(get_ciclista_per_dorsal(data_frame, 1000))

    return data_frame
