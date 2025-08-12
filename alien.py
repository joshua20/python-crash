#a simple dictionary

alien_0={

        'color':'green',
        'points':5,

        }
print(alien_0)

print(alien_0['color'])
print(alien_0['points'])

#incase you kill the alien you gain 5 points

new_points=alien_0['points']

print(f"you just earned: {new_points} points!")

#adding new key-value pairs

alien_0['x_position']=0
alien_0['y_position']=25

print(f"the new alien_0: \n\t {alien_0}")

