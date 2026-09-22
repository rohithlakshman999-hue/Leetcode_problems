class Solution(object):
    def letterCombinations(self, dig):
        list={
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }
        res = [""]

        for digit in dig:
            new = []
            for old in res:
                for ch in list[digit]:
                    new.append(old + ch)
            res = new

        return new