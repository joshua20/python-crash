#starting with an empty dictionary


alien_0={}

alien_0['color']='green'
alien_0['points']=5

print(alien_0)


#changing the value of a dictionry

print(f"the color of the alien is {alien_0['color']}")

alien_0['color']='yellow'

print(f"the color of the alien has changed to {alien_0['color']}")

alien_0['x_position']=0
alien_0['y_position']=25
alien_0['speed']='medium'

#determine how far an alien can move based on its current speed

if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    #this must be a fast alien
    x_increment=3

alien_0['x_position']=alien_0['x_position'] + x_increment

print(f"the new alien is at new x_position \n {alien_0}")


#removing key-value pairs from a dictionary

print(alien_0)

del alien_0['points']

print(f" the new alien after deleting 'points'\n\t{alien_0}")

