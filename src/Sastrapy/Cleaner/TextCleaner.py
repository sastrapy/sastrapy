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

  def cleanEmoji(self, data):
    text = data
    if type(data) == list:
      text = ' '.join(data)
    pattern = re.compile("["
                         u"\U0001F600-\U0001F64F"  # emoticons
                         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                         u"\U0001F680-\U0001F6FF"  # transport & map symbols
                         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                         u"\U00002500-\U00002BEF"  # chinese char
                         u"\U00002702-\U000027B0"
                         u"\U00002702-\U000027B0"
                         u"\U000024C2-\U0001F251"
                         u"\U0001f926-\U0001f937"
                         u"\U00010000-\U0010ffff"
                         u"\u2640-\u2642"
                         u"\u2600-\u2B55"
                         u"\u200d"
                         u"\u23cf"
                         u"\u23e9"
                         u"\u231a"
                         u"\ufe0f"  # dingbats
                         u"\u3030"
                         "]+", flags=re.UNICODE)
    result = pattern.sub(r'', text)
    return result.split() if type(data) == list else ' '.join(result.strip().split())
