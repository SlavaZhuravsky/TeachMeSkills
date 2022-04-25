# nambers = [1, 2, 3, 6, 9, 1, 2, 3, 4, 5]
namber = {}
def function(nambers):
    for i in nambers:
        if namber.get(i):
            namber[i] += 1
        else:
            namber[i] = 1
    print(namber)
    
function(nambers = [1, 4, 1, 4, 3, 1])

