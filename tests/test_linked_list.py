"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import Node
from src.linked_list import LinkedList
from unittest.mock import patch


class TestNodeStack(unittest.TestCase):
    def test_node(self):
        """Тестирование класса Node из src/linked_list.py"""
        # Формируем последовательность из связанных элементов
        node_1 = Node({'user_dictionary': 1}, None)
        node_2 = Node({'user_dictionary': 2}, node_1)
        node_3 = Node({'user_dictionary': 3}, node_2)

        # Тестируем правильность следования элементов в списке
        self.assertIs(node_2, node_3.next_node)
        self.assertIs(node_1, node_2.next_node)

        # Тестируем цепочку элементов и их значения
        self.assertEqual(node_3.data, {'user_dictionary': 3})
        self.assertEqual(node_3.next_node.data, {'user_dictionary': 2})
        self.assertEqual(node_2.next_node.data, {'user_dictionary': 1})
        self.assertIs(node_2.next_node.next_node, None)
        # Тестируем отсутствие элементов после конца списка
        with self.assertRaises(AttributeError):
            print(node_2.next_node.next_node.data)

        # Создаем элемент с некорректным типом аттрибута экземпляра класса
        with self.assertRaises(TypeError):
            Node({'test_dict': 1}, 'error_address')

    def test_linked_list(self):
        """Тестирование класса LinkedList из src/linked_list.py"""
        # Создаем пустой односвязный список
        ll = LinkedList()
        # Добавляем данные
        ll.insert_at_end({'id': 2})
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        # Проверяем данные списка с помощью магического метода __str__
        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_method_to_list_linked_list(self):
        """Тестируем метод to_list() класса LinkedList из src/linked_list.py"""
        # Создаем пустой односвязный список
        ll = LinkedList()
        # Добавляем данные
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})

        lst = ll.to_list()
        # Тестируем данные, которые вернул метод to_list()
        # Длина списка
        self.assertEqual(len(lst), 4)
        # Несколько значений элементов списка
        self.assertEqual(lst[0]['id'], 0)
        self.assertEqual(lst[1]['username'], 'lazzy508509')
        self.assertEqual(lst[3]['username'], 'mosh_s')

    @patch('builtins.print')
    def test_get_data_by_id_try_except_no_dict(self, mock_print):
        """Тестируем работу блока try ... except в методе get_data_by_id класса LinkedList из src/linked_list.py"""
        error_msg = 'Данные не являются словарем или в словаре нет id'
        # Создаем экземпляр класса LinkedList.
        # Добавляем элементы, один из которых не является словарем
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_beginning('idusername')
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        # Вызываем функции ll_1.get_data_by_id, и перехватываем вызов функции print c аргументом error_mgs,
        # который осуществляется в секции except блока try.
        ll.get_data_by_id(2)
        mock_print.assert_called_with(error_msg)

    @patch('builtins.print')
    def test_get_data_by_id_try_except_no_id(self, mock_print):
        """Тестируем работу блока try ... except в методе get_data_by_id класса LinkedList из src/linked_list.py"""
        error_msg = 'Данные не являются словарем или в словаре нет id'
        # Создаем экземпляр класса LinkedList.
        # Добавляем элементы, один из которых является словарем, в котором нет ключа 'id'
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'ids': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        # Вызываем функции ll_1.get_data_by_id, и перехватываем вызов функции print c аргументом error_mgs,
        # который осуществляется в секции except блока try.
        ll.get_data_by_id(2)
        mock_print.assert_called_with(error_msg)


if __name__ == "__main__":
    unittest.main()
