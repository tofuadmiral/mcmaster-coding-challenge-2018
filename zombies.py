## make a zombie object
class Zombie:
    ## zombies know their x, y and distance from the human
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = (x**2 + y**2)**(1/2)

    def update(human):
        ## eight cases for movement
        if distance%1 == 1 and x == human.x and y > human.y:
            self.y -= 1
            self.distance = ((self.x-human.x)**2 + (self.y-human.y)**2)**(1/2)
        elif distance%1 == 1 and x == human.x and y < human.y:
            self.y += 1
            self.distance = ((self.x-human.x)**2 + (self.y-human.y)**2)**(1/2)
        elif distance%1 == 1 and x > human.x and y == human.y:
            self.x -= 1 
            self.distance = ((self.x-human.x)**2 + (self.y-human.y)**2)**(1/2)
        elif distance%1 == 1 and x < human.x and y == human.y:
            self.x += 1 
            self.distance = ((self.x-human.x)**2 + (self.y-human.y)**2)**(1/2)
        elif distance%1!=1 and x<human.x and y > human.y:
            self.x += 1
            self.y -= 1
            self.distance = ((self.x-human.x)**2 + (self.y-human.y)**2)**(1/2)
        elif distance%1!=1 and x>human.x and y > human.y:
            self.x -= 1
            self.y -= 1
            self.distance = ((self.x-human.x)**2 + (self.y-human.y)**2)**(1/2)
        elif distance%1!=1 and x>human.x and y < human.y:
            self.x -= 1
            self.y += 1
            self.distance = ((self.x-human.x)**2 + (self.y-human.y)**2)**(1/2)
        elif distance%1!=1 and x<human.x and y < human.y:
            self.x += 1
            self.y += 1
            self.distance = ((self.x-human.x)**2 + (self.y-human.y)**2)**(1/2)

## Make a human object
class Human:
    ## humans know their distance from the nearest zombie, x and y 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = 1

    ## update their distance from the nearest zombie and also move away from it
    def update(x, y, ):
        if distance%1 == 1 and x == zombie.x and y > zombie.y:
            self.y += 1
            self.distance = ((self.x-zombie.x)**2 + (self.y-zombie.y)**2)**(1/2)
        elif distance%1 == 1 and x == zombie.x and y < zombie.y:
            self.y -= 1
            self.distance = ((self.x-zombie.x)**2 + (self.y-zombie.y)**2)**(1/2)
        elif distance%1 == 1 and x > zombie.x and y == zombie.y:
            self.x += 1 
            self.distance = ((self.x-zombie.x)**2 + (self.y-zombie.y)**2)**(1/2)
        elif distance%1 == 1 and x < zombie.x and y == zombie.y:
            self.x -= 1 
            self.distance = ((self.x-zombie.x)**2 + (self.y-zombie.y)**2)**(1/2)
        elif distance%1!=1 and x<zombie.x and y > zombie.y:
            self.x -= 1
            self.y += 1
            self.distance = ((self.x-zombie.x)**2 + (self.y-zombie.y)**2)**(1/2)
        elif distance%1!=1 and x>zombie.x and y > zombie.y:
            self.x += 1
            self.y += 1
            self.distance = ((self.x-zombie.x)**2 + (self.y-zombie.y)**2)**(1/2)
        elif distance%1!=1 and x>zombie.x and y < zombie.y:
            self.x += 1
            self.y -= 1
            self.distance = ((self.x-zombie.x)**2 + (self.y-zombie.y)**2)**(1/2)
        elif distance%1!=1 and x<zombie.x and y < zombie.y:
            self.x -= 1
            self.y -= 1
            self.distance = ((self.x-zombie.x)**2 + (self.y-zombie.y)**2)**(1/2)
        
## define a function to find the nearest zombie 
closestats = [0]*3
def findNearestZombie(human, zomArray):
    lowestDistance = 10000000
    closeZom = Zombie(100000, 100000)
    for i in range(numZombies):
        if zomArray[i].distance < lowestDistance :
            closeZom = zomArray[i]
    closestats[0] = closeZom.x
    closestats[1] = closeZom.y
    closestats[2] = closeZom.distance
    return closestats

## find how many zombies we need
numZombies = int(raw_input())

## populate our array of zombies
zomArray = [Zombie(0,0) for i in range(numZombies)]

for i in range(numZombies):
    zomcoords = str.split(raw_input())
    zomx = int(zomcoords[0])
    zomy = int(zomcoords[1])
    zomArray[i] = Zombie(zomx, zomy)

    
## instantiate a human for our game
bean = Human(0, 0)
moves = 0
    
## now we have all our zombies, so loop while our human isn't caught
## human is caught if the distance is zero
while(bean.distance!=0):
    nearzomstats = findNearestZombie(bean, zomArray)
    nearzom = Zombie(nearzomstats[0], nearzomstats[1])
    bean.update(nearzom)
    for i in range(numZombies):
        zomArray[i].update(bean)
    moves += 1

## print our moves
if moves == 1:
    print "never"
elif moves > 1:
    print moves
    

    