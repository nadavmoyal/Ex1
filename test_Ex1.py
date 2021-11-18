from unittest import TestCase
import pandas as pd

from AllInOne import building, elevator, elevator_call
from Ex1 import Ex1


class Test(TestCase):
    def test_Ex1(self):
        # create a csv file for the elev calls this is just for the len of the call for line 16
        e1 = elevator_call('Calls_a.csv')
        # df_from_ex1 = Ex1('B1.json', 'Calls_a.csv', 'Calls_a.csv')
        # print(f'===================={type(df_from_ex1)}')

        # this list will have all zero, this is because we want to test that if we have one elev
        # we get all of them to be allocated to elev zero
        expected_lst = [0] * len(e1.src)
        # we get the csv file from our code and put it in var csv_to_check( i not sure if we get it as a data frame
        # if i will print line 14 it will give NONE but all the things still run good
        csv_to_check = pd.read_csv('out.csv', header=None)

        # enter all of our allocate that we got from our code into a list actual_lst
        # with for loop
        actual_lst = []
        for i in range(len(csv_to_check)):
            actual_lst.append(csv_to_check.iloc[i, 5])
        # print(f'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^68{actual_lst}\n'
        #       f'and the len is: {len(actual_lst)}')
        # print(f'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6{expected_lst}\n'
        #       f'and the len is: {len(expected_lst)}')

        # compare both of the list we got 'actual_lst' & 'expected_lst'
        is_eq = TestCase()
        is_eq.assertListEqual(actual_lst, expected_lst)

    # ================================================
    # actualOptions = ['html', 'css', 'JavaScript', 'php']
    # expectedOptions = ['html', 'css', 'JavaScript', 'php']
    #
    # print(actualOptions)
    # print(expectedOptions)
    #
    # # tc = unittest.TestCase()
    # tc.assertListEqual(actualOptions, expectedOptions)

    # Or simply like this:
    # unittest.TestCase().assertListEqual(actualOptions, expectedOptions)
    # ====================================================================
