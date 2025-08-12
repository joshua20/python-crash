#a dictionary of similar objects

favorite_languages={
        'jane':'Python',
        'sarah':'C',
        'edwin':'Rust',
        'james':'Ruby'
        }

language=favorite_languages['sarah'].title()

print(f"Sarah' favorite language is {language}")

print(favorite_languages['sarah'])

#using the get() to extract values from dictionaries

language_value=favorite_languages.get('javascript','langauge does not exist')

print("getting values from dicts using the get()")
print(language_value)


