
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.advertising_data_api import AdvertisingDataApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from cervinodata_api.api.advertising_data_api import AdvertisingDataApi
from cervinodata_api.api.analytics_data_api import AnalyticsDataApi
from cervinodata_api.api.analytics_data_default_metrics_api import AnalyticsDataDefaultMetricsApi
from cervinodata_api.api.analytics_data_goals_api import AnalyticsDataGoalsApi
from cervinodata_api.api.campaign_group_api import CampaignGroupApi
from cervinodata_api.api.generic_data_api import GenericDataApi
