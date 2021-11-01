# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase
import mock
from commonconf import override_settings
from restclients_core.exceptions import DataFailureException
from uw_space.dao import SPACE_DAO
from uw_space.utils import fdao_space_override


@fdao_space_override
class TestSpace(TestCase):

    def test_auth_header(self, mock_get_auth_token):
        headers = SPACE_DAO()._custom_headers("GET", "/", {}, "")
