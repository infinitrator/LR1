import unittest
from main import two_sum


class TestTwoSum(unittest.TestCase):

    #Базовые рабочие варики
    def test_example_case(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_basic_match(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_non_adjacent(self):
        self.assertEqual(two_sum([1, 5, 3, 7], 10), [1, 3])

    #Пограничные значения
    def test_empty_list(self):
        self.assertIsNone(two_sum([], 0))  # нет элементов вообще

    def test_single_element(self):
        self.assertIsNone(two_sum([42], 42))  # один элемент

    def test_two_elements_match(self):
        self.assertEqual(two_sum([1, 2], 3), [0, 1])

    def test_two_elements_no_match(self):
        self.assertEqual(two_sum([1, 2], 5), [])

    #Списки из одинаковых чисел
    def test_all_same_elements_match(self):
        self.assertEqual(two_sum([5, 5, 5, 5], 10), [0, 1])

    def test_all_same_elements_no_match(self):
        self.assertEqual(two_sum([5, 5, 5, 5], 3), [])

    #Случаи с нулями
    def test_two_zeros_target_zero(self):
        self.assertEqual(two_sum([0, 0], 0), [0, 1])

    def test_zeros_and_other_numbers(self):
        self.assertEqual(two_sum([0, 4, 3, 0], 0), [0, 3])

    #Отрицательные числа
    def test_negative_numbers(self):
        self.assertEqual(two_sum([-1, -2, -3, -4, -5], -8), [2, 4])

    def test_mixed_negative_positive(self):
        self.assertEqual(two_sum([-10, 20, 10, -20], 0), [0, 1])

    def test_negative_target(self):
        self.assertEqual(two_sum([1, 2, 3, -6], -3), [2, 3])

    #Большие числа
    def test_large_numbers(self):
        self.assertEqual(two_sum([10**9, 10**9], 2 * 10**9), [0, 1])

    def test_large_and_small_numbers(self):
        self.assertEqual(two_sum([10**9, -10**9], 0), [0, 1])

    #Несколько возможных решений
    def test_multiple_solutions_first_found(self):
        result = two_sum([1, 2, 3, 4, 5], 6)
        self.assertIn(result, ([0, 4], [1, 3]))  # оба решения валидны

    def test_multiple_pairs_same_target(self):
        result = two_sum([2, 4, 3, 5, 7], 9)
        self.assertIn(result, ([1, 2], [0, 4]))

    #Пытаюсь поломать функцию
    def test_no_solution(self):
        self.assertEqual(two_sum([1, 2, 3], 7), [])

    def test_target_zero_with_no_zeros(self):
        self.assertEqual(two_sum([1, 2, 3], 0), [])

    def test_repeated_elements_but_one_solution(self):
        self.assertEqual(two_sum([2, 2, 3], 5), [0, 2])

    def test_large_list_no_solution(self):
        arr = list(range(1, 10001))  # 1..10000
        self.assertEqual(two_sum(arr, 20001), [])

    def test_large_list_with_solution(self):
        arr = list(range(1, 10001))
        self.assertEqual(two_sum(arr, 19999), [9997, 9998])  # (9998 + 9999)


if __name__ == "__main__":
    unittest.main()