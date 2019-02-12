class Solution(object):
    def findNSum(self,nums,target,N,cur,res):
        if len(nums)<N or N<2 or N*nums[0]>target or N*nums[-1]<target:
            return
        
        #implement 2sum in sorted list 
        if N==2:
            i = 0
            j = len(nums)-1
            while(i<j):
                if nums[i] + nums[j] == target:
                    res.append(cur +[nums[i],nums[j]])
                    i+=1
                    j-=1
                    while(i<j and nums[i]==nums[i-1]):
                        i+=1
                elif nums[i]+nums[j]<target:
                    i+=1
                else:
                    j-=1
        else: #reduce to N = 2
            for i in range(len(nums)-N+1):
                if i == 0 or(i>0 and nums[i-1] !=nums[i]):
                    self.findNSum(nums[i+1:],target-nums[i],N-1,cur+[nums[i]],res)
    
    
    
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.findNSum(nums,target,4,[],res)
        return res