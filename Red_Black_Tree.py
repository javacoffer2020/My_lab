class point:

    def __init__(self, name=0, color=True):
        self.name = name
        self.color = color

    def __str__(self):
        if self.color:
            c = 'Red'
        else:
            c = 'Black'
        return "Name:{}, color:{}\n".format(self.name, c)


class red_black_tree:

    def __init__(self, point=point(), father=None, lchild=None, rchild=None):
        self.point = point
        self.father = father
        self.lchild = lchild
        self.rchild = rchild

    def __str__(self):
        return "Father:{}; Point:{}; lchild:{}; rchild:{}".format(self.father.name, self.lchild.name, self.rchild.name)


a = point(1)
b = point(2)
c = point(3)
d = point(4)

print(a, b, c)

