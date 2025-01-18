"""
Mòdul ex1 - Exercici 1 de la PAC4

Objectiu:
- Importació del dataset.
- Mostrar els 5 primers valors.
- Comptar el nombre de ciclistes.
- Mostrar les columnes del dataframe.

"""
import pandas as pd

def load_dataset(path_csv: str, sep: str = ";") -> pd.DataFrame:
    """
    Carrega el dataset en un DataFrame de pandas.

    :param path_csv: Ruta on es troba el fitxer CSV
    :param sep: Separador de columnes, default és ';'
    :return: DataFrame amb les dades carregades.
    """
    df = pd.read_csv(path_csv, sep=sep)
    return df


def show_head(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """
    Retorna els primers n registres del DataFrame.

    :param df: DataFrame amb les dades.
    :param n: Número de registres a mostrar (per defecte 5).
    :return: DataFrame amb els primers n registres.
    """
    return df.head(n)


def get_num_cyclists(df: pd.DataFrame) -> int:
    """
    Retorna quants ciclistes apareixen al dataset.

    :param df: DataFrame amb les dades.
    :return: Enter amb el nombre de ciclistes.
    """
    return len(df)


def get_columns(df: pd.DataFrame) -> list:
    """
    Retorna les columnes del DataFrame.

    :param df: DataFrame amb les dades.
    :return: Llista amb els noms de les columnes.
    """
    return list(df.columns)


def run_ex1(csv_path: str) -> pd.DataFrame:
    """
    Executa l'Exercici 1: carrega dataset, mostra EDA bàsica.
    Retorna el DataFrame per poder-lo aprofitar als exercicis següents.
    """
    print("\n--- EXERCICI 1 ---")
    df = load_dataset(csv_path)
    print(f"Carregat dataset de: {csv_path}")

    print("\n1) Mostrant els 5 primers valors:")
    print(show_head(df, 5))

    print("\n2) Quants ciclistes van participar a la prova?")
    print(get_num_cyclists(df))

    print("\n3) Columnes del dataframe:")
    print(get_columns(df))

    return df
