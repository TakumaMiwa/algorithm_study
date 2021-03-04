def isUniaueChars(stirng_list):
    boolean = [False]*len(string_list)
    for i in range(len(stirng_list)):
        key = stirng_list[i]
        if boolean[key]:
            print("False")
            return
        boolean[i]=True
    print("Success")
    return

string_list = input()
isUniaueChars(string_list)