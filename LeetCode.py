'''
from tensorflow.examples.tutorials.mnist import input_data

class solution1:
    def twoSum(self,nums,target):
        length=len(nums)
        for i in range(length):
            for j in range(i+1,length):
                if(target-nums[i]==nums[j]):
                    return i,j

s=solution1()
nums=[2, 7, 11, 15]
print(s.twoSum(nums,9))
import math
class Solution2:
    def reverse(self, x):
        if(x>0):
            x=str(x)
            x=int(x[::-1])
            if((x>math.pow(2,31)-1)or (x<math.pow(-2,31))):
                x=0
        else:
            x=-1*x
            x = str(x)
            x = int(x[::-1])
            x=-1*x
            if ((x > math.pow(2, 31) - 1) or (x < math.pow(-2, 31))):
                x = 0
        return x
ss=Solution2()
print(ss.reverse(123))

class Solution3:
    def isPalindrome(self,x):
        if ((x<0) or ((x%10==0) and(x!=0))):
            return False
        reverNum = 0
        while(x>reverNum):
            reverNum=reverNum*10+(x%10)
            x/=10
        return x==reverNum or x==reverNum/10
sss=Solution3()
print(sss.isPalindrome(1111))


def hui(x):
    x=str(x)
    if(x==x[::-1]):
        return True
    else:
        return False
print(hui(11))
'''
class Solution4:
    def longestCommonPrefix(self, strs):
        n=len(strs)
        minl=min(len(x) for x in strs)
        print(n,minl)
        if not strs:
            return " "
        elif len(strs)==1:
            return strs[0]
        else:
            end=0
            while end<minl:
                for i in range(1,n):
                    if(strs[i][end]!=strs[i-1][end]):
                        return strs[i][:end]
                end+=1
            return strs[0][:end]

class Solution5:
    def isValid(self,s):
        if(len(s)%2==1or len(s)==0):
            return False
        dic={"(":")","{":"}","[":"]"}
        stacks=[]
        for i in s:
            print(i)
            if i in dic:
                stacks.append(i)
            else:
                if not stacks or dic[stacks.pop()]!=i:
                    return False
        return stacks==[]


class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution6:
    def mergrList(self,l1,l2):
        head=ListNode(0)
        first=head
        while(l1!=None and l2!=None):
            if(l1.val<l2.val):
                head.next=l1
                l1=l1.next
            else:
                head.next=l2
                l2=l2.next
        if(l1!=None):
            head.next=l1
        elif l2!=None:
            head.next=l2
        return first.next

class Solution7:
    def removeDuplicates(self, nums):
        len1=len(nums)
        print(len1)
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                    del(nums[j])
            len2=len(nums)
            print(len2)


class Solution8:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        s = 0
        for f in range(1, len(nums)):
            if nums[s] != nums[f]:
                s += 1
                nums[s] = nums[f]
        return s + 1

class Solution9:
    def strStr(self,haystack,needle):
        if needle==None:
            return 0
        if needle not in haystack:
            return -1
        return haystack.find(needle)

class Solution10:
    def searchInsert(self, nums, target):
        nums.append(target)
        nums.sort()
        for i in range(len(nums)):
            if target==nums[i]:
                return i
                break
s10=Solution10()
nums=[1,3,5,6]
target=2
print(s10.searchInsert(nums,target))

class solution:
    def countAndSay(self,n):
        if n==1:
            return '1'
        s=self.countAndSay(n-1)
        count=0
        temp_cha=s[0]
        new_str=''
        for cha in s:
            if cha==temp_cha:
                count+=1
            else:
                new_str=new_str+str(count)+temp_cha
                temp_cha=cha
                count=1
        new_str=new_str+str(count)+str(temp_cha)
        return new_str

class Solution11:
    def lengthOfLastWord(self,s):
        if(s==' '):
            return 0
        n=len(s)
        for i in range(len(s)-1):
            if(s[i]==" " and s[i+1]!=None):
                s1=s[i+1:len(s)]
                n=len(s1)
        return n
s11=Solution11()
s=""
print(s11.lengthOfLastWord(s))