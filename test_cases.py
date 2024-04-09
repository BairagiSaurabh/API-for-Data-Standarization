from main import Data_Preprocess
import pandas as pd

df = pd.read_csv("Coffee_Qlty_By_Country.csv",na_values='Nan')
test = Data_Preprocess(df,"Coffee_Qlty_By_Country_trial")
test.run()  
