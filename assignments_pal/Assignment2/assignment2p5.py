#Soumya Pal
#Assignment 2 part 5

import time
import numpy as np

times = []

while True:
  check = input("Enter s to add a reaction time, or q to show your average and quit: ")
  if check == 'q':
    if len(times)>0:
      print(f"\nYour average after {len(times)} tries was:\n"+str(np.mean(times)))
      print("\nGoodbye!")
      break
    else:
      print("\nGoodbye!")
      break
  elif check == 's':
    time.sleep(np.random.uniform(3,5))
    start=time.time()
    key = input("\nHit Enter Now!\n")
    times.append(time.time() - start)


  else:
    print('Invalid selection!\n')
    continue