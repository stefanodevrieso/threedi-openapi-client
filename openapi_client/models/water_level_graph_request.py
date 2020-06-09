# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.5   3Di core release: 2.0.9  deployed on:  10:00AM (UTC) on June 9, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class WaterLevelGraphRequest(object):
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
        'start_time': 'int',
        'history_points_limit': 'int',
        'subscribe': 'bool',
        'subscribe_rate_limit': 'float',
        'node_id': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'history_points_limit': 'history_points_limit',
        'subscribe': 'subscribe',
        'subscribe_rate_limit': 'subscribe_rate_limit',
        'node_id': 'node_id'
    }

    def __init__(self, start_time=None, history_points_limit=None, subscribe=None, subscribe_rate_limit=None, node_id=None):  # noqa: E501
        """WaterLevelGraphRequest - a model defined in OpenAPI"""  # noqa: E501

        self._start_time = None
        self._history_points_limit = None
        self._subscribe = None
        self._subscribe_rate_limit = None
        self._node_id = None
        self.discriminator = None

        self.start_time = start_time
        if history_points_limit is not None:
            self.history_points_limit = history_points_limit
        self.subscribe = subscribe
        if subscribe_rate_limit is not None:
            self.subscribe_rate_limit = subscribe_rate_limit
        self.node_id = node_id

    @property
    def start_time(self):
        """Gets the start_time of this WaterLevelGraphRequest.  # noqa: E501

        simulation time in seconds  # noqa: E501

        :return: The start_time of this WaterLevelGraphRequest.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this WaterLevelGraphRequest.

        simulation time in seconds  # noqa: E501

        :param start_time: The start_time of this WaterLevelGraphRequest.  # noqa: E501
        :type: int
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501
        if start_time is not None and start_time < 0:  # noqa: E501
            raise ValueError("Invalid value for `start_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._start_time = start_time

    @property
    def history_points_limit(self):
        """Gets the history_points_limit of this WaterLevelGraphRequest.  # noqa: E501

        Maximum number of points of history to return  # noqa: E501

        :return: The history_points_limit of this WaterLevelGraphRequest.  # noqa: E501
        :rtype: int
        """
        return self._history_points_limit

    @history_points_limit.setter
    def history_points_limit(self, history_points_limit):
        """Sets the history_points_limit of this WaterLevelGraphRequest.

        Maximum number of points of history to return  # noqa: E501

        :param history_points_limit: The history_points_limit of this WaterLevelGraphRequest.  # noqa: E501
        :type: int
        """
        if history_points_limit is not None and history_points_limit > 500:  # noqa: E501
            raise ValueError("Invalid value for `history_points_limit`, must be a value less than or equal to `500`")  # noqa: E501
        if history_points_limit is not None and history_points_limit < 1:  # noqa: E501
            raise ValueError("Invalid value for `history_points_limit`, must be a value greater than or equal to `1`")  # noqa: E501

        self._history_points_limit = history_points_limit

    @property
    def subscribe(self):
        """Gets the subscribe of this WaterLevelGraphRequest.  # noqa: E501

        Subscribe for new results during simulation  # noqa: E501

        :return: The subscribe of this WaterLevelGraphRequest.  # noqa: E501
        :rtype: bool
        """
        return self._subscribe

    @subscribe.setter
    def subscribe(self, subscribe):
        """Sets the subscribe of this WaterLevelGraphRequest.

        Subscribe for new results during simulation  # noqa: E501

        :param subscribe: The subscribe of this WaterLevelGraphRequest.  # noqa: E501
        :type: bool
        """
        if subscribe is None:
            raise ValueError("Invalid value for `subscribe`, must not be `None`")  # noqa: E501

        self._subscribe = subscribe

    @property
    def subscribe_rate_limit(self):
        """Gets the subscribe_rate_limit of this WaterLevelGraphRequest.  # noqa: E501

        Max number of items per second for subscription  # noqa: E501

        :return: The subscribe_rate_limit of this WaterLevelGraphRequest.  # noqa: E501
        :rtype: float
        """
        return self._subscribe_rate_limit

    @subscribe_rate_limit.setter
    def subscribe_rate_limit(self, subscribe_rate_limit):
        """Sets the subscribe_rate_limit of this WaterLevelGraphRequest.

        Max number of items per second for subscription  # noqa: E501

        :param subscribe_rate_limit: The subscribe_rate_limit of this WaterLevelGraphRequest.  # noqa: E501
        :type: float
        """
        if subscribe_rate_limit is not None and subscribe_rate_limit > 2:  # noqa: E501
            raise ValueError("Invalid value for `subscribe_rate_limit`, must be a value less than or equal to `2`")  # noqa: E501
        if subscribe_rate_limit is not None and subscribe_rate_limit < 0.25:  # noqa: E501
            raise ValueError("Invalid value for `subscribe_rate_limit`, must be a value greater than or equal to `0.25`")  # noqa: E501

        self._subscribe_rate_limit = subscribe_rate_limit

    @property
    def node_id(self):
        """Gets the node_id of this WaterLevelGraphRequest.  # noqa: E501


        :return: The node_id of this WaterLevelGraphRequest.  # noqa: E501
        :rtype: int
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this WaterLevelGraphRequest.


        :param node_id: The node_id of this WaterLevelGraphRequest.  # noqa: E501
        :type: int
        """
        if node_id is None:
            raise ValueError("Invalid value for `node_id`, must not be `None`")  # noqa: E501
        if node_id is not None and node_id < 1:  # noqa: E501
            raise ValueError("Invalid value for `node_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._node_id = node_id

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
        if not isinstance(other, WaterLevelGraphRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
