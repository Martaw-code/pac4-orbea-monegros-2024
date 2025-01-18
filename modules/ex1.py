"""
Mòdul ex1 - Exercici 1 de la PAC4

Objectiu:
- Importació del dataset.
- Mostrar els 5 primers valors.
- Comptar el nombre de ciclistes.
- Mostrar les columnes del dataframe.

"""
import pandas as pd

def carrega_conjunt(
        ruta_csv: str,
        sep: str = ";") -> pd.DataFrame:
    """
    Carrega el dataset en un DataFrame de pandas.

    :param ruta_csv: Ruta on es troba el fitxer CSV
    :param sep: Separador de columnes, default és ';'
    :return: DataFrame amb les dades carregades.
    """
    data_frame = pd.read_csv(ruta_csv, sep=sep)
    return data_frame


def primers_registres(
        data_frame: pd.DataFrame,
        nombre_files: int = 5) -> pd.DataFrame:
    """
    Retorna els primers nombre_files registres del DataFrame.

    :param data_frame: DataFrame amb les dades.
    :param nombre_files: Nombre de registres a mostrar (per defecte 5).
    :return: DataFrame amb els primers nombre_files registres.
    """
    return data_frame.head(nombre_files)


def get_nombre_ciclistes(data_frame: pd.DataFrame) -> int:
    """
    Retorna quants ciclistes apareixen al dataset.

    :param data_frame: DataFrame amb les dades.
    :return: Enter amb el nombre de ciclistes.
    """
    return len(data_frame)


def get_columnes(data_frame: pd.DataFrame) -> list:
    """
    Retorna les columnes del DataFrame.

    :param data_frame: DataFrame amb les dades.
    :return: Llista amb els noms de les columnes.
    """
    return list(data_frame.columns)


def run_ex1(ruta_csv: str) -> pd.DataFrame:
    """
    Executa l'Exercici 1: carrega el dataset i mostra EDA bàsica.

    :param ruta_csv: DataFrame amb les dades
    :return: DataFrame per poder-lo aprofitar als exercicis següents.
    """
    print("\n--- EXERCICI 1 ---")
    data_frame = carrega_conjunt(ruta_csv)
    print(f"Carregat dataset de: {ruta_csv}")

    print("\n1) Mostrant els 5 primers valors:")
    print(primers_registres(data_frame, 5))

    print("\n2) Quants ciclistes van participar a la prova?")
    print(get_nombre_ciclistes(data_frame))

    print("\n3) Columnes del dataframe:")
    print(get_columnes(data_frame))

    return data_frame
