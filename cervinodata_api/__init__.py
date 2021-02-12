# coding: utf-8

# flake8: noqa

"""
    Cervinodata API documentation

    <div style='margin: 2em 0;'>  <p>  Before you get going with the Cervinodata API, set up Cervinodata (read the support page here: <a href='https://support.cervinodata.com/hc/en-nl/articles/360004363237' target='_blank'>How to set up the Cervinodata API</a>).  </p> <h3>To use the Cervinodata API, you need all of the following:</h3> <p> <ol> <li>An active Cervinodata account, you can start a free trial <a href='https://app.cervinodata.com/register' target='_blank'>here</a></li> <li>At least one connection to a platform (check <a href='https://app.cervinodata.com/data-sources-connections' target='_blank'>here</a>)</li> <li>At least one account switched ON (check <a href='https://app.cervinodata.com/accounts' target='_blank'>here</a>)</li> <li>At least one data refresh executed (check <a href='https://app.cervinodata.com/manual-data-refresh' target='_blank'>here</a>)</li> <li>An active API token (check <a href='https://app.cervinodata.com/settings#/api' target='_blank'>here</a>)</li> </ol> </p> <p> Note that limits apply for <a href='https://support.cervinodata.com/hc/articles/360014265139' target='_blank'>Free plan users</a>. </p> <p> If you wish to automate your Cervinodata API connection, check out the list of client API's at <a href='https://github.com/Cervinodata' target='_blank'>https://github.com/Cervinodata</a>. </p> </div>  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@cervinodata.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "0.1.0"

# import apis into sdk package
from cervinodata_api.api.advertising_data_api import AdvertisingDataApi
from cervinodata_api.api.analytics_data_api import AnalyticsDataApi
from cervinodata_api.api.analytics_data_default_metrics_api import AnalyticsDataDefaultMetricsApi
from cervinodata_api.api.analytics_data_goals_api import AnalyticsDataGoalsApi
from cervinodata_api.api.campaign_group_api import CampaignGroupApi
from cervinodata_api.api.generic_data_api import GenericDataApi

# import ApiClient
from cervinodata_api.api_client import ApiClient
from cervinodata_api.configuration import Configuration
from cervinodata_api.exceptions import OpenApiException
from cervinodata_api.exceptions import ApiTypeError
from cervinodata_api.exceptions import ApiValueError
from cervinodata_api.exceptions import ApiKeyError
from cervinodata_api.exceptions import ApiAttributeError
from cervinodata_api.exceptions import ApiException
# import models into sdk package

