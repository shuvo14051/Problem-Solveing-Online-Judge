from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to store anagrams
        anagrams = {}
        
        # Iterate through each string in the input list
        for s in strs:
            # Sort the string to use as a key for the dictionary
            sorted_s = "".join(sorted(s))
            
            # If the sorted string is not in the dictionary, add it as a key with an empty list as its value
            if sorted_s not in anagrams:
                anagrams[sorted_s] = []
            
            # Append the original string to the list corresponding to its sorted form
            anagrams[sorted_s].append(s)
        
        # Return the values of the dictionary as a list
        return list(anagrams.values())

# Example usage
solution = Solution()
input_list = ["", "b"]
print(solution.groupAnagrams(input_list))
