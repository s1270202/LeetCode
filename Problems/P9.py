# 2023/4/29


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x_str = str(x)
            x_reverse = ""
            for s in x_str:
                x_reverse = s + x_reverse

            if x == int(x_reverse):
                return True
            else:
                return False