#obtaining guest names 
from pathlib import Path
guest=input("please enter your full name")

guest_store=Path("guest.txt")

guest_store.write_text(guest)
