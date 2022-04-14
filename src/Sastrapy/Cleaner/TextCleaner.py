import re

class CleanerTextMachine:
  def __init__(self) -> None:
      pass
  
  def cleanNumber(self, data):
    text = data
    if type(data) == list:
      text = ' '.join(data)
    result = re.sub('[0-9]', ' ', text)
    return result.split() if type(data) == list else ' '.join(result.strip().split())
  
  def cleanUrl(self, data):
    text = data
    if type(data) == list:
      text = ' '.join(data)
    result = re.sub('(https://\w+.\w+/\w+)|(https://\w+.\w+)|(http://\w+.\w+/\w+)|(http://\w+.\w+)', ' ', text)
    return result.split() if type(data) == list else ' '.join(result.strip().split())
  
  def cleanHashtag(self, data):
    text = data
    if type(data) == list:
      text = ' '.join(data)
    result = re.sub('(#\w+)', ' ', text)
    return result.split() if type(data) == list else ' '.join(result.strip().split())
  
  def cleanMention(self, data):
    text = data
    if type(data) == list:
      text = ' '.join(data)
    result = re.sub('(@\w+)', ' ', text)
    return result.split() if type(data) == list else ' '.join(result.strip().split())
  
  def cleanSymbol(self, data):
    text = data
    if type(data) == list:
      text = ' '.join(data)
    result = re.sub('[\W_]', ' ', text)
    return result.split() if type(data) == list else ' '.join(result.strip().split())
  
  def deepClean(self, data):
    text = data
    if type(data) == list:
      text = ' '.join(data)
    result = self.cleanUrl(text)
    result = self.cleanNumber(result)
    result = self.cleanHashtag(result)
    result = self.cleanMention(result)
    result = self.cleanSymbol(result)
    return result.split() if type(data) == list else ' '.join(result.strip().split())
  
  def cleanCustom(self, pattern, data):
    text = data
    if type(data) == list:
      text = ' '.join(data)
    result = re.sub(pattern, ' ', text)
    return result.split() if type(data) == list else ' '.join(result.strip().split())
  
  def cleanSingleChar(self, data):
    text = data
    if type(data) == str:
      text = data.split()
    result = list(filter(None, [word.strip() if len(word) > 1 else None for word in text]))
    return result if type(data) == list else ' '.join(result)
  
  def cleanMinChar(self, data, mininumLength):
    text = data
    if type(data) == str:
      text = data.split()
    result = list(
        filter(None, [word.strip() if len(word) > mininumLength else None for word in text]))
    return result if type(data) == list else ' '.join(result)

    
