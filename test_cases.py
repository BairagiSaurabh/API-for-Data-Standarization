from main import Data_Preprocess

import pandas as pd
import feature_engine
import numpy as np
#import streamlit as st
import pandas as pd
import dtale
from sklearn.model_selection import train_test_split
from feature_engine.imputation import (
    MeanMedianImputer,
    CategoricalImputer,
    ArbitraryNumberImputer
)
from feature_engine.encoding import WoEEncoder
from feature_engine.selection import DropConstantFeatures
from feature_engine.creation import CyclicalFeatures
from feature_engine.encoding import OneHotEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from feature_engine.encoding import CountFrequencyEncoder
from feature_engine.selection import DropCorrelatedFeatures
from feature_engine.outliers import Winsorizer, ArbitraryOutlierCapper, OutlierTrimmer
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("project_donor.csv",na_values='Nan')
test = Data_Preprocess(df,"project_donor_processed")
test.run()

# company_id,refund_date,party_regdate