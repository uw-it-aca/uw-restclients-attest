# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase
from restclients_core.exceptions import DataFailureException
from uw_space import Facility
from uw_space.utils import fdao_space_override


@fdao_space_override
class TestSpace(TestCase):
    def test_search_facility(self):
        att = Facility()
        self.assertEqual(
            result.json_data(),
            {}
        )
