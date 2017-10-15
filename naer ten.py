def near_ten(num):
  if (num % 10) <=2:
    return True
  elif (10-(num%10)) <=2:
    return True
  else:
    return False
