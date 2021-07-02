from itertools import combinations

def set(arr,r):
    return list(combinations(arr,r))
if __name__=="__main__":
    arr = [1,2,3,4]
    r = 2
    print(set(arr,r))    