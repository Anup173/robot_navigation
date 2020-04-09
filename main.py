import process_image
import random

occupied_grids, planned_path, obstacles = process_image.main("test_images/test_" +str(random.randrange(1,20,1))+ ".png")

print ("Obstacle Grids : ")
print (obstacles)
print ("Planned Path :")
print (planned_path)