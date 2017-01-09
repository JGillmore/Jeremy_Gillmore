def draw_stars(arr):
    for num in range(0,len(arr)):
        string = ""
        if type(arr[num]) == str:
            count = 0
            while count < len(arr[num]):
                string += arr[num][0].lower()
                count += 1
        else:
            while arr[num] > 0:
                string += "*"
                arr[num] -= 1
        print string

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(x)
