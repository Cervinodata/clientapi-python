# coding: utf-8

"""
    Cervinodata API documentation

    <div style='margin: 2em 0;'><p>Before you get going with the Cervinodata API, set up Cervinodata (read the support page here: <a href='https://support.cervinodata.com/hc/en-nl/articles/360004363237' target='_blank'>How to set up the Cervinodata API</a>).</p> <h2>To use the Cervinodata API, you need all of the following:</h2> <p> <ol> <li>An active Cervinodata account, you can start a free trial <a href='https://app.cervinodata.com/register' target='_blank'>here</a></li> <li>At least one connection to a platform (check <a href='https://app.cervinodata.com/pages/data-sources/connections' target='_blank'>here</a>)</li> <li>At least one account switched ON (check <a href='https://app.cervinodata.com/pages/data-sources/accounts' target='_blank'>here</a>)</li> <li>At least one data refresh executed (check <a href='https://app.cervinodata.com/pages/data-destinations-api/data-collection' target='_blank'>here</a>)</li> <li>An active API token (check <a href='https://app.cervinodata.com/settings#/api' target='_blank'>here</a>)</li> </ol> </p> </div>  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@cervinodata.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "Cervinodata API Client"
VERSION = "0.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Cervinodata API documentation",
    author="OpenAPI Generator community",
    author_email="support@cervinodata.com",
    url="https://github.com/Cervinodata/clientapi-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Cervinodata API documentation"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description="""\
    &lt;div style&#x3D;&#39;margin: 2em 0;&#39;&gt;&lt;p&gt;Before you get going with the Cervinodata API, set up Cervinodata (read the support page here: &lt;a href&#x3D;&#39;https://support.cervinodata.com/hc/en-nl/articles/360004363237&#39; target&#x3D;&#39;_blank&#39;&gt;How to set up the Cervinodata API&lt;/a&gt;).&lt;/p&gt; &lt;h2&gt;To use the Cervinodata API, you need all of the following:&lt;/h2&gt; &lt;p&gt; &lt;ol&gt; &lt;li&gt;An active Cervinodata account, you can start a free trial &lt;a href&#x3D;&#39;https://app.cervinodata.com/register&#39; target&#x3D;&#39;_blank&#39;&gt;here&lt;/a&gt;&lt;/li&gt; &lt;li&gt;At least one connection to a platform (check &lt;a href&#x3D;&#39;https://app.cervinodata.com/pages/data-sources/connections&#39; target&#x3D;&#39;_blank&#39;&gt;here&lt;/a&gt;)&lt;/li&gt; &lt;li&gt;At least one account switched ON (check &lt;a href&#x3D;&#39;https://app.cervinodata.com/pages/data-sources/accounts&#39; target&#x3D;&#39;_blank&#39;&gt;here&lt;/a&gt;)&lt;/li&gt; &lt;li&gt;At least one data refresh executed (check &lt;a href&#x3D;&#39;https://app.cervinodata.com/pages/data-destinations-api/data-collection&#39; target&#x3D;&#39;_blank&#39;&gt;here&lt;/a&gt;)&lt;/li&gt; &lt;li&gt;An active API token (check &lt;a href&#x3D;&#39;https://app.cervinodata.com/settings#/api&#39; target&#x3D;&#39;_blank&#39;&gt;here&lt;/a&gt;)&lt;/li&gt; &lt;/ol&gt; &lt;/p&gt; &lt;/div&gt;  # noqa: E501
    """
)
