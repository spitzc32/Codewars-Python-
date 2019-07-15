def solution(args):
    val, sep=f'{args[0]}', ','	
    for v in range(2,len(args)):
        if (args[v-2] == args[v]-2):
            sep = '-'
        elif (sep=='-'):
            val += f"{sep}{args[v-1]}"
            sep=','
        else:
            val+= f"{sep}{args[v-1]}"
        if v == len(args)-1:
            val+= f"{sep}{args[v]}"
        v+=1
    return val
2 we
