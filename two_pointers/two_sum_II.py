from typing import List


class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        l,r=0,len(num)-1
        res=[]

        while l<r:
            if num[l]+num[r]>target:
                r-=1
            elif num[l]+num[r]<target:
                l+=1
            else:
                return [l+1,r+1]
        
        return []