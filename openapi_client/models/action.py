# coding: utf-8

"""
    3Di API

    3Di simulation API   Framework release: 0.0.19   3Di core release: 2.0.2  deployed on:  03:09PM (UTC) on November 07, 2019  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Action(object):
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
        'name': 'str',
        'duration': 'int',
        'rate_limit': 'int'
    }

    attribute_map = {
        'name': 'name',
        'duration': 'duration',
        'rate_limit': 'rate_limit'
    }

    def __init__(self, name=None, duration=None, rate_limit=None):  # noqa: E501
        """Action - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._duration = None
        self._rate_limit = None
        self.discriminator = None

        self.name = name
        if duration is not None:
            self.duration = duration
        if rate_limit is not None:
            self.rate_limit = rate_limit

    @property
    def name(self):
        """Gets the name of this Action.  # noqa: E501


        :return: The name of this Action.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Action.


        :param name: The name of this Action.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        allowed_values = ["initialize", "start", "pause", "shutdown"]  # noqa: E501
        if name not in allowed_values:
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"  # noqa: E501
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def duration(self):
        """Gets the duration of this Action.  # noqa: E501

        Only valid for name='start'. Run simulation for given duration (in seconds) and pause  # noqa: E501

        :return: The duration of this Action.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Action.

        Only valid for name='start'. Run simulation for given duration (in seconds) and pause  # noqa: E501

        :param duration: The duration of this Action.  # noqa: E501
        :type: int
        """
        if duration is not None and duration < 1:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `1`")  # noqa: E501

        self._duration = duration

    @property
    def rate_limit(self):
        """Gets the rate_limit of this Action.  # noqa: E501

        Only valid for name='start'. Maximum simulation time in seconds per 1 second real time.   # noqa: E501

        :return: The rate_limit of this Action.  # noqa: E501
        :rtype: int
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        """Sets the rate_limit of this Action.

        Only valid for name='start'. Maximum simulation time in seconds per 1 second real time.   # noqa: E501

        :param rate_limit: The rate_limit of this Action.  # noqa: E501
        :type: int
        """
        if rate_limit is not None and rate_limit < 1:  # noqa: E501
            raise ValueError("Invalid value for `rate_limit`, must be a value greater than or equal to `1`")  # noqa: E501

        self._rate_limit = rate_limit

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
        if not isinstance(other, Action):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other