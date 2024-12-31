    from typing import List 

    class Solution:
        def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
            d = {}
            li = []
            for i in range(len(names)):
                d[heights[i]] = names[i]
            sorted_d = dict(sorted(d.items(), reverse=True))

            for val in sorted_d.values():
                li.append(val)

            return li

        
    s = Solution()
    print(s.sortPeople(["Mary","John","Emma"], [180,165,170]))