def read_into_array(path):
  arr = []
  with open(path, 'r') as f:
    arr = f.readlines()
    arr = map(lambda x : x.replace('\n', ''), arr)
  return list(arr)