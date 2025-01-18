# Makefile per al projecte PAC4 Orbea Monegros

# Variables
PYTHON := python3
PIP := pip
COVERAGE := coverage
PYLINT := pylint

MODULES := modules/ main.py
TESTS_DIR := tests

# Per a Windows, sovint cal fer "py -m pip" i "py -m python" en lloc de "pip" i "python".

.PHONY: help install run-all run-ex1 run-ex2 run-ex3 run-ex4 run-ex5 tests test-suite pylint clean

## ===========================
## Ajuda
## ===========================
help:
	@echo "=== Makefile PAC4 Orbea Monegros ==="
	@echo "Comandes disponibles:"
	@echo "  make crea-venv           -> Crea l'entorn virtual (venv/) si no existeix"
	@echo "  make install             -> Instal·la dependències dins l'entorn virtual (requirements.txt)"
	@echo "  make run-all             -> Executar tots els exercicis (ex1..ex5) amb main.py"
	@echo "  make run-ex1             -> Executar l'exercici 1"
	@echo "  make run-ex2             -> Executar l'exercici 2"
	@echo "  make run-ex3             -> Executar l'exercici 3"
	@echo "  make run-ex4             -> Executar l'exercici 4"
	@echo "  make run-ex5             -> Executar l'exercici 5"
	@echo "  make tests               -> Executar tots els tests unitaris"
	@echo "  make test-suite          -> Executem la suite de testos"
	@echo "  make coverage           -> Executa coverage (grava dades)"
	@echo "  make coverage-report     -> Mostra l'informe de cobertura en text"
	@echo "  make coverage-html       -> Genera l'informe HTML de cobertura (htmlcov/)"
	@echo "  make pylint              -> Comprovar estil (PEP8) amb pylint"
	@echo "  make clean               -> Netejar fitxers innecessaris (cache, coverage, etc.)"


## ===========================
## Creació de l'entorn virtual
## ===========================
crea-venv:
	@if [ ! -d "venv" ]; then \
	    echo "Creant entorn virtual a ./venv ..."; \
	    $(PYTHON) -m venv venv; \
	    echo "Entorn creat. Per activar-lo, fes:"; \
	    echo " - Linux/Mac: source venv/bin/activate"; \
	    echo " - Windows (Powershell): .\\venv\\Scripts\\Activate.ps1"; \
	    echo "Després pots fer 'make install' per instal·lar dependències."; \
	else \
	    echo "L'entorn virtual ja existeix a ./venv. No fem res."; \
	fi


## ===========================
## Instal·lació de dependències
## ===========================
install:
	@echo "Instal·lant dependències de requirements.txt dins l'entorn virtual..."
	@echo "Recorda activar l'entorn virtual abans de fer make install."
	venv/bin/$(PIP) install -r requirements.txt

## ===========================
## Execució del projecte
## ===========================
run-all:
	@echo "Executant tots els exercicis (ex1..ex5)..."
	$(PYTHON) main.py --exercise all

run-ex1:
	@echo "Executant l'exercici 1..."
	$(PYTHON) main.py --exercise ex1

run-ex2:
	@echo "Executant l'exercici 2..."
	$(PYTHON) main.py --exercise ex2

run-ex3:
	@echo "Executant l'exercici 3..."
	$(PYTHON) main.py --exercise ex3

run-ex4:
	@echo "Executant l'exercici 4..."
	$(PYTHON) main.py --exercise ex4

run-ex5:
	@echo "Executant l'exercici 5..."
	$(PYTHON) main.py --exercise ex5


## ===========================
## Tests i Suite de Tests
## ===========================
tests:
	@echo "Executant tests unitaris amb unittest..."
	$(PYTHON) -m unittest discover $(TESTS_DIR)

test-suite:
	@echo "Executant la suite de test personalitzada..."
	$(PYTHON) -m tests.test_suite

coverage-report:
	venv/bin/$(COVERAGE) run -m pytest tests/

coverage-html:
	venv/bin/$(COVERAGE) html


## ===========================
## PEP8 i pylint
## ===========================
pylint:
	@echo "Comprovant estil PEP8 amb pylint..."
	$(PYLINT) $(MODULES) $(TESTS_DIR)


## ===========================
## Neteja
## ===========================
clean:
	@echo "Eliminant fitxers de caché i cobertura..."
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*.pyc" -exec rm -f {} +
	find . -name "*.egg-info" -exec rm -rf {} +
	find . -name ".coverage" -exec rm -f {} +
