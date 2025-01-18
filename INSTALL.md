# Guia d'Instal·lació i Execució

A continuació, es presenta una guia pas a pas per instal·lar, executar i comprovar totes les funcionalitats de la PAC4 Orbea Monegros 2024.

La guia que es presenta està pensada per facilitar a l'usuari l'execució i l'escriptura de comandes a la terminal i automatitzar-ho mitjançant l'execució de comandes amb l'eina `make`. 

Aquestes comandes es troben declarades al `Makefile`.

La guia que es presenta a continuació, té el propòsit de ser seguida de forma seqüencial fins a la secció 3, per tal de poder:

1. Crear l'entorn virtual
2. Un cop creat l'entorn, activar-lo per tal de poder instal·lar-hi els paquets necessàris.
3. Instal·lar els paquets del fitxer `requirements.txt` a l'entorn virtual.

## 1. Crear l'entorn virtual

En primer lloc, des de la carpeta arrel del projecte (on hi ha el `Makefile`), executarem:

```bash
make crea-venv
```

Aquesta comanda, ens permetrà crear l'entorn virtual en el directori `venv/` si aquest no existeix. 
Això es fa així, per tal de facilitar a l'usuari la creació de l'entorn. A més, aquesta comanda, també dóna instruccions a l'usuari perquè depenent del seu SO activi l'entorn que s'ha acabat de crear per poder instal·lar els paquets.

## 2. Activa l’entorn virtual:

Ara s'explica com activar l'entorn en funció del teu SO:

### Linux/Mac

```bash
source venv/bin/activate
```

### Windows

```bash
.\venv\Scripts\Activate.ps1
```

Un cop activat, es mostrarà al *prompt* de la terminal l'entorn activat, en el nostre cas, `(venv)`, al principi.

## 3. Instal·lar dependències

```bash
make install
```

Això executa `pip install -r requirements.txt` dins de l'entorn virtual creat `(venv)` i instal·la tots els paquets necessaris per aquesta PAC4.

## 4. Executar els exercicis

Per tal d'executar de forma senzilla els exercicis els proveeixen dues comandes definides al `Makefile`:

Per una banda si volem executar tots els exercicis:

### Tots els exercicis

Per facilitar l'execució del `main.py` i que s'executin tots els exercicis (ex1...ex5) de forma seqüencial executarem la comanda:

```bash
make run-all
```

Notem que per defecte, s'ha definit que el `main.py` pot rebre l’opció `--exercise exN`, sent N el nombre de l'exercici a executar o bé `--exercise all` si els volem executar tots de forma seqüencial. Tot i això, per tal d'abstraure a l'usuari, es proporciona la comanda definida anterioment.

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

Hem definit un test per cada exercici, com així mateix un test pel `main.py` i aixñi mateix una `suite`de testos que els aglutina tots (tants els dels exercicis, com el del main)

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

A partir del paquest `coverage`, aquest ens proporciona una eina que mesura quantes línies del nostre codi han estat executades (o “cobertes”) durant l’execució dels tests.
Això ens permet veure quines parts del projecte tenen tests que verifiquen el seu comportament i quines parts romanen sense provar. 
Primer generem la cobertura en format text:

```bash
make coverage-report
```
I a continuació, genera un informe HTML a `htmlcov/`. 
Si s'obre `htmlcov/index.html` es poden veure les línies cobertes i les que no:

```bash
make coverage-html
```

Notar, a partir del test de cobertura, hem pogut veure que en total hem cobert un 99% del codi. No s'ha assolit el 100% ja que en el cas del fitxer de `test_suite.py`, no queden cobertes i probades les seves línies, ja que aquest test precisament prova els altres tests.

## Generació del paquet `pac4-orbea-monegros` i instal·lació del mateix

En aquesta secció s'explica com crear i instal·lar el paquet Python que hem definit al projecte, i com fer-lo servir a partir de l’entry point que s'ha configurat a setup.py. Concretament:

### Build (sdist i wheel)

S’executen les ordres de setup.py (`sdist` i `bdist_wheel`) que generen a la carpeta dist/ els fitxers de distribució: 
- **.tar.gz (source distribution)**
- **.whl (wheel)**

Aquest pas és per compilar i empaquetar el codi en un format instal·lable.

```bash
make build-dist
```

### Instal·lar el wheel generat

S’instal·la el fitxer `.whl` dins l’entorn virtual `(venv)`. 
Això significa que ara el paquet `pac4-orbea-monegros` està disponible a Python com qualsevol llibreria que hàgim instal·lat via `pip`.

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

Aquest, executa directament la funció `main()` del fitxer `main.py`, passant-li el paràmetre `--exercise ex2`.
També podríem fer `--exercise all` per executar tots els exercicis alhora.

Addicionalment, un cop instal·lat el paquet, si volem obtenir la seva informació (versions, dependències, directori d’instal·lació, etc.), podem executar la següent comanda:

```bash
python3 -m pip show pac4-orbea-monegros
```

## Generar la documentació

Genera la documentació a la carpeta `docs` en forma de documentació HTML. Si obrim l'`index.html` podrem consultar-la:

```bash
make docs
```

## Netejar fitxers i carpetes

Si algun pas de l'instal·lació o generació de fitxers o del paquet no ha sigut satisfactoria, s'aconsella executar la comanda:

```bash
make clean
```
que ens permet esborrar les carpetes i els fitxers següents:

- Carpetes de caché (__pycache__)
- Fitxers `.pyc`, `.egg-info` i `.coverage` 
- Carpeta `dist/`, `build/`, `docs`, `venv/` i `htmlcov`
- Zip del projecte `pac4_orbea_monegros.zip`
