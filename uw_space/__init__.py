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
from uw_space.utils import str_to_datetime

by_code_path = "/space/v1/facility.json?facility_code={}"
by_number_path = "/space/v1/facility/{}.json"
logger = logging.getLogger(__name__)


class Facility(object):

    def __init__(self):
        self.dao = SPACE_DAO()
        self._read_headers = {"Accept": "application/json"}

    def search_by_code(self, facility_code):
        """
        facility_code: string
        """
        url = by_code_path.format(facility_code)
        response = self.dao.getURL(url, self._read_headers)
        logger.debug(
            {'url': url, 'status': response.status, 'data': response.data})
        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)
        return self.__process_json(json.loads(response.data))

    def search_by_number(self, facility_number):
        """
        facility_number: string
        """
        url = by_number_path.format(facility_number)
        response = self.dao.getURL(url, self._read_headers)
        logger.debug(
            {'url': url, 'status': response.status, 'data': response.data})
        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)
        return self.__process_map_json(json.loads(response.data))

    def __process_json(self, jdata):
        objs = []
        facilitys = json_data.get("Facilitys")
        for facility in facilitys:
            furi = facility.get("FacilityURI")
            if furi:
                url = furi.get("Href")
                building_resp = self.dao.getURL(url, self._read_headers)
                if building_resp.status != 200:
                    raise DataFailureException(
                        url, building_resp.status, building_resp.data)
                obj = self.__process_map_json(json.loads(building_resp.data))
                objs.append(obj)
        return objs

    def __process_map_json(self, jdata):
        obj = Facility()
        obj.facility_code = jdata.get("FacilityCode")
        obj.facility_number = jdata.get("AggregateFacilityNumber")
        obj.name = jdata.get("LongName")
        cpoint = jdata.get("CenterPoint")
        if cpoint:
            obj.latitude = cpoint.get("Latitude")
            obj.longitude = cpoint.get("Longitude")
        site_json = jdata.get("Site")
        if site_json:
            obj.site = site_json.get("Description")
        obj.last_updated = str_to_datetime(jdata.get("ModifiedDate"))
        return obj
