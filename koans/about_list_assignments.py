#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrayAssignments in the Ruby Koans
#

from runner.koan import *

class AboutListAssignments(Koan):
    def test_non_parallel_assignment(self):
        names = ["John", "Smith"]
        self.assertEqual(["John", "Smith"], names)

    def test_parallel_assignments(self):
        first_name, last_name = ["John", "Smith"]
        # first goes to index 0, sencond to index 1, ect.
        self.assertEqual("John", first_name)
        self.assertEqual("Smith", last_name)

    def test_parallel_assignments_with_extra_values(self):
        title, *first_names, last_name = ["Sir", "Ricky", "Bobby", "Worthington"]
        # *first_names applies to all list items that aren't the first and last items
        self.assertEqual("Sir", title)
        self.assertEqual(["Ricky", "Bobby"], first_names)
        self.assertEqual("Worthington", last_name)

    def test_parallel_assignments_with_fewer_values(self):
        title, *first_names, last_name = ["Mr", "Bond"]
        # title still takes the fist item and last_name still takes the last item. leaving an empty list for *first_names
        self.assertEqual("Mr", title)
        self.assertEqual([], first_names)
        self.assertEqual("Bond", last_name)

    def test_parallel_assignments_with_sublists(self):
        first_name, last_name = [["Willie", "Rae"], "Johnson"]
        # first_name takes the full sublist
        self.assertEqual(["Willie", "Rae"], first_name)
        self.assertEqual("Johnson", last_name)

    def test_swapping_with_parallel_assignment(self):
        first_name = "Roy"
        last_name = "Rob"
        first_name, last_name = last_name, first_name
        #  same as first_name = last_name and last_name = first_name
        self.assertEqual("Rob", first_name)
        self.assertEqual("Roy", last_name)

