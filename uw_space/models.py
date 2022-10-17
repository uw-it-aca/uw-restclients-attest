# Copyright 2022 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

import json
from restclients_core import models
from uw_space.utils import date_to_str, str_to_datetime


class Facility(models.Model):
    code = models.CharField(max_length=16)
    last_updated = models.DateTimeField()
    latitude = models.CharField(max_length=32)
    longitude = models.CharField(max_length=32)
    name = models.CharField(max_length=96)
    number = models.CharField(max_length=16)
    type = models.CharField(max_length=32)
    site = models.CharField(max_length=96)

    def __init__(self, *args, **kwargs):
        super(Facility, self).__init__(*args, **kwargs)

    @staticmethod
    def from_json(json_data):
        obj = Facility()
        obj.code = json_data.get("facilityCode")
        obj.number = json_data.get("facilityNumber")
        obj.last_updated = str_to_datetime(json_data.get("modifiedDate"))
        obj.name = json_data.get("longName")
        obj.latitude = json_data.get("mapUri", {}).get("latitude")
        obj.longitude = json_data.get("mapUri", {}).get("longitude")
        obj.site = json_data.get("site", {}).get("description")
        obj.type = json_data.get("facilityType", {}).get("description")
        return obj

    def json_data(self):
        return {
            "code": self.code,
            "last_updated": date_to_str(self.last_updated),
            "latitude": self.latitude,
            "longitude": self.longitude,
            "name": self.name,
            "number": self.number,
            "site": self.site,
            "type": self.type,
        }

    def __str__(self):
        return json.dumps(self.json_data(), default=str)
