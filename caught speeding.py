def caught_speeding(speed, is_birthday):
  intspeed = int(speed) - (5 if is_birthday else 0)
  if intspeed <=60:
    return 0
  elif intspeed <=80:
    return 1
  elif intspeed >=81:
    return 2
  else:
    return
