import ndjson
import dtoResource as  dto
import csv_book




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   # nltk.download('names')
   #files = data_utils.download_wiki(language="en", target_dir="./enwiki_dump")
   with open('resource/enwiki_books.ndjson') as f:
      jsonFormat = ndjson.load(f)

  # print(jsonFormat[1][1])
   csvOut=csv_book.csv_book()
   for item in jsonFormat:
        book = dto.pass_list(item)
        csvOut.add_record(book)

   csvOut.save()


