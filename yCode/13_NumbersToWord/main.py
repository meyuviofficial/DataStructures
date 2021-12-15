class Solution:
    def GetWord(self, num: int) -> str:

        switcher = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

        return switcher.get(num, '')

    def solve(self, num: int, ans: str) -> str:
        if num == 0:
            return ans
        elif num < 10:
            # print(num)
            return ans+self.GetWord(num)
        elif num < 20:
            return ans+self.GetWord(num)
        elif num < 100:
            # print(num)
            ans += self.GetWord(num//10 * 10)+" "+self.solve(num % 10, ans)
            return ans.strip()
        elif num < 1000:
            # print(num)
            ans += self.GetWord(num//100)+" Hundred " + \
                self.solve(num % 100, ans)
            return ans.strip()
        elif num < 1000000:
            # print(num)
            ans += self.solve(num//1000, ans)+" Thousand " + \
                self.solve(num % 1000, ans)
            return ans.strip()
        elif num < 1000000000:
            ans += self.solve(num//1000000, ans)+" Million " + \
                self.solve(num % 1000000, ans)
            # print(ans)
            return ans.strip()
        elif num < 1000000000000:
            ans += self.solve(num//1000000000, ans) + \
                " Billion "+self.solve(num % 1000000000, ans)
            # print(ans)
            return ans.strip()

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        return self.solve(num, "").strip()

"""
Input: num = 123
Output: "One Hundred Twenty Three"

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""