comands = ['cd', 'ls', 'git']

for i in range(len(comands)):
        for j in range(len(comands[i])):
            check_str = ''
            for k in range(len(comands[i])):
                if k != j:
                     check_str += comands[i][k]
            print(check_str)