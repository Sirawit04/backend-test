def odd_int(arr):
    num_count = {}
    
    for num in arr:
        if num not in num_count:
            num_count[num] = 1
        else:
            num_count[num]+=1    

    for key, value in num_count.items():
            if value % 2 == 1:
                return key
            

# if __name__ == "__main__":
#      print(odd_int([0]))
