from main import Data_Preprocess
import pandas as pd

df = pd.read_csv("project_donor.csv",na_values='Nan')
test = Data_Preprocess(df,"project_donor_processed")
test.run()

