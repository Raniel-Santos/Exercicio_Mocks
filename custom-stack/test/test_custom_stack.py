import pytest
from unittest.mock import patch, MagicMock
from custom_stack.custom_stack_class import CustomStack, StackEmptyException, StackFullException, NumberAscOrder

def test_push():
    stack = CustomStack(3)
    stack.push(1)
    assert stack.size() == 1
    stack.push(2)
    assert stack.size() == 2
    stack.push(3)
    assert stack.size() == 3

    with pytest.raises(StackFullException):
        stack.push(4)

def test_pop():
    stack = CustomStack(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1

    with pytest.raises(StackEmptyException):
        stack.pop()

def test_top():
    stack = CustomStack(3)
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    assert stack.size() == 2

    stack.pop()
    assert stack.top() == 1
    assert stack.size() == 1

    stack.pop()
    with pytest.raises(StackEmptyException):
        stack.top()

def test_size_and_isEmpty():
    stack = CustomStack(3)
    assert stack.size() == 0
    assert stack.isEmpty() == True

    stack.push(1)
    assert stack.size() == 1
    assert stack.isEmpty() == False

    stack.pop()
    assert stack.size() == 0
    assert stack.isEmpty() == True

#---------- Testes EX_02 ----------

def test_sort_with_numbers():
    stack = CustomStack(6)
    numbers = [5, 2, 8, 3, 1, 7]
    for num in numbers:
        stack.push(num)


    with patch.object(NumberAscOrder, 'sort') as mock_sort:
        # "Mocka" os argumentos do método sort
        mock_sort.return_value = [1, 2, 3, 5, 7, 8]
        sorted_numbers = NumberAscOrder.sort(stack)
        assert sorted_numbers == [1, 2, 3, 5, 7, 8]
        mock_sort.assert_called_once_with(stack)

def test_sort_with_empty_stack():
    stack = CustomStack(6)
    # "Mocka" os argumentos do método sort
    with patch.object(NumberAscOrder, 'sort') as mock_sort:
        # Mocka o retorno do método sort
        mock_sort.return_value = []
        sorted_numbers = NumberAscOrder.sort(stack)
        assert sorted_numbers == []
        mock_sort.assert_called_once_with(stack)

def test_sort_with_duplicates():
    stack = CustomStack(6)
    numbers = [3, 2, 5, 2, 3, 5]
    for num in numbers:
        stack.push(num)

    with patch.object(NumberAscOrder, 'sort') as mock_sort:
        # "Mocka" os argumentos do método sort
        mock_sort.return_value = [2, 2, 3, 3, 5, 5]
        sorted_numbers = NumberAscOrder.sort(stack)
        assert sorted_numbers == [2, 2, 3, 3, 5, 5]
        mock_sort.assert_called_once_with(stack)

def test_sort_with_descending_order():
    stack = CustomStack(6)
    numbers = [6, 5, 4, 3, 2, 1]
    for num in numbers:
        stack.push(num)


    with patch.object(NumberAscOrder, 'sort') as mock_sort:
        # "Mocka" os argumentos do método sort
        mock_sort.return_value = [1, 2, 3, 4, 5, 6]
        sorted_numbers = NumberAscOrder.sort(stack)
        assert sorted_numbers == [1, 2, 3, 4, 5, 6]

        mock_sort.assert_called_once_with(stack)
