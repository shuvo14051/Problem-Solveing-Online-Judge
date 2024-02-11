class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()","o")
        command = command.replace("(al)","al")

        return command
    

s = Solution()
print(s.interpret("G()()()()(al)"))
