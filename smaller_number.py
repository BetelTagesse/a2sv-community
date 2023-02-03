class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count=[]
        for values in nums:
            number=0
            for j in nums:
                if values>j:
                    number+=1
            count.append(number)
        return count
    