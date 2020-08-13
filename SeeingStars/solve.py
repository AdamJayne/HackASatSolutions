import numpy
import matplotlib
import matplotlib.pyplot as plt

puzzle = open('values.txt').read().split("\n")

stars = []


for y, line in enumerate(puzzle):
  stars.append([])
  mylist = list(map(lambda v: int(v), line.split(',')));
  for x, value in enumerate(mylist):
    stars[y].append(value)
    # if value == 255 and value > mylist[x+1]:
    #   stars.append((x, y))
    #   break

# with open('stars.txt', 'w+') as f:
#   for star in stars:
#     f.write(f'{star[0]},{star[1]}\n')
#   f.write('\n')

report = numpy.array(stars)

fig, ax = plt.subplots()
im = ax.imshow(report, cmap=plt.get_cmap('gray'))

plt.show()

# ticket{quebec33113juliet:GMpb46SCGfGB1lr2aj799x0C1xA2XYXHipKc5ZrCVXdfcyXPqCVeNFBBi4_nzi2oYg}