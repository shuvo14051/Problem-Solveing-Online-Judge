from typing import List 

class Solution:

    def morse_code_generator(self, text):
        morse_mapping = {
        'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--.."
    }
        morse_code = ""
        for i in text:
            morse_code += morse_mapping[i]
        
        return morse_code
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s = set()
        for word in words:
            m = self.morse_code_generator(word)
            s.add(m)

        return len(s)
    

s = Solution()
print(s.uniqueMorseRepresentations(["gin","zen","gig","msg"]))
