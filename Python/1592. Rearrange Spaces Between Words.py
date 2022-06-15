class Solution:
    def reorderSpaces(self, text: str) -> str:
        if len(text) < 2: return text
        print(text, len(text))
        s = text.count(" ")
        text = text.split()
        temp = len(text) - 1
        n = s // (temp) if temp > 0 else 0
        m = " " * (s % (temp)) if temp > 0 else " " * s
        return (" " * n).join(text) + m
