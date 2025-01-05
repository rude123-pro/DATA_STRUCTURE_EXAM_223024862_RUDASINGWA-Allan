class TreeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

def create_legal_document_tree():
    root = TreeNode("Legal Documents")
    root.left = TreeNode("Firm Docs")    
    root.right = TreeNode("Individual Docs")   
    
    root.left.left = TreeNode("Amendation")
    root.left.right = TreeNode("Taxes forms") 
    
    root.right.left = TreeNode("Business Plan") 
    root.right.right = TreeNode("Location size")

    return root
def display_tree(root):
    def get_height(node):
        if not node:
            return 0
        return max(get_height(node.left), get_height(node.right)) + 1
    def get_width(node):
        if not node:
            return 0
        return max(len(node.name), get_width(node.left) + get_width(node.right))
    def _display_aux(node):
        if not node.right and not node.left:
            line = node.name
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        if not node.right:
            lines, n, p, x = _display_aux(node.left)
            s = node.name
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if not node.left:
            lines, n, p, x = _display_aux(node.right)
            s = node.name
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        left, n, p, x = _display_aux(node.left)
        right, m, q, y = _display_aux(node.right)
        s = node.name
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = _display_aux(root)
    for line in lines:
        print(line)

def main():
    root = create_legal_document_tree()
    print("\nLegal Document Binary Tree Structure:")
    print("=" * 50)
    display_tree(root)
    
    print("=" * 50)
if __name__ == "__main__":
    main()