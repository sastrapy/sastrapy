import pathlib


class SlangConverterMachine():
    def __init__(self):
        path = pathlib.Path(__file__).parent.absolute()
        self.originalDictionaryPath = str(path) + '/Dictionary/slang.txt'
        self.dictionaryPath = self.originalDictionaryPath
        self.dictionary = {}

        self.openDictionary()

    def openDictionary(self):
        dictionary = open(self.dictionaryPath, 'r')
        self.dictionary = {word.rstrip().lower().split(';')[0]: word.rstrip(
        ).lower().split(';')[1] for word in dictionary.readlines()}

    def resetDictionary(self):
        self.dictionaryPath = self.originalDictionaryPath
        self.openDictionary()

    def importDictionary(self, path):
        self.dictionaryPath = path
        self.openDictionary()
    
    def convertSlang(self, data):
      self.data = data
      if type(self.data) == str:
        data = self.data.split()
      
      result = list(filter(None, [self.dictionary[word.strip().lower()] if word.strip().lower() in self.dictionary else word for word in data]))
      return result if type(self.data) == list else ' '.join(result).strip()
