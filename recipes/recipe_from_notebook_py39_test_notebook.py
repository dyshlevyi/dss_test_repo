# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE_MAGIC_CELL
# Automatically replaced inline charts by "no-op" charts
# %pylab inline
#import matplotlib
#matplotlib.use("Agg")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
#import dataiku
#from dataiku import pandasutils as pdu
#import pandas as pd

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
from dataiku import pandasutils as pdu
import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import  GridSearchCV
from sklearn.metrics import precision_score, recall_score, f1_score, roc_curve, cohen_kappa_score, roc_auc_score, accuracy_score, classification_report, auc, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  LabelBinarizer

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Recipe outputs
#lightgbm_tls_issue = dataiku.Dataset("lightgbm_tls_issue")
#lightgbm_tls_issue.write_with_schema(pandas_dataframe)