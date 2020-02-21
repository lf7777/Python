class Solution(object):
    def game(self,guess,answer):
        count = 0
        i=0
        while i < len(guess):
            if guess[i]==answer[i]:
                count+=1
            i+=1
        return count

new = Solution()
print(new.game([3,3,3],[3,3,3]))
