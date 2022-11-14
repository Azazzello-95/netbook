
PLOT_SPACE= " == Plot == "
PLOT ="==Plot=="


def pass_list(l:[str]):
      desc:str=l[1]
      if (PLOT in desc):
          print(l[0])
          desc= desc.split(PLOT)[1]
      elif PLOT_SPACE in desc :
          desc= desc.split(PLOT_SPACE)[1]
      else:
          desc = l[1].split("==Contents==")[0]
      desc = desc.split("==")[0]
      return  Book_DTO(l[0],desc,l[2][2])



class Book_DTO:
 title: str
 description:str
 autor: str
 type: str

 def __init__(self, title:str , description:str ,autor: str):
     self.title= title
     self.description=description
     self.autor=autor




 def print_book(self):
     print("title:" + self.title+" autor:"+self.autor, " desc"+self.description)