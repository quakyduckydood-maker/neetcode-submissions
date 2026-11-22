class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hushtable = defaultdict(list)
        listtoreturn = []
        for strings in strs:
            key = "".join(sorted(strings))
            hushtable[key].append(strings)
        for key in hushtable:
            listtoreturn.append(hushtable[key])
        return listtoreturn



            
            

