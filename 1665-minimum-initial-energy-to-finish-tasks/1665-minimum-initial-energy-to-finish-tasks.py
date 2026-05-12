class Solution(object):
    def defference(self,task):
        return task[1]- task[0]
        
    def minimumEffort(self, tasks):
        tasks.sort(key=self.defference)        
        ans = 0
        for i in tasks:
            ans = max( ans + i[0], i[1])
        return ans