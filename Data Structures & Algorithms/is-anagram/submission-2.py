class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list,t_list = [],[]
        for i in s:
            s_list.append(i)
        for i in t: 
            t_list.append(i)
 

        s_list.sort()
        t_list.sort()

        if(len(s_list)!= len(t_list)):
            return False


        for i in range(len(s_list)):
            if s_list[i] != t_list[i]:
                return False
        return True
        