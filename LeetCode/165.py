class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        print("Before append:")
        print(v1, v2)

        # Make both versions equal length
        while len(v1) < len(v2):
            v1.append('0')
        while len(v2) < len(v1):
            v2.append('0')
        
        print("After append:")
        print(v1, v2)

        for i in range(len(v1)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        
        return 0

s = Solution()
print(s.compareVersion(version1 = "0.1", version2 = "1.1"))


# Wrong answer
"""
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        if len(v1) != len(v2):
            return 0
        else:
            for i in range(len(v1)):
                if int(v1[i]) > int(v2[i]):
                    return 1
                elif int(v1[i]) < int(v2[i]):
                    return -1
                else:
                    return 0
"""