# PAC4 - Orbea Monegros 2024

Aquest projecte és la PAC4 de l'assignatura "Programació per a la Ciència de Dades", on s'analitza un dataset de l'Orbea Monegros 2024. El codi està empaquetat com un mòdul de Python, i inclou:

- **Anàlisi de dades** i neteja (Ex1, Ex2, Ex3, Ex4, Ex5).
- **Estructura de mòduls** amb tests unitaris i cobertura.
- **Llicència MIT** i fitxers de configuració (`setup.py`, `requirements.txt`).
- **Documentació** al `README` i un fitxer `INSTALL.md` amb instruccions addicionals.

## Estructura del projecte

- **`setup.py`**: Fitxer de configuració per empaquetar el projecte com a llibreria instal·lable.
- **`requirements.txt`**: Llista de dependències de Python.
- **`LICENSE`**: Llicència MIT.
- **`INSTALL.md`**: Explicació detallada de com configurar l'entorn, instal·lar i executar.
- **`main.py`**: Punt d'entrada principal, crida les funcions dels exercicis.
- **`modules/`**: Carpeta amb els mòduls (ex1.py, ex2.py, etc.).
- **`tests/`**: Carpeta amb tests unitaris (test_ex1.py, test_ex2.py, ...).
- **`data/`**: Carpeta amb el dataset (p. ex. `dataset.csv`).
- **`img/`**: Carpeta on es genera l’histograma o altres imatges.

## Instal·lació ràpida

1. **Opció 1**: Fer servir `pip install .` (explicat en detall a [INSTALL.md](INSTALL.md)).
2. **Opció 2**: Fer servir directament `pip install -r requirements.txt` i executar `main.py` manualment.

## Execució

- **Per defecte** (sense paràmetres), `main.py` executa tots els exercicis en ordre (Ex1 → Ex2 → Ex3 → Ex4 → Ex5):

  ```bash
  python main.py
