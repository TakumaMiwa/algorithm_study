while True:
    time = list(input())
    if time[0]=='?':
        if time[1]=='?':
            time[0] = '2'
            time[1] = '3'
        elif 0<=int(time[1])<=3:
            time[0] = '2'
        else:
            time[0] = '1'

    if time[1]=='?':
        if time[0]=='0' or time[0]=='1':
            time[1] = '9'
        else:
            time[1] = '3'

    if time[3]=='?':
        time[3] = '5'
    if time[4]=='?':
        time[4] = '9'

    print(''.join(time))