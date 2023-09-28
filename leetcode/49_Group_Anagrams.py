class Solution_fast:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        elif len(strs) == 1:
            return [strs]
        
        hash_table = {}
        for string in strs:
            key = [0] * 26
            for letter in string:
                pos = ord(letter) - ord("a")
                key[pos] += 1
            key = tuple(key)
            if key in hash_table:
                hash_table[key].append(string)
            else:
                hash_table[key] = [string]
        return hash_table.values()


class Solution_slower:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        elif len(strs) == 1:
            return [strs]
        
        hash_table = {}

        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in hash_table:
                hash_table[sorted_string].append(string)
            else:
                hash_table[sorted_string] = [string]
        return hash_table.values()
