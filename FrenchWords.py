import pandas as pd

class cRandomWord():
    def __init__(self):
        self.dfFrenchWords = pd.read_csv("./data/french_words.csv").to_dict(orient="records")
        print (f"French Words: {self.dfFrenchWords}")
       
    def dGetDict(self):
        return self.dfFrenchWords




