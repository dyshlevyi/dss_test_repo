# -*- coding: utf-8 -*-
import dataiku
from dataiku import spark as dkuspark
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

# Read recipe inputs
Inline_dataset_prepared = dataiku.Dataset("Inline_dataset_prepared")
Inline_dataset_prepared_df = dkuspark.get_dataframe(sqlContext, Inline_dataset_prepared)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a SparkSQL dataframe
pyspark_test_df = Inline_dataset_prepared_df # For this sample code, simply copy input to output

# Write recipe outputs
pyspark_test = dataiku.Dataset("pyspark_test")
dkuspark.write_with_schema(pyspark_test, pyspark_test_df)
