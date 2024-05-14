import itertools

class Solution:
    def countVowelStrings(self, n: int) -> int:
      s = "aeiou"
      out = list(itertools.combinations_with_replacement(s,n))
      count = 0
      for item in out:
        if list(item) == sorted(item):
          count+=1

      return count