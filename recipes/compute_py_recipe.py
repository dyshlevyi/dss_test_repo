# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
split_party_democrat = dataiku.Dataset("split_party_democrat")
split_party_democrat_df = split_party_democrat.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

py_recipe_df = split_party_democrat_df # For this sample code, simply copy input to output


# Write recipe outputs
py_recipe = dataiku.Dataset("py_recipe")
py_recipe.write_with_schema(py_recipe_df)
