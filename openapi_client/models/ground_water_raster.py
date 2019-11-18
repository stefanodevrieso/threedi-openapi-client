# coding: utf-8

"""
    3Di API

    3Di simulation API   Framework release: 0.0.19   3Di core release: 2.0.2  deployed on:  03:09PM (UTC) on November 07, 2019  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class GroundWaterRaster(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'url': 'str',
        'simulation': 'str',
        'aggregation_method': 'str',
        'initial_waterlevel': 'str',
        'initial_waterlevel_id': 'str'
    }

    attribute_map = {
        'url': 'url',
        'simulation': 'simulation',
        'aggregation_method': 'aggregation_method',
        'initial_waterlevel': 'initial_waterlevel',
        'initial_waterlevel_id': 'initial_waterlevel_id'
    }

    def __init__(self, url=None, simulation=None, aggregation_method=None, initial_waterlevel=None, initial_waterlevel_id=None):  # noqa: E501
        """GroundWaterRaster - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._simulation = None
        self._aggregation_method = None
        self._initial_waterlevel = None
        self._initial_waterlevel_id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.aggregation_method = aggregation_method
        self.initial_waterlevel = initial_waterlevel
        if initial_waterlevel_id is not None:
            self.initial_waterlevel_id = initial_waterlevel_id

    @property
    def url(self):
        """Gets the url of this GroundWaterRaster.  # noqa: E501


        :return: The url of this GroundWaterRaster.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GroundWaterRaster.


        :param url: The url of this GroundWaterRaster.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this GroundWaterRaster.  # noqa: E501


        :return: The simulation of this GroundWaterRaster.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this GroundWaterRaster.


        :param simulation: The simulation of this GroundWaterRaster.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def aggregation_method(self):
        """Gets the aggregation_method of this GroundWaterRaster.  # noqa: E501


        :return: The aggregation_method of this GroundWaterRaster.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_method

    @aggregation_method.setter
    def aggregation_method(self, aggregation_method):
        """Sets the aggregation_method of this GroundWaterRaster.


        :param aggregation_method: The aggregation_method of this GroundWaterRaster.  # noqa: E501
        :type: str
        """
        if aggregation_method is None:
            raise ValueError("Invalid value for `aggregation_method`, must not be `None`")  # noqa: E501
        allowed_values = ["mean", "max", "min"]  # noqa: E501
        if aggregation_method not in allowed_values:
            raise ValueError(
                "Invalid value for `aggregation_method` ({0}), must be one of {1}"  # noqa: E501
                .format(aggregation_method, allowed_values)
            )

        self._aggregation_method = aggregation_method

    @property
    def initial_waterlevel(self):
        """Gets the initial_waterlevel of this GroundWaterRaster.  # noqa: E501


        :return: The initial_waterlevel of this GroundWaterRaster.  # noqa: E501
        :rtype: str
        """
        return self._initial_waterlevel

    @initial_waterlevel.setter
    def initial_waterlevel(self, initial_waterlevel):
        """Sets the initial_waterlevel of this GroundWaterRaster.


        :param initial_waterlevel: The initial_waterlevel of this GroundWaterRaster.  # noqa: E501
        :type: str
        """
        if initial_waterlevel is None:
            raise ValueError("Invalid value for `initial_waterlevel`, must not be `None`")  # noqa: E501

        self._initial_waterlevel = initial_waterlevel

    @property
    def initial_waterlevel_id(self):
        """Gets the initial_waterlevel_id of this GroundWaterRaster.  # noqa: E501


        :return: The initial_waterlevel_id of this GroundWaterRaster.  # noqa: E501
        :rtype: str
        """
        return self._initial_waterlevel_id

    @initial_waterlevel_id.setter
    def initial_waterlevel_id(self, initial_waterlevel_id):
        """Sets the initial_waterlevel_id of this GroundWaterRaster.


        :param initial_waterlevel_id: The initial_waterlevel_id of this GroundWaterRaster.  # noqa: E501
        :type: str
        """

        self._initial_waterlevel_id = initial_waterlevel_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GroundWaterRaster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
