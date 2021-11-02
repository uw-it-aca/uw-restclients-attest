# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

import json
from restclients_core import models


class Facility(models.Model):
    facility_code = models.CharField(max_length=32)
    facility_number = models.CharField(max_length=32)
    href = models.CharField(max_length=255)
    latitude = models.CharField(max_length=64)
    longitude = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    site = models.CharField(max_length=96)

    def __init__(self, *args, **kwargs):
        super(Facility, self).__init__(*args, **kwargs)

    def json_data(self):
        return {
            "facility_code": self.facility_code,
            "facility_number": self.facility_number,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "name": self.name,
            "site": self.site,
        }

    def __str__(self):
        return json.dumps(self.json_data(), default=str)
