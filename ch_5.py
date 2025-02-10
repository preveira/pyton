def is_triangle(leng1, leng2, leng3):
  if leng1 > leng2 + leng3:
    print('No')
  else:
    if leng2 > leng1 + leng3:
      print('No')
    else:
      if leng3 > leng1 + leng2:
        print('No')
      else:
        print('Yes')

is_triangle(4, 5, 6)