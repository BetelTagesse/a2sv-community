# # class Solution(object):
# def fizzBuzz( n):
#             # """
#             # :type n: int
#             # :rtype: List[str]
#             # """
#             # self.n = n
#             if(n%3==0) & (n%5==0):
#                     return "FizzBuzz"
#             if (n % 3==0):
#                 return "fizz"
            
#             if(n%5==0):
#                 return "Buzz"
        
#             else:
#                 return n
# print(fizzBuzz(3))
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # ans list
        ans = []
       
        for num in range(1,n+1):

            if (num % 3 == 0) and (num % 5 == 0):
                # Divides by both 3 and 5, add FizzBuzz
                ans.append("FizzBuzz")
            elif num % 3 == 0:
                # Divides by 3, add Fizz
                ans.append("Fizz")
            elif num % 5 == 0:
                # Divides by 5, add Buzz
                ans.append("Buzz")
            else:
                # Not divisible by 3 or 5, add the number
                ans.append(str(num))

        return ans