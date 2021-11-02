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

facility_api = "/space/v1/facility.json?facility_code={}"
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
        return __process_json(json.loads(response.data))

    def __process_json(jdata):
        facilitys = json_data.get("Facilitys")
        for facility in facilitys:
            obj = Facility()
            obj.facility_code = facility.get("FacilityCode")
            obj.facility_number = facility.get("AggregateFacilityNumber")
            furi = facility.get("FacilityURI")
            if furi:
                obj.href = furi.get("Href")
                building_resp = self.dao.getURL(obj.href, self._read_headers)
                if building_resp.status != 200:
                    raise DataFailureException(url, building_resp.status, building_resp.data)

                bd_json = json.loads(building_resp.data)
                obj.name = bd_json.get("LongName")
                cpoint = bd_json.get("CenterPoint")
                if cpoint:
                    obj.latitude = cpoint.get("Latitude")
                    obj.longitude = cpoint.get("Longitude")
                site_json = bd_json.get("Site")
                if site_json:
                    obj.site = site_json.get("Description")
