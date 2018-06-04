class LexerReader:
  reader = None
  unget_p = False
  ch = 0
  

  #---------------------------
  # コンストラクタ
  #
  # tw : TextIOWrapper
  #---------------------------
  def __init__(self, r):
    self.reader = r

  def read(self):
    if self.unget_p:
      self.unget_p = False
    else:
      self.ch = self.reader.read(1)
    
    return self.ch
  
  def unread(self,c):
    self.unget_p = True