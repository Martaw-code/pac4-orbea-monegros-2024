import os
from setuptools import setup, find_packages

def parse_requirements(file_path: str):
    """
    Llegeix el fitxer de requirements (requirements.txt) i en retorna
    una llista de dependències sense comentaris ni línies buides.
    """
    with open(file_path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    reqs = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            reqs.append(line)
    return reqs

requirements = parse_requirements("requirements.txt")

setup(
    name="pac4-orbea-monegros",
    version="0.1.0",
    description="PAC4 - Orbea Monegros 2024: Anàlisi de dades de la cursa.",
    author="Marta Granero I Martí",
    author_email="martagraneroi@uoc.edu",
    url="https://github.com/martaw-code/pac4-orbea-monegros-2024",
    license="MIT",
    packages=find_packages(),
    py_modules=["main"],
    python_requires=">=3.12",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "orbeamonegros=main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="orbea monegros python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
)