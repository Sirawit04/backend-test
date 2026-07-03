

def countSmileys(arr):
    count = 0
    for i in arr:
        if len(i) == 2:
            if i[0] == ":" or i[0] == ";":
                if i[1] == ")" or i[1] == "D":
                    count+=1
        elif len(i) == 3:
            if i[0] == ":" or i[0] == ";":
                if i[2] == ")" or i[2] == "D":
                    if i[1] == "-" or i[1] == "~":
                        count+=1
    
    return count


# test 
# arr = [';D', ':-(', ':-)', ';~)']
# print(countSmileys([';D', ':-(', ':-)', ';~)']))

# def countSmileys(arr):
#     count = 0
#     for i in arr:
#         if len(i) == 2:
#             for j in arr.values(i):
#                 print("passs")

# for i in arr:
#     if len(i) == 2:
#             if i[0] == ":" or i[0] == ";":
#                 print('pass')
