
import matplotlib.pyplot as plt
plt.axis([0, 12, 0, 12])
import pygame

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ORANGE = (248, 184, 120)
RED = (255, 0, 0)
pygame.init()
wn = pygame.display.set_mode((400,400))
wn.fill((WHITE))
pygame.display.flip()
font = pygame.font.Font('times new roman.ttf', 32)


class Binary_tree_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Binary_tree:
    def __init__(self, data):
        self.head = Binary_tree_node(data)

    def add(self, data):
        if self.head is None:
            self.head = Binary_tree_node(data)
            return
        self._add(self.head, data)

    def _add(self, curr_node, data):
        if data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = Binary_tree_node(data)
            else:
                self._add(curr_node.left, data)
        else:
            if curr_node.right is None:
                curr_node.right = Binary_tree_node(data)
            else:
                self._add(curr_node.right, data)
    
    def inorder(self):
        if self.head is not None:
            self._inorder(self.head)

    def _inorder(self, curr_node):
        if curr_node.left is not None:
            self._inorder(curr_node.left)
        print(curr_node.data)
        if curr_node.right is not None:
            self._inorder(curr_node.right)

    def preorder(self):
        if self.head is not None:
            self._preorder(self.head)
            
    def _preorder(self, curr_node):
        print(curr_node.data)
        if curr_node.left is not None:
            self._preorder(curr_node.left)
        if curr_node.right is not None:
            self._preorder(curr_node.right)
            
    def postorder(self):
        if self.head is not None:
            self._postorder(self.head)

    def _postorder(self, curr_node):
        if curr_node.left is not None:
            self._postorder(curr_node.left)
        if curr_node.right is not None:
            self._postorder(curr_node.right)
        print(curr_node.data)
        
    def height_tree(self):
        return self._height_tree(self.head)

    def _height_tree(self, curr_node):
        if curr_node.left and curr_node.right is not None:
            return 1 + max(self._height_tree(curr_node.left), self._height_tree(curr_node.right))
        elif curr_node.left is not None:
            return 1 + self._height_tree(curr_node.left)
        elif curr_node.right is not None:
            return 1 + self._height_tree(curr_node.right)
        else:
            return 1
     
    def min_value(self):
        return self._min_value(self.head)  
     
    def _min_value(self, curr_node):
        if curr_node.left is not None:
            return self._min_value(curr_node.left)
        return curr_node.data

    def max_value(self):
        return self._max_value(self.head)
        
    def _max_value(self, curr_node):
        if curr_node.right is not None:
            return self._max_value(curr_node.right)
        return curr_node.data

    def draw(self, x, y, curr_node):
        p1 = [x, y]
        p2 = [p1[0] - 1, p1[1] - 2]
        p3 = [p1[0] + 1, p1[1] - 2]
        plt.text(p1[0] - 0.015, p1[1] + 0.25, curr_node.data)
        if curr_node.left is not None:
            self.draw_left(x, y, curr_node.left)
        if curr_node.right is not None:
            self.draw_right(x, y, curr_node.right)

    def draw_left(self, x, y, curr_node):
        p1 = [x, y]
        p2 = [p1[0] - 1, p1[1] - 2]
        p3 = [p1[0] + 1, p1[1] - 2]
        x_values_left = [p1[0], p2[0]]
        y_values_left = [p1[1], p2[1]]
        plt.plot(x_values_left, y_values_left, 'bo', linestyle="--")
        plt.text(p2[0] - 0.5, p2[1] - 0.25, curr_node.data)
        if curr_node.left is not None:
            self.draw_left(p2[0], p2[1], curr_node.left)
        if curr_node.right is not None:
            self.draw_right(p2[0], p2[1], curr_node.right)

    def draw_right(self, x, y, curr_node):
        p1 = [x, y]
        p2 = [p1[0] - 1, p1[1] - 2]
        p3 = [p1[0] + 1, p1[1] - 2]
        x_values_right = [p1[0], p3[0]]
        y_values_right = [p1[1], p3[1]]
        plt.plot(x_values_right, y_values_right, 'bo', linestyle="--")
        plt.text(p3[0] + 0.5, p3[1] - 0.25, curr_node.data)
        if curr_node.right is not None:
            self.draw_right(p3[0], p3[1], curr_node.right)
        if curr_node.left is not None:
            self.draw_left(p3[0], p3[1], curr_node.left)
            
    def breadth(self):
        h = self.height_tree()
        for i in range(h):
            self.print_level(i, self.head)
               
    def print_level(self, level, curr_node):
        if curr_node.data is None:
            return
        if level == 0:
            print(curr_node.data)
        elif level > 0:
            if curr_node.left is not None:
                self.print_level(level - 1, curr_node.left)
            if curr_node.right is not None:
                self.print_level(level - 1, curr_node.right)
    
    def draw_pygame(self, x, y , curr_node):
        p1 = [x, y]
        text = font.render(str(curr_node.data), True, GREEN, BLUE)
        wn.blit(text, p1)
        if curr_node.left is not None:
            self.draw_left_pygame(x, y, curr_node.left)
        if curr_node.right is not None:
            self.draw_right_pygame(x, y, curr_node.right)

    def draw_left_pygame(self, x, y, curr_node):
        p1 = [x, y]
        p2 = [p1[0] - 30, p1[1] + 60]
        pygame.draw.line(wn, BLUE, p1, p2)
        pygame.draw.circle(wn, BLACK, p1, 4)
        pygame.draw.circle(wn, BLACK, p2, 4)
        text = font.render(str(curr_node.data), True, GREEN, BLUE)
        wn.blit(text, p2)
        if curr_node.left is not None:
            self.draw_left_pygame(p2[0], p2[1], curr_node.left)
        if curr_node.right is not None:
            self.draw_right_pygame(p2[0], p2[1], curr_node.right)

    def draw_right_pygame(self, x, y, curr_node):
        p1 = [x, y]
        p3 = [p1[0] + 30, p1[1] + 60]
        pygame.draw.line(wn, BLUE, p1, p3)
        pygame.draw.circle(wn, BLACK, p1, 4)
        pygame.draw.circle(wn, BLACK, p3, 4)
        text = font.render(str(curr_node.data), True, GREEN, BLUE)
        wn.blit(text, p3)
        if curr_node.right is not None:
            self.draw_right_pygame(p3[0], p3[1], curr_node.right)
        if curr_node.left is not None:
            self.draw_left_pygame(p3[0], p3[1], curr_node.left)
            
my_tree = Binary_tree(10)
#reader = open('myfile.txt')
#list_number = list(reader)
#print(list_number)
#reader.close()

#for i in range(len(list_number)):
#    list_number[i] = float(list_number[i])
#    my_tree.add(list_number[i])
my_tree.add(5)
my_tree.add(3)
my_tree.add(12)
my_tree.add(4)
my_tree.add(16)
my_tree.add(1)
my_tree.add(8)
#print(my_tree.postorder())
#print(my_tree.height_tree())
#print(my_tree.min_value())
#print(my_tree.max_value())
#my_tree.print_level(1, my_tree.head)
#my_tree.breadth()
#my_tree.postorder()
my_tree.draw(5, 10, my_tree.head)
plt.show()
state = True
while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
    my_tree.draw_pygame(200, 30, my_tree.head)
    pygame.display.flip()

pygame.quit()
quit()


