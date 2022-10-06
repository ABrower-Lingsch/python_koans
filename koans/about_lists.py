#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrays in the Ruby Koans
#

from runner.koan import *

class AboutLists(Koan):
    def test_creating_lists(self):
        empty_list = list()
        self.assertEqual(list, type(empty_list))
        # an empty list has a length of 0 because there are no items to be counted in it
        self.assertEqual(0, len(empty_list))

    def test_list_literals(self):
        nums = list()
        self.assertEqual([], nums)

        nums[0:] = [1]
        self.assertEqual([1], nums)

        nums[1:] = [2]
        self.assertListEqual([1, 2], nums)

        nums.append(333)
        #  adds item to the end of the list
        self.assertListEqual([1, 2, 333], nums)

    def test_accessing_list_elements(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual('peanut', noms[0])
        self.assertEqual('jelly', noms[3])
        # negatives start from the back of the list
        self.assertEqual('jelly', noms[-1])
        self.assertEqual('butter', noms[-3])

    def test_slicing_lists(self):
        noms = ['peanut', 'butter', 'and', 'jelly']
        # [starts from this location : end at this location]
        self.assertEqual(['peanut'], noms[0:1])
        self.assertEqual(['peanut', 'butter'], noms[0:2])
        self.assertEqual([], noms[2:2])
        # if end is longer than list, it goes to the end of the list
        self.assertEqual(['and', 'jelly'], noms[2:20])
        self.assertEqual([], noms[4:0])
        self.assertEqual([], noms[4:100])
        self.assertEqual([], noms[5:0])

    def test_slicing_to_the_edge(self):
        noms = ['peanut', 'butter', 'and', 'jelly']
        
        self.assertEqual(['and', 'jelly'], noms[2:])
        # goes to end ^
        self.assertEqual(['peanut', 'butter'], noms[:2])
        # starts are beginnig ^

    def test_lists_and_ranges(self):
        # if start point isn't defined, always starts with 0. Excludes end point.
        self.assertEqual(range, type(range(5)))
        self.assertNotEqual([1, 2, 3, 4, 5], range(1,6))
        self.assertEqual([0, 1, 2, 3, 4], list(range(5)))
        self.assertEqual([5, 6, 7, 8], list(range(5, 9)))

    def test_ranges_with_steps(self):
        # third number defines increments . negatives count backwards
        self.assertEqual([5, 4], list(range(5, 3, -1)))
        self.assertEqual([0, 2, 4, 6], list(range(0, 8, 2)))
        self.assertEqual([1, 4, 7], list(range(1, 8, 3)))
        self.assertEqual([5, 1, -3], list(range(5, -7, -4)))
        self.assertEqual([5, 1, -3, -7], list(range(5, -8, -4)))

    def test_insertions(self):
        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not')
        self.assertEqual(['you', 'shall', 'not', 'pass'], knight)
        # inserts in front of the item at the given index
        knight.insert(0, 'Arthur')
        self.assertEqual(['Arthur', 'you', 'shall', 'not', 'pass'], knight)

    def test_popping_lists(self):
        stack = [10, 20, 30, 40]
        stack.append('last')

        self.assertEqual([10, 20, 30, 40, 'last'], stack)
        # .pop() removes last item from list
        popped_value = stack.pop()
        self.assertEqual('last', popped_value)
        self.assertEqual([10, 20, 30, 40], stack)
        # .pop(i) removes item at the given index
        popped_value = stack.pop(1)
        self.assertEqual(20, popped_value)
        self.assertEqual([10, 30, 40], stack)

        # Notice that there is a "pop" but no "push" in python?

        # Part of the Python philosophy is that there ideally should be one and
        # only one way of doing anything. A 'push' is the same as an 'append'.

        # To learn more about this try typing "import this" from the python
        # console... ;)

    def test_making_queues(self):
        queue = [1, 2]
        queue.append('last')

        self.assertEqual([1, 2, 'last'], queue)

        popped_value = queue.pop(0)
        self.assertEqual(1, popped_value)
        self.assertEqual([2, 'last'], queue)

        # Note, popping from the left hand side of a list is
        # inefficient. Use collections.deque instead.

