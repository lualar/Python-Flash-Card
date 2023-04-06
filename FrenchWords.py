import pandas as pd

class cRandomWord():
    def __init__(self):
        #open file 
        try:
            #If user already played this app before and save its status
            self.dfFrenchWords = pd.read_csv("./data/words_to_learn.csv").to_dict(orient="records")
        except FileNotFoundError:
            self.dfFrenchWords = pd.read_csv("./data/french_words.csv").to_dict(orient="records")
        #print (f"French Words: {self.dfFrenchWords} - Count {len(self.dfFrenchWords)}")
       
    def dGetDict(self):
        return self.dfFrenchWords

    def fSaveWordsToLearn(self, dictWordsToLearn):
        pd.DataFrame.to_csv(pd.DataFrame.from_dict(dictWordsToLearn), "./data/words_to_learn.csv", index=False)




