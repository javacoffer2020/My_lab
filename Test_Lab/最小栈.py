class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def __repr__(self):
        return str(self.main_stack)

    def push(self, element):
        self.main_stack.append(element)
        # 若辅助栈为空，或