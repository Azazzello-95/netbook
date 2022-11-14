import pandas as pd
import os
import dtoResource as  dto
class csv_book:
    phat= "resource/book.csv"
    df: pd.DataFrame
    flag_index = 0
    def __init__(self):
          self.df = self._create_df()

    def _create_df(self):
        if os.path.exists(self.phat):
            print("create_db find phat")
            self.flag_index = 1
            return pd.read_csv(self.phat)
        else:
            return pd.DataFrame(columns=['titolo','autore','descrizione'])

    def add_record(self, book:dto.Book_DTO ):
       dict ={'titolo':book.title,'autore':book.autor,'descrizione': book.description}
       series = pd.Series(dict)
       self.df = pd.concat([self.df, series.to_frame().T], ignore_index=True)


    def save(self):
        if self.flag_index == 0:
         self.df.to_csv(self.phat)
        else:
            self.df.to_csv(self.phat,index=False)