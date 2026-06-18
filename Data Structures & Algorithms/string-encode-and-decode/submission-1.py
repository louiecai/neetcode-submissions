class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(string)) + '*' + string for string in strs])

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        currentLen = ''

        while i < len(s):
            if s[i] == '*':
                output.append( s[i + 1:i + 1 + int(currentLen)] )
                i += int(currentLen) + 1
                currentLen = ''
            elif s[i].isnumeric:
                currentLen += str(s[i])
                i += 1
        
        return output
            
