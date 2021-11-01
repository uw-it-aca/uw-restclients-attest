# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

import json
from restclients_core import models


class Facility(models.Model):
    description = models.CharField(max_length=255)
    facility_code = models.CharField(max_length=32)
    facility_number = models.CharField(max_length=32)
    href = models.CharField(max_length=255)
    name = models.CharField(max_length=128)

    def __init__(self, *args, **kwargs):
        super(Facility, self).__init__(*args, **kwargs)

    @staticmethod
    def from_json(json_data):
        obj = Facility()
        facilitys = json_data.get("facilitys")
        for facility in facilitys:
            obj.facility_code = facility.get("facilityCode")
            obj.facility_number = facility.get("facilityNumber")
            uri = facility.get("facilityURI")
            obj.description = uri.get("description")
            obj.href = uri.get("href")
        return obj

    def json_data(self):
        return {
            "description": self.description,
            "facility_code": self.facility_code,
            "facility_number": self.facility_number,
            "href": self.href,
            "name": self.name
        }

    def __str__(self):
        return json.dumps(self.json_data(), default=str)
