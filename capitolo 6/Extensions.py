favorite_languages = {
    'Patrizio' : ['python', 'powershell', 'php'],
    'Andrea' : ['Visual Basic', 'Python'],
    'Michele' : ['Cobol'],
    'Emanuele' : ['php', 'Python', 'bash'],
    'phil' : ['rust', 'go'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t- {language.title()}")