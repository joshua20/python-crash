#slicing a list

players=['charles', 'martina','florence','eli']

print(players)

print(f"3 players:\n\t {players[0:3]}")

print(f"player 2 to 4: \n\t {players[1:4]}")

#looping through a slice

print("these are the first 3 p;ayers from the my team")
for player in players[:3]:
    print( player)
