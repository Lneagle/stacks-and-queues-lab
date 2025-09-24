class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f'Pushed {item} to stack: {self.items}')

    def pop(self):
        if not self.is_empty():
            removed = self.items.pop()
            print(f'Popped {removed} from stack: {self.items}')
            return removed
        else:
            print('Stack is empty. Nothing to pop.')
            return None
        
    def peek(self):
        if not self.is_empty():
            print(f'Top of stack is: {self.items[-1]}')
            return self.items[-1]
        else:
            print('Stack is empty. No top element.')
            return None
        
    def is_empty(self):
        return len(self.items) == 0

def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    # TODO: Implement stack logic to validate parentheses
    tester = Stack()
    for c in s:
        if c in ['{', '[', '(']:
            tester.push(c)
        elif c == '}':
            if tester.peek() == '{':
                tester.pop()
        elif c == ']':
            if tester.peek() == '[':
                tester.pop()
        elif c == ')':
            if tester.peek() == '(':
                tester.pop()
    return tester.is_empty()