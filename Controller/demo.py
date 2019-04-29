from Modules.Main import Main
from Modules.DatabaseConnector import DatabaseConnector as db


def executeScriptsFromFile(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            db.run(command)
            print('command executed')
        except:
            print('command failed')

executeScriptsFromFile('test/no.sql')

print('************************************************')
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

input = {}
output = Main.login(input)
print(output)

print('#######')

input = {'username':'oi', 'password':'oi'}
output = Main.login(input)
print(output)

print('#######')

input = {'username':'username_01', 'password':'password_01'}
output = Main.login(input)
print(output)