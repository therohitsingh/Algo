
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        for idx in range(len(nums)-1, 0, -1):
            if nums[idx] == nums[idx-1]:
                del nums[idx]
        return len(nums)

#second method for removing duplicate

arr = [0,0,1,1,1,2,2,3,3,4]
x = list(dict.fromkeys(arr))
print(x)