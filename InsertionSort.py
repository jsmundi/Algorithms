#Insertion Sort

def insort(a):

    for index in range(1, len(a)):

        currentval = a[index]
        position = index

        while position>0 and a[position-1]>currentval:
            a[position] = a[position-1]
            position = position-1

        a[position] = currentval


a = [12, 11, 13, 5, 6]
insort(a)
print(a)