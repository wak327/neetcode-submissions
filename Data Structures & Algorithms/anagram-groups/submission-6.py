def get_hash(str_1: str) -> tuple:
    ch_arr = [0]*26
    for i in str_1:
        ch_arr[ord(i)-ord('a')] += 1
    return tuple(ch_arr)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strs:
            s_h = get_hash(s)
            groups[s_h].append(s)
        return list(groups.values())