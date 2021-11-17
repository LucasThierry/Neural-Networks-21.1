#Abrir o arquivo xls
file2 = open('TRNcod.xls', 'r')
Lines = file2.readlines()
 
# Reescrever todas as linhas do xls para o csv modificando a separação para ','
file1 = open('TRNcod.csv', 'w')
for line in Lines:
    file1.writelines(line.replace("	",","))
file1.close()
