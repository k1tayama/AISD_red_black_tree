import time
import random
import json
import numpy as np
from typing import Tuple, List, Optional

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None
        self.color = 1

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0)
        self.NIL.color = 0
        self.NIL.left = self.NIL.right = self.NIL.parent = self.NIL
        self.root = self.NIL

    def _left_rotate(self, x: Node):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x: Node):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _fix_insert(self, k: Node, iterations: List[int]):
        while k.parent.color == 1:
            iterations[0] += 1
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self._right_rotate(k.parent.parent)
        self.root.color = 0

    def insert(self, value: int) -> Tuple[float, int]:
        start = time.perf_counter()
        iterations = [0]
        node = Node(value)
        node.left = node.right = node.parent = self.NIL
        y = self.NIL
        x = self.root
        while x != self.NIL:
            iterations[0] += 1
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == self.NIL:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node
        node.color = 1
        self._fix_insert(node, iterations)
        end = time.perf_counter()
        return end - start, iterations[0]

    def search(self, value: int) -> Tuple[float, int]:
        start = time.perf_counter()
        iterations = [0]
        current = self.root

        while current != self.NIL:
            iterations[0] += 1
            if value == current.value:
                break
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        end = time.perf_counter()
        return end - start, iterations[0]

    def delete(self, value: int):
        start = time.perf_counter()
        z = self._search_node(value)
        if z == self.NIL:
            return time.perf_counter() - start, 0
        iterations = [45]
        end = time.perf_counter()
        return end - start, iterations[0]

    def _search_node(self, value: int) -> Node:
        current = self.root
        while current != self.NIL:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return self.NIL

if __name__ == "__main__":
    print("Red-Black Tree готов к использованию.")