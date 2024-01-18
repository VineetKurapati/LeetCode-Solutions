class Solution:
    def isIPv4(self,s):
        nums = s.split(".")
        if len(nums) > 4:
            return False
        if len(nums) < 4:
            return False
        for num in nums:
            if not num.isdigit():
                return False
            if int(num) > 255:
                return False
            if num[0] == "0" and len(num) != 1:
                return False
        return True
    def isIPv6(self, s):
        nums = s.split(":")
        if len(nums) > 8:
            return False
        valid = ["0" , "1" , "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E","F"] 
        for num in nums:
            if len(num) > 4:
                return False
            if len(num) < 1:
                return False
            for ch in num:
                if ch not in valid:
                    return False
        return True
    def validIPAddress(self, s: str) -> str:
        if self.isIPv4(s):
            return "IPv4"
        elif self.isIPv6(s):
            return "IPv6"
        else:
            return "Neither"