# Задание 6
import codecs
f = codecs.open( "lab4.6.txt", "r", "utf_8_sig" )
const = True
while const:
    lst = f.readline()
    if not lst:
        print('(The End)')
        const = False
    else:
        str_1 = lst.split(':')[0]
        lenght = len(lst)
        val = []
        i = 0
        while i < lenght:
            s_int = ''
            a = lst[i]
            while '0' <= a <= '9':
                s_int += a
                i += 1
                if i < lenght:
                    a = lst[i]
                else:
                    break
            i += 1
            if s_int != '':
                val.append(int(s_int))
        sum = 0
        for i in range(len(val)):
            sum += val[i]
        const = dict.fromkeys([str_1], sum)
        print(const, end=' ')
f.close()