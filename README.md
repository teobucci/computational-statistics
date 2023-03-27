<!-- omit from toc -->
# The price of uncertainty during COVID-19

![GitHub last commit](https://img.shields.io/github/last-commit/teobucci/computational-statistics?logo=github)

A sensitivity analysis on an extended infection model using [UQpy](https://github.com/SURGroup/UQpy/).

This project was developed for the course of **Computational Statistics** for the MSc. in Mathematical Engineering at Politecnico di Milano, A.Y. 2022/2023.

<!-- omit from toc -->
# Table of contents

- [Installation](#installation)
  - [How to clone the repository](#how-to-clone-the-repository)
  - [How to install the packages](#how-to-install-the-packages)
- [Analysis](#analysis)
- [Final results](#final-results)
- [Authors](#authors)


# Installation

## How to clone the repository

```
git clone https://github.com/teobucci/computational-statistics
```

## How to install the packages

Install the required packages using, for example, pip

```
pip install -r requirements.txt
```

# Analysis

The repository contains different folders, which are explained here. The main files are:

- [`main.ipynb`](./main.ipynb) is the main Jupyter Notebook for the project, which contains all the analysis and is completely independent.
- [`local_extSIR.py`](./local_extSIR.py) is the mathematical implementation of the Extended SIR model used for this project.

Other directories and files are:

- `UQpy` is a folder which contains some helpful material for getting started with `UQpy`.
- `Uncertainpy` is a folder which contains old and failed experiments using [Uncertainpy](https://github.com/simetenn/uncertainpy/), indeed this project initially aimed at using such library.
- `docs` is a folder which contains the paper used in this project.
- `figures` is a folder which contains images embedded in the Jupyter Notebook.
- `physics_models` is a folder which contains Jupyter Notebooks of simple physics model to be using for experimenting with `UQpy`.

# Final results

An exported PDF version of [`main.ipynb`](./main.ipynb) can be found here: [`main.pdf`](./output/main.pdf).

The final presentation can be found here: [`comp_stat_bucci_petruso.pdf`](./output/comp_stat_bucci_petruso.pdf).

# Authors

- Teo Bucci ([@teobucci](https://github.com/teobucci))
- Flavia Petruso ([@fl-hi1](https://github.com/fl-hi1))
