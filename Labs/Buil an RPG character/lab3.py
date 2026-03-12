full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):

    if not isinstance(name, str):
        return 'The character name should be a string'

    if name == '':
        return 'The character should have a name'

    if len(name) > 10:
        return 'The character name is too long'

    if ' ' in name:
        return'The character name should not contain spaces'

    for stat in [strength, intelligence, charisma]:
        if not isinstance(stat, int):
            return 'All stats should be integers'

        if stat < 1:
            return 'All stats should be no less than 1'

        if stat > 4:
            return 'All stats should be no more than 4'

    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'

    verification = f'{name}' + '\n'
    verification += 'STR ' + full_dot * strength + (10 - strength) * empty_dot + '\n'
    verification += 'INT ' + full_dot * intelligence + (10 - intelligence) * empty_dot + '\n'
    verification += 'CHA ' + full_dot * charisma + (10 - charisma) * empty_dot

    return verification


print(create_character('ren', 4, 2, 1))