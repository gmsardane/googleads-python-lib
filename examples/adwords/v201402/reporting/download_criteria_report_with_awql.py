#!/usr/bin/python
#
# Copyright 2014 Google Inc. All Rights Reserved.
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

"""This example downloads a criteria performance report with AWQL.

To get report fields, run get_report_fields.py.

Tags: ReportDefinitionService.mutate
Api: AdWordsOnly
"""

__author__ = ('api.kwinter@gmail.com (Kevin Winter)'
              'Joseph DiLallo')

from googleads import adwords


# Specify where to download the file here.
PATH = '/tmp/report_download.csv'


def main(client, path):
  # Initialize appropriate service.
  report_downloader = client.GetReportDownloader(version='v201402')

  # Create report query.
  report_query = ('SELECT CampaignId, AdGroupId, Id, Criteria, CriteriaType, '
                  'Impressions, Clicks, Cost '
                  'FROM CRITERIA_PERFORMANCE_REPORT '
                  'WHERE Status IN [ACTIVE, PAUSED] '
                  'DURING LAST_7_DAYS')

  with open(path, 'w') as output_file:
    report_downloader.DownloadReportWithAwql(report_query, 'CSV', output_file)

  print 'Report was downloaded to \'%s\'.' % path


if __name__ == '__main__':
  # Initialize client object.
  adwords_client = adwords.AdWordsClient.LoadFromStorage()

  main(adwords_client, PATH)
