def uses_none(word, forbidden):
  for letter in word.lower():
      if letter in forbidden.lower():
        return False 

  return True

print(uses_none('banana', 'xyz'))
print(uses_none('apple', 'efg'))

def uses_only(word, available):
  for letter in word.lower():
    if letter not in available.lower():
      return False
  return True
      
print(uses_only('apple', 'apl'))
print(uses_only('banana', 'ban'))

def uses_all(word, required):
  for letter in required.lower():
    if letter not in word.lower():
      return False
  return True

print(uses_all('banana', 'nab'))
print(uses_all('apple', 'ipa'))


#check if the word length is long enough
#check if word contains only characters from (available) letters
#check if word contains required letter
#if all of these are True then return True
def check_word(word, available, required):
  if len(word) < 4:
    return False
  for letter in word.lower():
    if letter not in available.lower():
      return False
  for letter in required.lower():
    if letter not in word.lower():
      return False
  return True

print(check_word('color', 'ACDLORT', 'R'))
print(check_word('told', 'ACDLORT', 'R'))