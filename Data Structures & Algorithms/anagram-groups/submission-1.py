class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #for every every string in the list loop over over other key and check if that 
        # is an anagram
        myMap = {}
        for string in strs:
            key = self.getKey(string)
            if key in myMap:
                myMap[key].append(string)
            else:
                myMap[key] = [string]

        output = []
        for entry in myMap.values():
            output.append(entry)

        return output
    
    def getKey(self, string: str) -> str:
        arr = [0] * 26

        for char in string:
            arr[ord(char) - ord('a')] += 1
        key = ""
        print(arr)
        for i in range(0, 26):
            key += str(arr[i]) + str(i)
        return key

