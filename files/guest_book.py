#writing a guest book
from pathlib import Path
users=[]
while True:
    user=input("please enter you name  ")
    users+=user

    
for user in users:
    guest_book=Path("guest_book.txt")
    guest_book.write_text()


