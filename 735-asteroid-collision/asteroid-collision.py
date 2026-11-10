class Solution(object):
    def asteroidCollision(self, asteroids):
            res=[]
            n=len(asteroids)
            for i in asteroids:
                while res and res[-1]>0 and i<0:
                    if res[-1]<abs(i):
                        res.pop()
                    elif res[-1]==abs(i):
                        res.pop()
                        break
                    else:
                        break
                else:
                    res.append(i)
            return res

