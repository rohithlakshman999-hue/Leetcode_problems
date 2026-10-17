class Solution(object):
    def lemonadeChange(self, bills):
        n=len(bills)
        five=0
        ten=0
        twen=0
        for x in bills:
            if x==5:
                five+=1
            elif x==10:
                ten+=1
                if five==0:
                    return False
                else:
                    five-=1
            elif x==20:
                if five>0 and ten>0:
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                else:
                    return False
        return True
