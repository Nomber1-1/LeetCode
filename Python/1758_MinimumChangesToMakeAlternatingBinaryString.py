def minOperations(s):
        """
        :type s: str
        :rtype: int
        """
        num_change = 0
        one_zero_counter = 0
        zero_one_counter = 0
        
        print("String is: " + s)
        
        for i in range(0,len(s)-1,2):
            print("Sequence is %s%s" %(s[i],s[i+1]))
            if(s[i]=="0" and s[i+1]=="1"):
                zero_one_counter += 1
            elif(s[i]=="1" and s[i+1]=="0"):
                one_zero_counter += 1
            elif(s[i]==s[i+1]):
                num_change += 1
        
        #Not Forget to take into consideration last digit if odd
        if(len(s)%2!=0):
            if(s[len(s)-2]=="0" and s[len(s)-1]=="1"):
                zero_one_counter += 1
            elif(s[len(s)-2]=="1" and s[len(s)-1]=="0"):
                one_zero_counter += 1
            elif(s[len(s)-2]==s[len(s)-1]):
                num_change += 1
        
                
        print("01: %s" %(zero_one_counter))
        print("10: %s" %(one_zero_counter))
        print(num_change)
        
        if num_change == 0 and one_zero_counter == zero_one_counter:
            print("No changes: 0")
            return num_change
        
        if zero_one_counter == one_zero_counter:
            print("For string %s, the number of changes needed is %s" %(s, num_change))
            return num_change
        
        num_change = 0
        if zero_one_counter > one_zero_counter:
            print("01 > 10")
            for i in range(0,len(s)-1,2):
                if(s[i]=="1" and s[i+1]=="0"):
                    num_change += 2
                elif(s[i]==s[i+1]):
                    num_change += 1
                    
        elif zero_one_counter < one_zero_counter:
            print("01 < 10")
            for i in range(0,len(s)-1,2):
                if(s[i]=="0" and s[i+1]=="1"):
                    num_change += 2
                elif(s[i]==s[i+1]):
                    num_change += 1
            
        print("For string %s, the number of changes needed is %s" %(s, num_change))
        return num_change
            
# Solution - 1:
"""
class Solution(object):
    def minOperations(self, s):
        c1=c2=0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '0':
                    c1+=1
                else:
                    c2+=1
            else:
                if s[i] == '1':
                    c1+=1
                else:
                    c2+=1
        return min(c1,c2)
    
# Solution - 2:
class Solution(object):
    def minOperations(self, s):
        c_0 = s[0]
        count1 = self.count(s, c_0)
        count2 = self.count(s, '0' if c_0 == '1' else '1') + 1
        return min(count1, count2)

    def count(self, s, c_pre):
        count = 0
        for i in range(1, len(s)):
            current = s[i]
            if current == c_pre:
                count += 1
                c_pre = '0' if c_pre == '1' else '1'
            else:
                c_pre = current
        return count
"""
    
if __name__ == "__main__":
    print(minOperations("0100")) #1
    print(minOperations("10")) #0
    print(minOperations("1111")) #2
    print(minOperations("100000")) #2
    print(minOperations("101001010101")) #4
    print(minOperations("000")) #1
