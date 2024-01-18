def head_smash(arr):
    if len(str(arr)) == 0 or arr == []:
        return 'Gym is empty'
    elif type(arr) == int:
        return "This isn't the gym!!"
    else:
        for i in range(len(arr)):
            arr[i] = arr[i].replace('O', ' ')
        return arr