def in1to10(n, outside_mode):
  # see if its in range(1,10)
  # if True returns True
  # if False returns False
  # unless outside_mode is True
    if not outside_mode:
        return (n>=1 and n<=10)
    else:
        return (n<=1 or n>=10)
