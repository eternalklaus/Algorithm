class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        output = []
        for word in words:
            output += word.split(separator)
        output = [_ for _ in output if _ != ""]
        return output