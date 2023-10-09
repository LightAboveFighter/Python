def intToRoman(num: int) -> str:
    msv = [ int( list(str(num))[i] ) for i in range(len(str(num)) ) ]
    ans = ''
    Romans1 = ( 1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10:"X")
    Romans2 = ( 4="IV", 9="IX" )
    
    for i in range(len(msv)):
        case_part = 0
        if msv[i] in [1, 2, 3]:
            case_part = 1
        if msv[i] in [4, 9]:
            case_part = 2
        else:
            case_part = 3
        
        ans.append