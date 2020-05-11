# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 0.0.48   3Di core release: 2.0.7  deployed on:  02:54PM (UTC) on May 06, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PotentialBreach(object):
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
        'connected_pnt_id': 'int',
        'levee_material': 'str',
        'line_id': 'int',
        'maximum_breach_depth': 'float',
        'threedimodel': 'str',
        'id': 'int'
    }

    attribute_map = {
        'url': 'url',
        'connected_pnt_id': 'connected_pnt_id',
        'levee_material': 'levee_material',
        'line_id': 'line_id',
        'maximum_breach_depth': 'maximum_breach_depth',
        'threedimodel': 'threedimodel',
        'id': 'id'
    }

    def __init__(self, url=None, connected_pnt_id=None, levee_material=None, line_id=None, maximum_breach_depth=None, threedimodel=None, id=None):  # noqa: E501
        """PotentialBreach - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._connected_pnt_id = None
        self._levee_material = None
        self._line_id = None
        self._maximum_breach_depth = None
        self._threedimodel = None
        self._id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.connected_pnt_id = connected_pnt_id
        self.levee_material = levee_material
        self.line_id = line_id
        self.maximum_breach_depth = maximum_breach_depth
        if threedimodel is not None:
            self.threedimodel = threedimodel
        if id is not None:
            self.id = id

    @property
    def url(self):
        """Gets the url of this PotentialBreach.  # noqa: E501


        :return: The url of this PotentialBreach.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PotentialBreach.


        :param url: The url of this PotentialBreach.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def connected_pnt_id(self):
        """Gets the connected_pnt_id of this PotentialBreach.  # noqa: E501


        :return: The connected_pnt_id of this PotentialBreach.  # noqa: E501
        :rtype: int
        """
        return self._connected_pnt_id

    @connected_pnt_id.setter
    def connected_pnt_id(self, connected_pnt_id):
        """Sets the connected_pnt_id of this PotentialBreach.


        :param connected_pnt_id: The connected_pnt_id of this PotentialBreach.  # noqa: E501
        :type: int
        """
        if connected_pnt_id is None:
            raise ValueError("Invalid value for `connected_pnt_id`, must not be `None`")  # noqa: E501
        if connected_pnt_id is not None and connected_pnt_id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `connected_pnt_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if connected_pnt_id is not None and connected_pnt_id < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `connected_pnt_id`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._connected_pnt_id = connected_pnt_id

    @property
    def levee_material(self):
        """Gets the levee_material of this PotentialBreach.  # noqa: E501


        :return: The levee_material of this PotentialBreach.  # noqa: E501
        :rtype: str
        """
        return self._levee_material

    @levee_material.setter
    def levee_material(self, levee_material):
        """Sets the levee_material of this PotentialBreach.


        :param levee_material: The levee_material of this PotentialBreach.  # noqa: E501
        :type: str
        """
        if levee_material is None:
            raise ValueError("Invalid value for `levee_material`, must not be `None`")  # noqa: E501
        allowed_values = ["sand", "clay"]  # noqa: E501
        if levee_material not in allowed_values:
            raise ValueError(
                "Invalid value for `levee_material` ({0}), must be one of {1}"  # noqa: E501
                .format(levee_material, allowed_values)
            )

        self._levee_material = levee_material

    @property
    def line_id(self):
        """Gets the line_id of this PotentialBreach.  # noqa: E501


        :return: The line_id of this PotentialBreach.  # noqa: E501
        :rtype: int
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        """Sets the line_id of this PotentialBreach.


        :param line_id: The line_id of this PotentialBreach.  # noqa: E501
        :type: int
        """
        if line_id is None:
            raise ValueError("Invalid value for `line_id`, must not be `None`")  # noqa: E501
        if line_id is not None and line_id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `line_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if line_id is not None and line_id < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `line_id`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._line_id = line_id

    @property
    def maximum_breach_depth(self):
        """Gets the maximum_breach_depth of this PotentialBreach.  # noqa: E501


        :return: The maximum_breach_depth of this PotentialBreach.  # noqa: E501
        :rtype: float
        """
        return self._maximum_breach_depth

    @maximum_breach_depth.setter
    def maximum_breach_depth(self, maximum_breach_depth):
        """Sets the maximum_breach_depth of this PotentialBreach.


        :param maximum_breach_depth: The maximum_breach_depth of this PotentialBreach.  # noqa: E501
        :type: float
        """
        if maximum_breach_depth is None:
            raise ValueError("Invalid value for `maximum_breach_depth`, must not be `None`")  # noqa: E501

        self._maximum_breach_depth = maximum_breach_depth

    @property
    def threedimodel(self):
        """Gets the threedimodel of this PotentialBreach.  # noqa: E501


        :return: The threedimodel of this PotentialBreach.  # noqa: E501
        :rtype: str
        """
        return self._threedimodel

    @threedimodel.setter
    def threedimodel(self, threedimodel):
        """Sets the threedimodel of this PotentialBreach.


        :param threedimodel: The threedimodel of this PotentialBreach.  # noqa: E501
        :type: str
        """

        self._threedimodel = threedimodel

    @property
    def id(self):
        """Gets the id of this PotentialBreach.  # noqa: E501


        :return: The id of this PotentialBreach.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PotentialBreach.


        :param id: The id of this PotentialBreach.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if not isinstance(other, PotentialBreach):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
