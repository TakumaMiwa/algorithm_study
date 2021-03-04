
pos = [0] * 8
flag_a = [False] * 8
flag_b = [False] * 15
flag_c = [False] * 15

def put():
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()


def set_queen(i):
    for j in range(8):
        if not flag_a[j] and not flag_b[i+j] and not flag_c[i-j+7]:
            pos[i] = j
            if i == 7:
                put()
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = True
                set_queen(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = False


set_queen(0)
