# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE_MAGIC_CELL
# Automatically replaced inline charts by "no-op" charts
# %pylab inline
import matplotlib
matplotlib.use("Agg")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
from dataiku import pandasutils as pdu
import pandas as pd

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
from cmdstanpy import cmdstan_path, CmdStanModel
# import cmdstanpy

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
posterior = CmdStanModel(stan_file = "/home/centos/dina_independent.stan")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import os, os.path
print("==== DEBUG: ENVIRONMENT")
for v in sorted(os.environ):
    print(v + " => " + os.environ[v])
print("==== CMDSTAN_DIR: " + os.path.expanduser(os.path.join('~', '.cmdstan')))

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Recipe outputs
cmdstan = dataiku.Dataset("cmdstan")
cmdstan.write_with_schema(pandas_dataframe)