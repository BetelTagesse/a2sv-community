class Solution:
    def sortSentence(self, s: str) -> str:
        words = []
        word = ""
        length = 0
        sorted = ""
        for i in range(10):
            words.append(None)
        for i in s:
            if i != " ":
                word += i
                length += 1
                j = i
            else:
                track = int(j)
                newWord = word[:(length - 1)]
                words[track] = newWord
                word = ""
                length = 0
        words[int(i)] = word[:length - 1]
        for i in words:
            if i:
                sorted += (i + " ")
        return(sorted[:(len(sorted) - 1)])
