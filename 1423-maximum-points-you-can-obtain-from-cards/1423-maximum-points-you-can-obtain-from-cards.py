class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        lsum=0
        rsum=0
        maxsum=0
        for i in range(k):
            lsum+=cardPoints[i]
            maxsum=lsum
        right=len(cardPoints)-1
        for j in range(k-1,-1,-1):
            lsum-=cardPoints[j]
            rsum+=cardPoints[right]
            right-=1
            maxsum=max(maxsum,lsum+rsum)
        return maxsum