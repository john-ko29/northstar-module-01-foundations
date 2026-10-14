## What is this?

Module 1 Project: The NorthwoodFresh Southeast Diagnosis 

Client: NorthwoodFresh 

Prototyping the analysis methodology on a synthetic dataset that has the same shape and the same expected pattern.

## What's in the folder?

README.md - Explaining the purpose, files and reproducing the analysis

generate_northwoodfresh_data.py - Python script that creates a synthetic dataset for NorthFresh, containing three columns: Region, month, and revenue. 

northwoodfresh_sales.csv - synthetic dataset created by running generate_northwoodfresh_data.py

northwoodfresh_analysis.ipynb - Jupyter file that runs statistic summary on the dataset from northwoodfresh_sales.csv 

sven_anderson_memo.md - markdown explaining the results of the statistic summary from northwoodfresh_analysis.ipynb

## How to reproduce the analysis

activate the conda env, run the generation script, open the notebook, run it top to bottom.

## The headline finding

Finding the Effect Size = $108334.94 at a 22.95% drop. 

At a 95% CI, the true drop could between $84,552.95 to $132,116.93.

With the p-value at 0.0000044, the chance of this drop appearing by chance is extremely unlikely. A zero difference is not included which agrees wit the p-value