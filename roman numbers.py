'''Given a roman numeral, convert it to an integer.

 '''
class Solution:
    def romanToInt(self, s: str) -> int:
        rome_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        a = 0
        for i in range(1, len(s)):

            for key, value in rome_nums.items():

                if rome_nums[s[i]] > rome_nums[s[i - 1]]:
                    a -= rome_nums[s[i - 1]]
                    a += rome_nums[s[i]] - rome_nums[s[i - 1]]
                    break

                else:
                    if s[i] == key:
                        a += value

        a += rome_nums.get(s[0])

        return a
res = Solution()
print(res.romanToInt('MCMXCIV'))