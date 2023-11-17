def check_comand(user_comand: str, comands: list[str]) -> bool:
    if user_comand in comands:
        return True
    cnt = 0

    def variables(comand: str):
        res = []
        for i in range(len(comand)):
            check_str = ''
            for k in range(len(comand)):
                if i != k:
                    check_str += comand[k]
            res.append(check_str)
        return set(res)
    user_variables = variables(user_comand)
    comands_variables = []
    for i in comands:
        elems = variables(i)
        for k in elems:
            comands_variables.append(k)
    
    #пользователь ввел лишний символ
    for i in user_variables:
        cnt += comands.count(i)
    if cnt > 1:
        return False
    
    #пользователь пропустил символ
    cnt += comands_variables.count(user_comand)
    if cnt > 1:
        return False

    #пользователь заменил один символ
    for i in user_variables:
        cnt += comands_variables.count(i)
    return cnt == 1


        
