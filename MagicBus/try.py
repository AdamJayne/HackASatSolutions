challenge = open('stuff.txt').read().split('.')
starters = set()
for line in challenge:
  starters.add(line[:3])
  for char in line[1:-1].split("+"):
    bytesobj = bytes.fromhex()

