class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()#先把數字先排好
        ans=[[nums[0]]]#把最前面、最小的數字，放在兩成方括號裡
        repeat=0#目前的數字nums[0]沒有重複
        N=len(nums)#有幾個數字
        for i in range(1,N):#想比較是否相同
            if nums[i]==nums[i-1]:
                repeat+=1
                if len(ans)<=repeat:
                    ans.append([])#增加一層樓
            else:#沒有重複
                repeat=0
            ans[repeat].append(nums[i])
        return ans