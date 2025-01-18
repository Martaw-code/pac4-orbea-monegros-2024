"""
Fitxer principal: main.py

Aquest fitxer actua com a punt d'entrada per a la PAC4 Orbea Monegros.
Rep paràmetres de la línia de comandes i executa els exercicis
corresponents (ex1, ex2, ex3, ex4, ex5 o all), utilitzant
les funcions run_exX() definides als mòduls ex1.py, ex2.py, etc.
"""
import argparse

from modules.ex1 import run_ex1
from modules.ex2 import run_ex2
from modules.ex3 import run_ex3
from modules.ex4 import run_ex4
from modules.ex5 import run_ex5

def parse_args() -> argparse.Namespace:
    """
    Analitza i retorna els paràmetres de línia de comandes.

    Retorna:
        argparse.Namespace: Conté els dos paràmetres 'exercise' i 'csv'.

        - exercise (str): Indica quin exercici executar
          (ex1, ex2, ex3, ex4, ex5 o all). Per defecte 'all'.
        - csv (str): Ruta al fitxer CSV amb el dataset. Per defecte "data/dataset.csv".
    """
    parser = argparse.ArgumentParser(
        description="PAC4 Orbea Monegros - Controlador d'exercicis"
    )
    parser.add_argument(
        "--exercise", "-e",
        default="all",
        help="Exercici a executar (ex1, ex2, ex3, ex4, ex5 o all). Per defecte, all."
    )
    parser.add_argument(
        "--csv", "-c",
        default="data/dataset.csv",
        help="Ruta del CSV amb el dataset (per defecte data/dataset.csv)."
    )
    return parser.parse_args()


def main() -> None:
    """
    Funció principal de la PAC4 Orbea Monegros:

    1. Obté els paràmetres d'entrada amb parse_args().
    2. En funció de 'exercise', executa un o diversos exercicis:
       - 'all'  -> ex1, ex2, ex3, ex4 i ex5 en ordre.
       - 'ex1'  -> només ex1
       - 'ex2'  -> carrega df d'ex1 i fa ex2
       - 'ex3'  -> ex1 + ex2 + ex3
       - 'ex4'  -> ex1 + ex2 + ex3 + ex4
       - 'ex5'  -> ex1 + ex2 + ex3 + ex4 + ex5
       - qualsevol altre valor -> no reconegut

    També té l'opció de canviar la ruta del dataset via '--csv data/altre.csv'.

    Retorna:
        None
    """
    args = parse_args()

    # Execució dels exercicis segons el valor de --exercise
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

if __name__ == "__main__": # pragma: no cover
    main()
