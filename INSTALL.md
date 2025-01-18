# Guia d'Instal·lació i Execució

A continuació, es presenta una guia pas a pas per instal·lar, executar i comprovar totes les funcionalitats de la PAC4 Orbea Monegros 2024.

La guia que es presenta està pensada per facilitar a l'usuari l'execució i l'escriptura de comandes a la terminal i automatitzar-ho mitjançant l'execució de comandes amb l'eina `make`. Aquestes comandes es troben declarades al `Makefile`

## 1. Crear i activar l'entorn virtual

En primer lloc, de la carpeta arrel del projecte (on hi ha el `Makefile`), en executa:

```bash
make crea-venv
```

Que ens permetrà crear l'entorn virtual en el directori `venv/` si aquest no existeix. Això es fa així, per tal de facilitar a l'usuari la creacio de l'entorn. A més, aquesta comanda, també dóna les instruccions a l'usuari perquè depenent del seu SO activi l'entorn que s'ha acabat de crear.

## 2. Activa l’entorn virtual:

### Linux/Mac

```bash
source venv/bin/activate
```

### Windows

```bash
.\venv\Scripts\Activate.ps1
```

Un cop activat, es mostrarà al *prompt* de la terminal `(venv)` al principi.

## 3. Instal·lar dependències

```bash
make install
```

Això executa `pip install -r requirements.txt` dins de l'entorn virtual creat (venv) i instal·la tots els paquets necessaris per aquesta PAC4.

## 4. Executar els exercicis

### Tots els exercicis

Per facilitar l'execució del `main.py` i que s'executin tots els exercicis (ex1...ex5) de forma seqüencial executarem la comanda:

```bash
make run-all
```

Notem que per defecte, s'ha definit que el `main.py` pot rebre l’opció `--exercise exN`, sent N el nombre d'exercici a executar o bé `--exercise all` si els volem executar tots. Tot i això, per tal d'abstraure a l'usuari, es proporciona la comanda definida anterioment.

### Execució separada dels exercicis

Si es vol executar algún exercici en concret, ho farem de la següent manera:

```bash
make run-ex1
make run-ex2
make run-ex3
make run-ex4
make run-ex5
```

## Execució de tests i cobertura

### Tests

```bash
make tests
```
Ens permet executar tots els tests definits a la carpeta `tests/`.

I per tal d'executar la suite de testos, `test_suite.py`, ho podem fer amb la comanda:

```bash
make test-suite
```

### Cobertura

Per tal de generar l'informe de la cobertura dels tests de tot el codi i mostrar-la en format `html`, ho podem fer de la següent manera:

Primer generem la cobertura en format text:

```bash
make coverage-report
```
I a continuació, genera un informe HTML a `htmlcov/`. 
Si s'obre `htmlcov/index.html` es poden veure les línies cobertes i les que no:

```bash
make coverage-html
```

## Generar el paquet i instal·lar-lo

### Build (sdist i wheel)

```bash
make build-dist
```

### Instal·lar el wheel generat

Instal·la el `.whl` del paquet generat a dins del nostre entorn `venv`: 

```bash
make install-dist
```
    
Un cop instal·lat, podem fer el següent, ja que s'ha definit al fitxer `setup.py` l`'entry_point` de forma adequada:

```bash
orbeamonegros --exercise ex2
```

Que ens permetrà executar qualsevol exercici si l'especifiquem de forma anàlega a com ho hem fet amb la comanda anterior, o si els volem executar tots:

```bash
orbeamonegros --exercise all
```

I un cop instal·lat el paquet, si volem obtenir la seva informació, podem executar la següent comanda:

```bash
python3 -m pip show pac4-orbea-monegros
```

## Generar la documentació

Genera la documentació a la carpeta `docs` en forma de documentació HTML. Si obrim l'`index.html` podrem consultar-la:

```bash
make docs
```

## Netejar fitxers i carpetes

Si algun pas de l'instal·lació o generació de fitxers o del paquet no ha sigut satisfactori, s'aconsella executar la comanda:

```bash
make clean
```
que ens permet esborrar les carpetes i els fitxers següents:

- Carpetes de caché (__pycache__)
- Fitxers `.pyc`, `.egg-info` i `.coverage` 
- Carpeta `dist/`, `build/`, `docs`, `venv/` i `htmlcov`
