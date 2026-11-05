class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        newarr = ''

        for i in range(len(word)):
            newarr += word[i]

            if word[i] == ch:
                break

        s = newarr[::-1]
        remaining = word[len(newarr):]

        value = s + remaining
        return value