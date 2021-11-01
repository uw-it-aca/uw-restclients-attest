# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

"""
This is the interface for interacting with the Attesttation Web Service.
"""
import json
import logging
from restclients_core.exceptions import DataFailureException
from uw_space.dao import SPACE_DAO
from uw_space.models import Facility

facility_api = "facility?facility_code={}"
logger = logging.getLogger(__name__)


class Facility(object):

    def __init__(self):
        self.dao = SPACE_DAO()
        self._read_headers = {"Accept": "application/json"}

    def search(self, facility_code):
        """
        facility_code: string
        """
        url = facility_api.format(facility_code)
        response = self.dao.getURL(url, self._read_headers)
        logger.debug(
            {'url': url, 'status': response.status, 'data': response.data})
        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)
        return Facility.from_json(json.loads(response.data))
