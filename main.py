"""
Fitxer principal: main.py
Crida les funcions run_exX() definides a cada exN.py
"""
import argparse

from modules.ex1 import run_ex1
from modules.ex2 import run_ex2
from modules.ex3 import run_ex3
from modules.ex4 import run_ex4
from modules.ex5 import run_ex5

def parse_args():
    """
    Analitza els paràmetres de la línia de comandes i retorna
    un objecte argparse.Namespace.

    Returns:
        argparse.Namespace: Objecte amb els paràmetres 'exercise' i 'csv'.
          - exercise (str): Quin exercici s'ha de dur a terme (ex1, ex2, ex3, ex4, ex5 o all).
          - csv (str): Ruta al fitxer CSV amb el dataset (per defecte data/dataset.csv).
    """
    parser = argparse.ArgumentParser(
        description="PAC4 Orbea Monegros - Controlador d'exercicis"
    )
    parser.add_argument(
        "--exercise",
        "-e",
        default="all",
        help="Exercici a executar (ex1, ex2, ex3, ex4, ex5 o all). Per defecte, all."
    )
    parser.add_argument(
        "--csv",
        "-c",
        default="../data/dataset.csv",
        help="Ruta del CSV amb el dataset (per defecte data/dataset.csv)."
    )
    return parser.parse_args()

def main():
    """
    Funció principal que:
      1) Obté els paràmetres d'entrada amb parse_args().
      2) Executa l'exercici (o exercicis) corresponent(s) en funció del paràmetre 'exercise'.
         - all -> executa ex1, ex2, ex3, ex4 i ex5 en ordre.
         - exN -> executa l'exN, assegurant-se prèviament de carregar el DF de l'ex1 i ex2, etc.

    Retorna:
        None
    """
    args = parse_args()

    if args.exercise == "all":
        df_ex1 = run_ex1(args.csv)
        df_ex2 = run_ex2(df_ex1)
        df_ex3 = run_ex3(df_ex2)
        df_ex4 = run_ex4(df_ex3)
        run_ex5(df_ex4)

    elif args.exercise == "ex1":
        run_ex1(args.csv)

    elif args.exercise == "ex2":
        df_ex1 = run_ex1(args.csv)
        run_ex2(df_ex1)

    elif args.exercise == "ex3":
        df_ex1 = run_ex1(args.csv)
        df_ex2 = run_ex2(df_ex1)
        run_ex3(df_ex2)

    elif args.exercise == "ex4":
        df_ex1 = run_ex1(args.csv)
        df_ex2 = run_ex2(df_ex1)
        df_ex3 = run_ex3(df_ex2)
        run_ex4(df_ex3)

    elif args.exercise == "ex5":
        df_ex1 = run_ex1(args.csv)
        df_ex2 = run_ex2(df_ex1)
        df_ex3 = run_ex3(df_ex2)
        df_ex4 = run_ex4(df_ex3)
        run_ex5(df_ex4)

    else:
        print(f"Exercici '{args.exercise}' no reconegut.")

if __name__ == "__main__":
    main()
