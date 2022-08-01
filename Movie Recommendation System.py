
from GenerateData import IMBD
import pandas as pd

Imbd = IMBD()
# moviee = Imbd.GetMovie(2)

moviee = pd.read_csv('Movie_Data.csv')
# print(moviee.head())


