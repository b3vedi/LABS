from copy import deepcopy
from math import floor, sqrt

def array_not_equals(arr1,arr2):
    countx = 0
    for i in arr1:
        county = 0
        for j in i:
            if(arr2[countx][county] != j):return True
            county += 1
        countx += 1
    return False


def kmeans():
    points = [[2,2,"A"],[3,2,"B"],[1,1,"C"],[3,1,"D"],[1.5,0.5,"E"]]

    k = 2

    centres = [[2,2],[1,1]]
    prevCenters = [[0,0],[0,0]]
    mean = [[0,0],[0,0]]
    while(array_not_equals(centres,prevCenters)):
        list1=[]
        list2=[]
        for i in points:
            if(distance(i,centres[1]) > distance(i,centres[0])):
                list1.append(i)
            else :
                list2.append(i)
        sum1=0
        sum2=0
        for i in list1:
            sum1 += i[0]
            sum2 += i[1]
        mean[0][0] = sum1/len(list1)
        mean[0][1] = sum2/len(list1)
        sum1=0
        sum2=0
        for i in list2:
            sum1 += i[0]
            sum2 += i[1]
        mean[1][0] = sum1/len(list2)
        mean[1][1] = sum2/len(list2)
        print("Mean is ",mean)
        print("List1 is",list1)
        print("List2 is",list2)
        print("Centres are ",centres)
        prevCenters =deepcopy(centres)
        centres = deepcopy(mean)

def distance(a,b):
    sum = (a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1])
    return sqrt(sum)


if __name__ == "__main__":
    kmeans()