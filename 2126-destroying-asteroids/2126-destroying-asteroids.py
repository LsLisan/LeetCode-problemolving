class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        ans = True
        for i in asteroids:
            if (mass < i):
                return False
            mass +=i
        return ans 