'''
maintain a prefix sum which sum the elements as the array is traversed , it counts the number of subarrays
from any interval i-->j.
It maintains a hashmap or dictionary, stores the prefix sum in the hashmap
if the prefixsum-(k) is in the hashmap it increases the counter by the value stored in the hashmap.
'''

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        prefixsum = 0
        m = defaultdict(int)
        m[0] = 1
        
        for num in nums:
            prefixsum += num
            cnt += m[prefixsum - k]  
            m[prefixsum] += 1

        return cnt
