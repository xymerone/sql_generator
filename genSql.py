import re, pyperclip as pc
def addSqlRow(nm,tp):
    sqlRow = '`'+str(nm)+'`'
    if tp == 'v':
        sqlRow += ' VARCHAR(250) NOT NULL DEFAULT \'\' '
    elif tp == 'i':
        sqlRow += ' INT NOT NULL '
    elif tp == 't':
        sqlRow += ' TEXT '
    elif tp == 'd':
        sqlRow += ' DATETIME '
    else:
        return false
    return sqlRow + ', \n'
print("Генератор sql запитів створення таблиці.")
print('--------------------------------------------------------')
nameFile = input('ім\'я таблиці та файлу: ')
nameFile = nameFile + '.sql'
f = open(nameFile,'w')
print('Доступні типи:\n v(varchar(250)),\n i(int),\n t(text),\n d(datatime).')
print('Формат ім\'я колонки(тип) розділино комою, наприклад name(v), age(i)')
colum = input(': ')
arr = colum.split(',')
pat = r"(\w+)\((\w+)\)"
nameTable = nameFile.replace('.sql','')
f.write("CREATE TABLE IF NOT EXISTS `"+nameTable+"` ( \n")
f.write("`id` INT NOT NULL AUTO_INCREMENT, \n")
for col in arr:
    col = col.lower()
    col = col.strip()
    m = re.match(pat,col)
    f.write( addSqlRow( m.group(1), m.group(2) ) )
f.write(" PRIMARY KEY(`id`) \n )")
f.close()
print("Завершено!! Сгенеровано "+nameFile+" у папці цього скрипту.")
print("Результат генерації sql запиту на створення таблиці: ")
sql = open(nameFile,'r')
print('--------------------------------------------------------')
buf = ''
for line in sql:
    print(line.replace('\n',''))
    buf += line
pc.copy(buf)
sql.close()
print('SQL вже скопійовано в буфер обміну!')
print('--------------------------------------------------------')
input("Для завершення натиніть Enter.")


