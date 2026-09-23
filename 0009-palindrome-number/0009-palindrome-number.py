class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        if x==0:
            return True    
        temp=x
        num=0
        while temp>0:
            num=num*10+temp%10
            temp//=10
        if num==x:
            return True
        return False        


        """
        :type x: int
        :rtype: bool
        """
        