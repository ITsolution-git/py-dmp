#!/usr/bin/env python
#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This example downloads a criteria performance report.

To get report fields, run get_report_fields.py.

The LoadFromStorage method is pulling credentials and properties from a
"googleads.yaml" file. By default, it looks for this file in your home
directory. For more information, see the "Caching authentication information"
section of our README.

"""


import logging
from googleads import adwords

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)


def main(client):
    report_downloader = client.GetReportDownloader(version='v201708')

    report = {
        'reportName': 'Last 7 days CRITERIA_PERFORMANCE_REPORT',
        'dateRangeType': 'LAST_7_DAYS',
        'reportType': 'CRITERIA_PERFORMANCE_REPORT',
        'downloadFormat': 'CSV',
        'selector': {
            'fields': [
                'Date', 'CampaignId', 'CampaignName', 'Cost'
            ]
        }
    }

    report_downloader.DownloadReport(
        report, open('adwords.csv', 'w'), skip_report_header=True,
        skip_column_header=False, skip_report_summary=True,
        include_zero_impressions=True
    )


if __name__ == '__main__':
    adwords_client = adwords.AdWordsClient.LoadFromStorage(
        '/var/www/html/data-management-platform/cssdata/google_adwords/googleads.yaml'
    )

    main(adwords_client)
