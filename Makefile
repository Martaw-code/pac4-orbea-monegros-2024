# Makefile per al projecte PAC4 Orbea Monegros

PYTHON := python3
PIP := pip
COVERAGE := coverage
PYLINT := pylint

MODULES := modules/ main.py
TESTS_DIR := tests
DOCS_OUTPUT_DIR := docs

# Per a Windows, sovint cal fer "py -m pip" i "py -m python" en lloc de "pip" i "python".

.PHONY: help crea-venv install run-all run-ex1 run-ex2 run-ex3 run-ex4 run-ex5 tests test-suite build-dist install-dist docs coverage-html coverage-report zip pylint clean

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
	@echo "  make build-dist          -> Genera el paquet (sdist i wheel) a ./dist/"
	@echo "  make install-dist        -> Instal·la el wheel creat a ./dist/ (primer build-dist)"
	@echo "  make docs                -> Genera documentació amb pdoc"
	@echo "  make coverage-report     -> Mostra l'informe de cobertura en text"
	@echo "  make coverage-html       -> Genera l'informe HTML de cobertura (htmlcov/)"
	@echo "  make zip                 -> Genera el zip del projecte amb els fitxers essencials"
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
	    echo "Ara ja pots fer 'make install' per instal·lar dependències."; \
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


## ===========================
## Coverage
## ===========================
coverage-report:
	venv/bin/$(COVERAGE) run -m pytest tests/

coverage-html:
	venv/bin/$(COVERAGE) html


## ===========================
## Generar el paquet (sdist i wheel)
## ===========================
build-dist:
	@echo "Generant sdist i wheel a ./dist/..."
	venv/bin/$(PIP) install --upgrade pip
	venv/bin/$(PYTHON) setup.py sdist bdist_wheel


## ===========================
## Instal·lar el paquet generat al venv
## ===========================
install-dist:
	@echo "Instal·lant el paquet generat a ./dist/*.whl ..."
	venv/bin/$(PIP) install --upgrade pip
	venv/bin/$(PIP) install dist/pac4_orbea_monegros-0.1.0-py3-none-any.whl


## ===========================
## Generar documentació amb pdoc
## ===========================
docs:
	@echo "Generant documentació amb pdoc a $(DOCS_OUTPUT_DIR)/"
	venv/bin/pdoc $(MODULES) $(TESTS_DIR)  --output-dir $(DOCS_OUTPUT_DIR)


## ===========================
## PEP8 i pylint
## ===========================
pylint:
	@echo "Comprovant estil PEP8 amb pylint..."
	$(PYLINT) $(MODULES) $(TESTS_DIR)


## ===========================
## ZIP del projecte
## ===========================
zip:
	@echo "Creant zip del projecte..."
	zip -r pac4_orbea_monegros.zip . \
		-x "venv/*" \
		-x "dist/*" \
		-x "build/*" \
		-x "__pycache__/*" \
		-x ".git/*" \
		-x ".pytest_cache/*" \
		-x ".DS_Store" \
		-x "*.egg-info/*" \
		-x "htmlcov/*" \
		-x "docs/*"
	@echo "Arxiu pac4_orbea_monegros.zip creat amb èxit!"

## ===========================
## Neteja
## ===========================
clean:
	@echo "Eliminant fitxers d'entorn, caché, cobertura, docs, dist, zip, build..."
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*.pyc" -exec rm -f {} +
	find . -name "*.egg-info" -exec rm -rf {} +
	find . -name ".coverage" -exec rm -f {} +
	find . -name "venv" -exec rm -rf {} +
	find . -name "docs" -exec rm -rf {} +
	find . -name "dist" -exec rm -rf {} +
	find . -name "build" -exec rm -rf {} +
	find . -name "htmlcov" -exec rm -rf {} +
	find . -name "*.zip" -exec rm -rf {} +
