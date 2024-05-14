class Solution:
    def isPalindrome(self, s: str) -> bool:
        base = "abcdefghijklmnopqrstuvwxyz0123456789"
        string = ""
        for i in s.lower():
            if i in base:
                string += i
        return string == string[::-1]
    
s = Solution()
print(s.isPalindrome("sa1rGJngX!::lF3By:AB1,Jca:Uvt.`1\"; DK2u?;1d6ma!K7 as:lU:7Yvz434?X'0c:0;h6R2Aht!s:rQOK HiO?pH!B38 zu7\"' PW8urs4E 8?zKlE\"hy\"C!1x0?TXwj6K\",6GIIj4'sw!kBo:r?y:?;ia`:wI,,Iw:`ai;?:y?r:oBk!ws'4jIIG6,\"K6jwXT?0x1!C\"yh\"ElKz?8 E4sru8WP '\"7uz 83B!Hp?OiH KOQr:s!thA2R6h;0:c0'X?434zvY7:Ul:sa 7K!am6d1;?u2;D K\"1`.tvU:acJ,1BA:yB3Fl::!XgnJGr1as"))