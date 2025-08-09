#removing prefixxes in strings

url="https://www.ksa.go.ke"

print(url)
remove_preffix= url.removeprefix("https://")

print(f"the new url is {remove_preffix}")
