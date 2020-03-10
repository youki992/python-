import re
def is_matched(addr):
  if re.match(r'[0-9\_]+',addr)!=None:
      print('matched')
  else:
      print('match error')
is_matched('__')
is_matched('29')
is_matched('_004')
is_matched('')
is_matched('D')