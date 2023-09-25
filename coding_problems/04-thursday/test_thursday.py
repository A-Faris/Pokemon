import pytest

from thursday import missing_number


def test_basic_test_1():
    assert missing_number([3, 0, 1]) == 2


def test_basic_test_2():
    assert missing_number([0, 1]) == 2


def test_basic_test_3():
    assert missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


@pytest.mark.parametrize("nums,missing_num",
                         [([15, 9, 22, 23, 32, 25, 17, 11, 8, 27, 19, 34, 29, 30, 20, 16, 36, 26, 1, 6, 33, 5, 37, 24, 4, 12, 28, 14, 3, 13, 2, 18, 21, 10, 35, 0, 7], 31),
                          ([28, 17, 38, 27, 10, 18, 31, 21, 29, 23, 8, 11, 6, 13, 34, 22, 9, 14, 1,
                            25, 3, 33, 35, 37, 26, 19, 0, 5, 12, 4, 24, 36, 30, 20, 32, 15, 7, 2], 16),
                             ([9, 19, 3, 6, 14, 1, 10, 7, 17, 5, 12,
                              0, 4, 15, 16, 2, 8, 18, 20, 13], 11),
                             ([13, 19, 23, 5, 1, 22, 16, 21, 20, 11, 7, 0, 6,
                              9, 3, 24, 17, 8, 4, 12, 18, 15, 25, 10, 2], 14),
                             ([20, 30, 24, 28, 10, 14, 1, 29, 3, 25, 26, 39, 44, 16, 12, 31, 22, 19, 5, 21, 13, 37,
                              17, 8, 7, 33, 40, 36, 4, 0, 32, 23, 27, 35, 43, 42, 2, 41, 6, 11, 34, 18, 9, 38], 15),
                             ([37, 25, 36, 24, 16, 6, 42, 34, 11, 20, 0, 29, 27, 3, 7, 15, 17, 18, 43, 13, 23, 12,
                              28, 39, 4, 5, 19, 9, 31, 26, 2, 22, 8, 33, 41, 10, 38, 1, 35, 21, 32, 30, 14], 40),
                             ([1], 0),
                             ([30, 16, 32, 40, 11, 2, 36, 37, 19, 41, 13, 22, 4, 29, 9, 27, 17, 18, 25, 28, 3,
                              42, 0, 31, 7, 15, 39, 35, 1, 10, 38, 12, 14, 26, 21, 23, 34, 33, 8, 24, 20, 5], 6),
                             ([37, 15, 30, 6, 26, 35, 33, 32, 5, 12, 16, 20, 38, 0, 39, 18, 24, 13, 36, 28,
                              25, 4, 17, 8, 7, 29, 27, 11, 9, 19, 10, 2, 3, 34, 1, 14, 23, 31, 22], 21),
                             ([19, 7, 26, 12, 40, 43, 38, 39, 36, 23, 4, 9, 14, 29, 16, 2, 11, 31, 42, 1, 41, 24, 44,
                              28, 5, 25, 3, 35, 0, 22, 13, 6, 17, 20, 10, 32, 33, 15, 18, 8, 27, 30, 34, 21], 37),
                             ([4, 3, 0, 2], 1),
                             ([25, 18, 4, 39, 17, 38, 14, 35, 37, 23, 3, 9, 10, 40, 29, 30, 36, 8, 20, 34,
                              13, 33, 7, 12, 19, 11, 0, 16, 27, 22, 26, 5, 32, 28, 24, 2, 1, 6, 15, 31], 21),
                             ([7, 6, 3, 5, 8, 4, 2, 0], 1),
                             ([1, 0, 3, 2], 4),
                             ([12, 11, 8, 19, 27, 30, 2, 24, 10, 21, 6, 9, 1, 7, 20, 4,
                              15, 25, 17, 26, 22, 29, 16, 14, 23, 0, 18, 28, 3, 13], 5),
                             ([22, 21, 24, 13, 23, 15, 0, 2, 6, 8, 25, 5, 10,
                              16, 9, 3, 20, 1, 17, 4, 18, 14, 19, 7, 12], 11),
                             ([15, 5, 9, 3, 29, 21, 41, 27, 25, 18, 26, 22, 1, 19, 12, 40, 8, 0, 31, 20, 4, 33,
                              39, 35, 6, 23, 2, 13, 36, 7, 16, 24, 34, 11, 10, 17, 28, 38, 37, 14, 30], 32),
                             ([12, 8, 9, 14, 5, 4, 2, 3, 6,
                              15, 16, 11, 0, 1, 7, 10], 13),
                             ([1, 8, 7, 2, 3, 9, 5, 0, 4], 6),
                             ([31, 33, 4, 13, 8, 5, 21, 3, 25, 32, 29, 28, 23, 7, 27, 16, 0,
                              1, 10, 15, 26, 9, 14, 18, 6, 24, 12, 22, 20, 2, 11, 17, 19], 30),
                             ([0, 6, 7, 19, 13, 1, 10, 21, 3, 2, 18,
                              8, 14, 17, 16, 11, 4, 15, 5, 12, 9], 20),
                             ([17, 12, 2, 8, 9, 6, 13, 10, 3, 16, 20,
                              18, 1, 11, 19, 4, 7, 5, 14, 0, 15], 21),
                             ([17, 16, 26, 24, 19, 1, 33, 38, 34, 11, 18, 6, 41, 9, 42, 3, 20, 13, 4, 14, 25, 22,
                              15, 7, 31, 8, 29, 28, 35, 36, 30, 0, 37, 27, 23, 40, 12, 2, 32, 39, 10, 21], 5),
                             ([11, 6, 5, 12, 1, 2, 8, 4, 10, 9, 3, 0, 7], 13),
                             ([12, 11, 16, 9, 10, 8, 4, 7,
                              5, 1, 14, 0, 2, 6, 15, 13], 3),
                             ([43, 34, 35, 6, 39, 4, 31, 25, 20, 22, 8, 45, 41, 0, 28, 13, 2, 33, 24, 27, 1, 36, 32, 14,
                              19, 29, 10, 30, 9, 26, 40, 38, 44, 15, 7, 3, 16, 5, 18, 23, 11, 46, 47, 17, 12, 21, 37], 42),
                             ([14, 1, 7, 15, 2, 17, 20, 19, 16, 4, 3,
                              9, 8, 18, 13, 5, 12, 6, 11, 21, 10], 0),
                             ([7, 3, 4, 6, 10, 9, 5, 14, 13, 12, 2, 15, 0, 11, 8], 1),
                             ([25, 0, 1, 7, 13, 2, 14, 16, 24, 21, 22, 26, 10, 28,
                              6, 3, 18, 19, 27, 12, 23, 4, 15, 11, 20, 9, 8, 5], 17),
                             ([14, 21, 12, 24, 20, 30, 27, 8, 18, 19, 5, 1, 2, 11, 0, 9,
                              4, 28, 13, 10, 3, 16, 17, 25, 7, 6, 29, 26, 15, 22], 23),
                             ([5, 3, 1, 0, 2], 4),
                             ([26, 11, 22, 0, 20, 13, 3, 10, 18, 2, 5, 17, 16,
                              4, 1, 6, 21, 9, 24, 7, 14, 8, 19, 15, 25, 12], 23),
                             ([11, 21, 2, 13, 24, 22, 1, 19, 10, 0, 14, 16, 26, 23,
                              4, 6, 17, 9, 5, 8, 3, 18, 27, 20, 25, 7, 15], 12),
                             ([3, 10, 0, 7, 8, 9, 4, 2, 12,
                              13, 6, 1, 5, 14, 15, 11], 16),
                             ([0, 7, 6, 12, 17, 19, 9, 29, 11, 3, 37, 15, 35, 22, 25, 2, 38, 18, 16, 36, 13,
                              32, 28, 31, 4, 24, 30, 10, 34, 5, 20, 33, 21, 8, 23, 40, 27, 14, 1, 39], 26),
                             ([30, 15, 1, 2, 7, 22, 17, 18, 10, 19, 9, 23, 6, 11, 27, 4, 31,
                              13, 16, 14, 5, 0, 24, 21, 29, 12, 3, 20, 28, 8, 32, 25], 26),
                             ([1, 2], 0),
                             ([11, 1, 12, 10, 9, 8, 0, 4, 5, 7, 15, 3, 6, 13, 14], 2),
                             ([32, 16, 30, 9, 24, 33, 39, 20, 17, 12, 6, 25, 36, 13, 26, 22, 34, 23, 0, 31,
                              35, 15, 21, 4, 14, 19, 3, 8, 27, 38, 11, 37, 29, 18, 1, 10, 28, 7, 5], 2),
                             ([5, 17, 6, 8, 7, 19, 11, 16, 4, 21, 14, 13, 9, 20, 18, 3, 1, 2, 12, 10, 15], 0)])
def test_random_test_cases(nums, missing_num):
    assert missing_number(nums) == missing_num
