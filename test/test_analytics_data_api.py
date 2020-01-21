# coding: utf-8

"""
    Cervinodata API documentation

    <div style='margin: 2em 0;'><p>Before you get going with the Cervinodata API, set up Cervinodata (read the support page here: <a href='https://support.cervinodata.com/hc/en-nl/articles/360004363237' target='_blank'>How to set up the Cervinodata API</a>).</p> <h2>To use the Cervinodata API, you need all of the following:</h2> <p> <ol> <li>An active Cervinodata account, you can start a free trial <a href='https://app.cervinodata.com/register' target='_blank'>here</a></li> <li>At least one connection to a platform (check <a href='https://app.cervinodata.com/pages/data-sources/connections' target='_blank'>here</a>)</li> <li>At least one account switched ON (check <a href='https://app.cervinodata.com/pages/data-sources/accounts' target='_blank'>here</a>)</li> <li>At least one data refresh executed (check <a href='https://app.cervinodata.com/pages/data-destinations-api/data-collection' target='_blank'>here</a>)</li> <li>An active API token (check <a href='https://app.cervinodata.com/settings#/api' target='_blank'>here</a>)</li> </ol> </p> </div>  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@cervinodata.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import cervinodata_api
from cervinodata_api.api.analytics_data_api import AnalyticsDataApi  # noqa: E501
from cervinodata_api.rest import ApiException


class TestAnalyticsDataApi(unittest.TestCase):
    """AnalyticsDataApi unit test stubs"""

    def setUp(self):
        self.api = cervinodata_api.api.analytics_data_api.AnalyticsDataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_views(self):
        """Test case for get_views

        Return views by organisation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
