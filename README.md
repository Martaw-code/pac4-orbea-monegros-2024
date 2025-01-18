# PAC4 - Orbea Monegros 2024

Aquest projecte és la PAC4 de l'assignatura "Programació per a la Ciència de Dades", on s'analitza un dataset de l'Orbea Monegros 2024.

## Autora

Marta Granero I Martí

## 1. Estructura del projecte

- **`LICENSE`**: El document de llicència.  
- **`README.md`**: Explicació general del projecte, estructura, eines, exercicis, Makefile 
- **`INSTALL.md`**: Guia d’instal·lació i com dur a terme l'execució dels exercicis, la documentació i el paquet.
- **`requirements.txt`**: Llista de dependències necessàries (pandas, Faker, matplotlib, etc.).  
- **`setup.py`**: Script per empaquetar el projecte com a paquet instal·lable (genera `sdist` i `wheel`).  
- **`Makefile`**: Script per executar comandes de forma automatitzada (creació d’entorn virtual, instal·lació, execució de tests, cobertura, etc.).  
- **`data/`**: Fitxers de dades com el `dataset.csv`.  
- **`img/`**: Imatges generades pel codi (histograma, etc.).  
- **`modules/`**: Codi Python separat per cada exercici (`ex1.py`, `ex2.py`, `ex3.py`, `ex4.py` i `ex5.py`).  
- **`main.py`**: Punt d’entrada principal (rep paràmetres com `--exercise ex1` o bé `--csv data/dataset`) i crida els mòduls.  
- **`tests/`**: Fitxers de test unitaris (ex: `test_ex1.py`) i suite addicional (`test_suite.py`).


## 2. Eines i paquets utilitzats

Al projecte hem fet servir diverses eines i llibreries:

- **Python 3.12** (o superior).
- **pandas**: per carregar i manipular dades (EDA).
- **matplotlib**: per generar l’histograma (Ex3).
- **Faker**: per anonimitzar el nom dels ciclistes (Ex2).
- **pytest** / **unittest**: per fer tests unitaris.
- **coverage**: per calcular la cobertura de codi.
- **pylint**: per comprovar l’estil segons la PEP8.
- **pdoc**: per generar documentació automàtica a partir dels docstrings.
- **Makefile**: per facilitar la creació d’entorn virtual, instal·lació de dependències, execució dels exercicis, tests, cobertura, documentació, creació del paquet i instal·lació del mateix al nostre entorn.
- **setup.py**: per empaquetar el projecte com un paquet (sdist + wheel) i poder-lo instal·lar amb `pip install dist/...`.

Totes aquestes depenen d'**`requirements.txt`**, on es defineixen versions concretes o mínimes.


## 3. Exercicis (Ex1 → Ex5)

1. **Ex1**: Carrega el dataset i mostra la EDA bàsica.  
2. **Ex2**: Anonimitza ciclistes amb Faker, elimina els ciclistes amb temps zero i retorna el ciclista amb dorsal 1000.  
3. **Ex3**: Agrupament dels temps dels ciclistes cada 20 min i generació de l'histograma (`img/histograma.png`) per veure el nombre de ciclistes per cada franja temporal.  
4. **Ex4**: Neteja i uniformitza els noms de clubs ciclistes.  
5. **Ex5**: Filtra la Unió Ciclista Sant Cugat (UCSC), troba el millor temps del ciclista de la Unió i calcula la posició/percentatge del ciclista en el rànquing global.


## 3. Makefile

Aquest projecte inclou un **Makefile** per automatitzar i simplificar la instal·lació i les tasques de la PAC que es demanen juntament amb algunes més:

- **`help`**: Permet veure la llista de comandes amb l'eina Make que podem executar. 
- **`create-venv`**: Crea un entorn virtual `venv/` (si no existeix).  
- **`install`**: Instal·la les dependències de `requirements.txt` dins `venv`.
- **`run-ex1`**, `run-ex2`, ..., `run-ex5`: Executa `main.py` amb l’exercici corresponent.  
- **`run-all`** : Executa tots els exercicis de forma seqüencial (ex1...ex5) del `main.py`.
- **`tests`**: Executa tests amb `unittest discover`.  
- **`test-suite`**: Executa `tests/test_suite.py`.  
- **`coverage-report`, `coverage-html`**: Relacionat amb l’ús de coverage.
- **`build-dist`**: Genera el paquet (`sdist` i `wheel`) a la carpeta `dist/` mitjançant `setup.py`.  
- **`install-dist`**: Instal·la el `.whl` generat (ex. `dist/*.whl`) dins `venv`.  
- **`docs`**: Genera documentació amb `pdoc` a la carpeta `docs_html/`.
- **`pylint`**: Comprova l’estil PEP8.  
- **`clean`**: Elimina fitxers de caché i coverage.

Si volem executar alguna comanda, només caldrà que fem:

```bash
make comanda
```
Per exemple, si volem llistar totes les comandes possibles per executar, farem:

```bash
make help
```

I si volem exeuctar el `main.py` perquè s'executin tots els exercicis, farem:

```bash
make run-all
```


## Com dur a terme l'execució i la instal·lació de l'entorn i els requeriments?

Per a una guia pas a pas (crear entorn virtual, instal·lar, executar exercici, tests i cobertures, etc.), consulta l’arxiu `INSTALL.md`. 
Allí s’explica detalladament com arrencar el projecte i com emprar el Makefile.

## Tests i cobertura

Els tests estan a la carpeta `tests/`. En aquesta hi trobarem un fitxer per cada exercici (`test_ex1.py`, etc.). Així mateix, també hi ha un `test_suite.py` que ens serveix per agrupar tot en una suite manual. 
A més a més, per calcular la cobertura dels testos, fem servir el paquet `coverage`.

## Generació de la documentació

Per generar documentació a partir dels docstrings (amb pdoc):

```bash
make docs
```

o manualment, des de la carpeta arrel del projecte:

```bash
pdoc modules/ main.py tests --output-dir docs
```

## Llicència

Aquest projecte es distribueix sota la `MIT License`, podeu trobar-hi més informació al fitxer `LICENSE` al projecte.


