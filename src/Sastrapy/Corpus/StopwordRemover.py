import pathlib

class StopwordRemoverMachine():
  def __init__(self):
    path = pathlib.Path(__file__).parent.absolute()
    self.originalDictionaryPath = str(path) + '/Dictionary/stopwords.txt'
    self.dictionaryPath = self.originalDictionaryPath
    self.dictionary = []

    self.openDictionary()

  def openDictionary(self):
    stopwordData = open(self.dictionaryPath, 'r')
    self.dictionary = [word.rstrip().lower() for word in stopwordData.readlines()]
  
  def resetDictionary(self):
    self.dictionaryPath = self.originalDictionaryPath
    self.openDictionary()
  
  def importDictionary(self, path):
    self.dictionaryPath = path
    self.openDictionary()

  def removeStopword(self, data):
    self.data = data
    if type(self.data) == str:
      data = self.data.split()
    
    result = list(filter(None, [word.strip() if word.lower() not in self.dictionary else None for word in data]))
    return result if type(self.data) == list else ' '.join(result).strip()
