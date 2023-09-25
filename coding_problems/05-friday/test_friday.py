import pytest

from friday import move_zeroes


def test_nothing_returned():
    assert move_zeroes([0, 1, 2]) is None


def test_basic_test_1():
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    assert nums == [1, 3, 12, 0, 0]


def test_basic_test_2():
    nums = [0]
    move_zeroes(nums)
    assert nums == [0]


@pytest.mark.parametrize("input_nums,moved_nums",
                         [([7, 0, 8, 2, 7, 9, 9, 1, 2, 5, 9, 7, 0, 10, 7, 6, 9, 9, 9, 0, 5, 6, 3, 3, 6, 5], [7, 8, 2, 7, 9, 9, 1, 2, 5, 9, 7, 10, 7, 6, 9, 9, 9, 5, 6, 3, 3, 6, 5, 0, 0, 0]),
                          ([8, 2, 7, 8, 10, 3, 5, 0, 5, 9, 8, 2, 4, 10, 3, 2, 9, 4, 7], [
                           8, 2, 7, 8, 10, 3, 5, 5, 9, 8, 2, 4, 10, 3, 2, 9, 4, 7, 0]),
                             ([3, 10, 6, 1, 10, 7, 7, 4, 8, 8, 10, 1, 7, 4, 10, 7], [
                              3, 10, 6, 1, 10, 7, 7, 4, 8, 8, 10, 1, 7, 4, 10, 7]),
                             ([0, 3, 9, 9, 4, 5, 8, 0, 3, 3, 0, 4, 7, 1, 2, 9, 8, 8, 1, 0, 3, 4, 2, 4, 2, 9, 6, 10, 1, 7, 0, 2, 6, 2, 8, 1, 4, 9, 1, 2, 10, 5], [
                              3, 9, 9, 4, 5, 8, 3, 3, 4, 7, 1, 2, 9, 8, 8, 1, 3, 4, 2, 4, 2, 9, 6, 10, 1, 7, 2, 6, 2, 8, 1, 4, 9, 1, 2, 10, 5, 0, 0, 0, 0, 0]),
                             ([4, 10, 4, 5, 7], [4, 10, 4, 5, 7]),
                             ([0, 3, 0, 0, 5, 5, 4, 2, 4, 3, 8, 10, 10, 2, 0, 3, 4, 8, 3, 8, 10, 5, 3, 8, 0, 3, 8, 8, 10, 6, 8, 2, 4, 7, 9, 10, 5, 4, 3, 2, 7, 1, 9, 4, 6, 5, 1], [
                              3, 5, 5, 4, 2, 4, 3, 8, 10, 10, 2, 3, 4, 8, 3, 8, 10, 5, 3, 8, 3, 8, 8, 10, 6, 8, 2, 4, 7, 9, 10, 5, 4, 3, 2, 7, 1, 9, 4, 6, 5, 1, 0, 0, 0, 0, 0]),
                             ([2, 3, 9, 3, 10, 4, 2, 8, 2, 2, 2, 1, 7, 6, 5, 8, 5, 8, 8, 5, 0, 8, 9, 5, 6, 3, 2, 3, 6, 5, 7, 0, 4, 6, 3, 2], [
                              2, 3, 9, 3, 10, 4, 2, 8, 2, 2, 2, 1, 7, 6, 5, 8, 5, 8, 8, 5, 8, 9, 5, 6, 3, 2, 3, 6, 5, 7, 4, 6, 3, 2, 0, 0]),
                             ([7, 3, 3, 6, 3, 7, 9, 8, 0, 7, 10, 1, 8, 5, 1, 7, 8, 4, 6, 4, 7, 6, 9, 0, 1, 10, 7, 8, 5, 8, 0], [
                              7, 3, 3, 6, 3, 7, 9, 8, 7, 10, 1, 8, 5, 1, 7, 8, 4, 6, 4, 7, 6, 9, 1, 10, 7, 8, 5, 8, 0, 0, 0]),
                             ([2, 9, 4, 1, 0, 6, 3, 7, 9, 1, 0, 10, 6, 3, 9, 1, 10, 5, 2, 3, 9, 1, 9], [
                              2, 9, 4, 1, 6, 3, 7, 9, 1, 10, 6, 3, 9, 1, 10, 5, 2, 3, 9, 1, 9, 0, 0]),
                             ([2, 6, 9, 4, 7, 0, 8, 1, 0, 6, 6, 6, 10, 8, 1, 0, 7, 3, 8, 6, 10, 4, 3, 5, 4, 4, 5, 8, 9, 10, 7, 7, 10, 3, 8, 10, 1, 7, 2, 7, 5, 1, 8, 8], [
                              2, 6, 9, 4, 7, 8, 1, 6, 6, 6, 10, 8, 1, 7, 3, 8, 6, 10, 4, 3, 5, 4, 4, 5, 8, 9, 10, 7, 7, 10, 3, 8, 10, 1, 7, 2, 7, 5, 1, 8, 8, 0, 0, 0]),
                             ([4, 4, 6, 6, 6, 8, 8, 10, 0],
                              [4, 4, 6, 6, 6, 8, 8, 10, 0]),
                             ([5, 6, 2, 7, 7, 10, 5, 5, 7, 7, 5, 4, 2, 3, 0, 3, 4, 5, 7, 6, 5, 0, 7, 5, 2, 1, 9, 10, 7, 10, 2, 2, 6, 10], [
                              5, 6, 2, 7, 7, 10, 5, 5, 7, 7, 5, 4, 2, 3, 3, 4, 5, 7, 6, 5, 7, 5, 2, 1, 9, 10, 7, 10, 2, 2, 6, 10, 0, 0]),
                             ([9, 10, 4, 2, 3, 1, 4, 1, 4, 7, 4, 4, 5, 9, 0, 7, 2, 2, 7, 10, 9, 4], [
                              9, 10, 4, 2, 3, 1, 4, 1, 4, 7, 4, 4, 5, 9, 7, 2, 2, 7, 10, 9, 4, 0]),
                             ([5, 7, 2, 0, 0, 1, 1, 4, 1, 3, 9, 8, 8, 1, 10, 1, 8, 9, 9, 8, 5, 5, 9, 4, 6, 7], [
                              5, 7, 2, 1, 1, 4, 1, 3, 9, 8, 8, 1, 10, 1, 8, 9, 9, 8, 5, 5, 9, 4, 6, 7, 0, 0]),
                             ([5, 3, 5, 8, 10, 8, 2, 6, 9, 8, 3, 2, 9, 10, 10, 8, 0, 1, 2, 2, 0, 0, 1, 10, 5, 8], [
                              5, 3, 5, 8, 10, 8, 2, 6, 9, 8, 3, 2, 9, 10, 10, 8, 1, 2, 2, 1, 10, 5, 8, 0, 0, 0]),
                             ([0, 1], [1, 0]),
                             ([6, 10, 1, 4, 7, 8, 8, 5, 2, 2, 4, 2, 5, 4, 9, 1, 5, 2, 7, 0, 8, 4, 7, 10, 9, 4, 4, 0, 1, 5], [
                              6, 10, 1, 4, 7, 8, 8, 5, 2, 2, 4, 2, 5, 4, 9, 1, 5, 2, 7, 8, 4, 7, 10, 9, 4, 4, 1, 5, 0, 0]),
                             ([9, 0, 1, 1, 0, 9, 6, 9, 2],
                              [9, 1, 1, 9, 6, 9, 2, 0, 0]),
                             ([6, 6, 3, 3, 1, 10, 6, 5, 0, 0, 4, 10, 3, 10, 9, 7, 8], [
                              6, 6, 3, 3, 1, 10, 6, 5, 4, 10, 3, 10, 9, 7, 8, 0, 0]),
                             ([8, 3, 9, 0, 9, 10, 7, 3, 4, 5, 0, 0, 4, 10, 2, 1, 8, 9, 10, 10, 4, 1, 10], [
                              8, 3, 9, 9, 10, 7, 3, 4, 5, 4, 10, 2, 1, 8, 9, 10, 10, 4, 1, 10, 0, 0, 0]),
                             ([3, 0, 4, 4, 7, 4, 2, 6, 1, 7, 4, 10, 7],
                              [3, 4, 4, 7, 4, 2, 6, 1, 7, 4, 10, 7, 0]),
                             ([0, 0, 0, 6, 4, 1, 5, 5, 2, 5, 6, 9, 0, 0, 5, 7, 7, 10, 1, 9, 10, 10, 7], [
                              6, 4, 1, 5, 5, 2, 5, 6, 9, 5, 7, 7, 10, 1, 9, 10, 10, 7, 0, 0, 0, 0, 0]),
                             ([9, 5, 1, 1, 0, 8, 0, 5, 7, 9, 8, 3, 1, 7, 1, 1, 8, 9, 9, 4, 4, 2, 5, 2, 9, 5, 1, 6, 4, 1, 6, 4, 7, 7, 6, 5, 3], [
                              9, 5, 1, 1, 8, 5, 7, 9, 8, 3, 1, 7, 1, 1, 8, 9, 9, 4, 4, 2, 5, 2, 9, 5, 1, 6, 4, 1, 6, 4, 7, 7, 6, 5, 3, 0, 0]),
                             ([10, 0, 4, 10, 8, 0, 3, 9, 2, 5, 3, 3, 10, 0, 7, 6, 1, 5, 5, 0, 5, 4, 4, 5, 0, 2, 8, 2, 0, 9, 9, 5, 9, 5, 3, 2, 9, 9, 3, 4, 0, 7, 9, 5, 0, 0, 10, 8], [
                              10, 4, 10, 8, 3, 9, 2, 5, 3, 3, 10, 7, 6, 1, 5, 5, 5, 4, 4, 5, 2, 8, 2, 9, 9, 5, 9, 5, 3, 2, 9, 9, 3, 4, 7, 9, 5, 10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                             ([2, 10, 9, 1, 1, 1, 8, 2, 0, 9, 7, 6, 8, 6, 4, 4, 5, 2, 8, 10, 8, 5, 7, 5, 8], [
                              2, 10, 9, 1, 1, 1, 8, 2, 9, 7, 6, 8, 6, 4, 4, 5, 2, 8, 10, 8, 5, 7, 5, 8, 0]),
                             ([0, 2, 0, 4, 7, 0, 4, 10, 5, 1, 3, 6, 0, 6, 5, 5, 0, 6, 7, 0, 4, 1, 6, 0, 9, 5, 10, 5, 8, 5, 2, 5, 3, 8, 5, 1, 0], [
                              2, 4, 7, 4, 10, 5, 1, 3, 6, 6, 5, 5, 6, 7, 4, 1, 6, 9, 5, 10, 5, 8, 5, 2, 5, 3, 8, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0]),
                             ([0, 1, 9, 2, 3, 8, 10, 6, 0, 1, 5, 10, 1, 2, 3, 10, 7, 9, 9, 8, 10, 6, 9, 4, 4, 5, 7, 4, 10, 1, 0, 3, 6, 4], [
                              1, 9, 2, 3, 8, 10, 6, 1, 5, 10, 1, 2, 3, 10, 7, 9, 9, 8, 10, 6, 9, 4, 4, 5, 7, 4, 10, 1, 3, 6, 4, 0, 0, 0]),
                             ([10, 8, 3, 9, 7, 10, 9, 7, 1, 6],
                              [10, 8, 3, 9, 7, 10, 9, 7, 1, 6]),
                             ([2, 6, 2, 9, 4, 0], [2, 6, 2, 9, 4, 0]),
                             ([10, 9], [10, 9]),
                             ([6, 3, 1, 7, 7, 9, 10, 4, 7, 3, 9],
                              [6, 3, 1, 7, 7, 9, 10, 4, 7, 3, 9]),
                             ([9, 1, 0, 1, 2, 2, 2, 6, 4, 5, 9, 4, 5, 7, 10, 4, 3, 4, 0, 8, 4, 9, 6, 7, 0, 8, 10, 10, 6, 8, 1, 4, 8, 7, 9, 9, 10, 5, 2, 0, 10, 2, 2, 3, 0, 4, 1, 4], [
                              9, 1, 1, 2, 2, 2, 6, 4, 5, 9, 4, 5, 7, 10, 4, 3, 4, 8, 4, 9, 6, 7, 8, 10, 10, 6, 8, 1, 4, 8, 7, 9, 9, 10, 5, 2, 10, 2, 2, 3, 4, 1, 4, 0, 0, 0, 0, 0]),
                             ([4, 9, 10, 2, 6, 7, 6, 2, 4, 3, 0, 10, 2, 0, 5, 3, 0, 10, 1, 8, 10, 4, 2, 4, 2, 6], [
                              4, 9, 10, 2, 6, 7, 6, 2, 4, 3, 10, 2, 5, 3, 10, 1, 8, 10, 4, 2, 4, 2, 6, 0, 0, 0]),
                             ([4, 5, 5, 4, 1, 3, 0, 8, 0, 6, 10, 1, 1, 0, 6, 9, 9, 3, 10, 2, 8, 3, 5, 3, 0, 7, 7, 7, 0, 6, 0, 0, 10, 10, 10, 3, 5, 9, 0, 5, 8, 5, 9, 1, 3, 8, 10, 10], [
                              4, 5, 5, 4, 1, 3, 8, 6, 10, 1, 1, 6, 9, 9, 3, 10, 2, 8, 3, 5, 3, 7, 7, 7, 6, 10, 10, 10, 3, 5, 9, 5, 8, 5, 9, 1, 3, 8, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0]),
                             ([8, 10, 8, 2, 2, 2, 1, 2, 0, 7, 1, 1, 10, 8],
                              [8, 10, 8, 2, 2, 2, 1, 2, 7, 1, 1, 10, 8, 0]),
                             ([0, 10, 8, 3, 3, 3, 1], [10, 8, 3, 3, 3, 1, 0]),
                             ([6, 4, 9, 1, 9, 0, 4, 10, 2, 0],
                              [6, 4, 9, 1, 9, 4, 10, 2, 0, 0]),
                             ([2, 6, 3, 1, 10, 3, 2, 0, 4, 10, 8, 0, 3, 5],
                              [2, 6, 3, 1, 10, 3, 2, 4, 10, 8, 3, 5, 0, 0]),
                             ([2, 0, 10, 8, 5, 0, 1, 1, 5, 9, 9, 9, 10, 6, 4, 3, 4, 6], [
                              2, 10, 8, 5, 1, 1, 5, 9, 9, 9, 10, 6, 4, 3, 4, 6, 0, 0]),
                             ([3, 7, 0, 1, 3, 4, 4, 0, 3, 2, 10, 3, 7, 9, 4, 10, 9, 10, 10, 5, 1, 9, 8, 8, 1, 10, 4, 2, 5], [3, 7, 1, 3, 4, 4, 3, 2, 10, 3, 7, 9, 4, 10, 9, 10, 10, 5, 1, 9, 8, 8, 1, 10, 4, 2, 5, 0, 0])])
def test_random_test_cases(input_nums, moved_nums):
    nums = input_nums
    move_zeroes(nums)
    assert nums == moved_nums
