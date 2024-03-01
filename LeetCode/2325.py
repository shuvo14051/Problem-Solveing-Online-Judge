class Solution:
    
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        unique_key = ""
        for i in key:
            if i==" ":
                continue
            if i not in unique_key:
                unique_key += i
        translation_table = str.maketrans(unique_key, alphabet)
        return message.translate(translation_table)        

    
s = Solution()
print(s.decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))