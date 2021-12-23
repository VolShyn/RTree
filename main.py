# Створити вузел
class RTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


# Дерево
class RTree:
    def __init__(self, t):
        self.root = RTreeNode(True)
        self.t = t

        # Вставити вузел

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = RTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

        # Вставити не заповн.

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self.insert_non_full(x.child[i], k)

        # Розділити потомків

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = RTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

    # Вивести на екран дерево
    def print_tree(self, x, l=0):
        sg.Print("Level ", l, " ", len(x.keys), end=":")
        for i in x.keys:
            sg.Print(i, end=" ")
        sg.Print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)

    # Знайти ключ в дереві
    def search_key(self, k, x=None):
        if x is not None:
            i = 0
            while i < len(x.keys) and k > x.keys[i][0]:
                i += 1
            if i < len(x.keys) and k == x.keys[i][0]:
                return (x, i)
            elif x.leaf:
                return None
            else:
                return self.search_key(k, x.child[i])

        else:
            return self.search_key(k, self.root)


# def main():
#     R = RTree(3)
#
#     for i in range(10):
#         R.insert((i, 2 * i))
#     R.print_tree(R.root)
#
#     if R.search_key(8) is not None:
#         print("\nFound root")
#     else:
#         print("\nRoot Not Found")


if __name__ == '__main__':
    import PySimpleGUI as sg

    sg.theme('BluePurple')

    layout = [[sg.Text(size=(15, 1), key='-OUTPUT-')],
              [sg.Input(key='-IN-')],
              [sg.Button('Find'), sg.Button('Insert'), sg.Button('ShowTree')]]

    window = sg.Window('R-tree', layout, font='Helvetica 12')
    R = RTree(3)
    R.insert((11, 1)), R.insert((9, 2)), R.insert((8, 3)), R.insert((10, 4)),
    R.insert((16, 5)), R.insert((18, 6)), R.insert((15, 7)), R.insert((17, 8)),
    R.insert((20, 9)), R.insert((23, 10))
    k = 11
    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'ShowTree':
            R.print_tree(R.root)
        if event == 'Insert':
            if values['-IN-'] is not None:
                R.insert((int(values['-IN-']), k))
                k += 1
            else:
                break

        if event == 'Find':
            if R.search_key(int(values['-IN-'])) is not None:
                sg.popup("\nFound ")
            else:
                sg.popup("\nNot Found")

    window.close()
    # main()
