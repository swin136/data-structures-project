"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node
from src.stack import Stack


class TestNodeStack(unittest.TestCase):
    def test_node(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')
        self.assertEqual(n1, n2.next_node)

    def test_stack_push(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')

        self.assertEqual(stack.top.data, 'data3')
        self.assertEqual(stack.top.next_node.data, 'data2')
        self.assertEqual(stack.top.next_node.next_node.data, 'data1')
        self.assertIs(stack.top.next_node.next_node.next_node, None)
        with self.assertRaises(AttributeError):
            print(stack.top.next_node.next_node.next_node.data)
