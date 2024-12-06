#Creating a Class to check the Validity of a String of Parentheses

class py_solution:
    def is_valid_parentheses(self, stri):
        stack = []
        pchar = {'(':')','{':'}','[':']'}

        for parenthese in stri:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False

        return len(stack) == 0

print(py_solution().is_valid_parentheses("[{()]}]"))
print(py_solution().is_valid_parentheses("(())"))
print(py_solution().is_valid_parentheses("()"))
