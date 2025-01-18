from setuptools import setup, find_packages

setup(
    name="pac4-orbea-monegros",
    version="0.1.0",
    description="PAC4 - Orbea Monegros 2024: Anàlisi de dades de la cursa.",
    author="Marta Granero I Martí",
    author_email="martagraneroi@uoc.edu",
    url="https://github.com/martaw-code/orbea-monegros-2024",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.12",
    install_requires=[
        "pandas",
        "matplotlib",
        "Faker",
        "coverage",
        "pylint",
        "setuptools",
        "pdoc"
    ],
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