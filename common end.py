def common_end(a, b):
  x = a[0] == b[0]
  y = a[-1] == b[-1]
  return x or y
