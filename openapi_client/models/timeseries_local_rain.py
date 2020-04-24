# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 0.0.43   3Di core release: 2.0.7  deployed on:  10:00AM (UTC) on April 24, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class TimeseriesLocalRain(object):
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
        'offset': 'int',
        'values': 'list[list[float]]',
        'interpolate': 'bool',
        'units': 'str',
        'diameter': 'int',
        'point': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'url': 'url',
        'simulation': 'simulation',
        'offset': 'offset',
        'values': 'values',
        'interpolate': 'interpolate',
        'units': 'units',
        'diameter': 'diameter',
        'point': 'point',
        'uid': 'uid'
    }

    def __init__(self, url=None, simulation=None, offset=None, values=None, interpolate=None, units=None, diameter=None, point=None, uid=None):  # noqa: E501
        """TimeseriesLocalRain - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._simulation = None
        self._offset = None
        self._values = None
        self._interpolate = None
        self._units = None
        self._diameter = None
        self._point = None
        self._uid = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.offset = offset
        self.values = values
        if interpolate is not None:
            self.interpolate = interpolate
        if units is not None:
            self.units = units
        self.diameter = diameter
        self.point = point
        if uid is not None:
            self.uid = uid

    @property
    def url(self):
        """Gets the url of this TimeseriesLocalRain.  # noqa: E501


        :return: The url of this TimeseriesLocalRain.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TimeseriesLocalRain.


        :param url: The url of this TimeseriesLocalRain.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this TimeseriesLocalRain.  # noqa: E501


        :return: The simulation of this TimeseriesLocalRain.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this TimeseriesLocalRain.


        :param simulation: The simulation of this TimeseriesLocalRain.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def offset(self):
        """Gets the offset of this TimeseriesLocalRain.  # noqa: E501

        offset of event in simulation in seconds  # noqa: E501

        :return: The offset of this TimeseriesLocalRain.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TimeseriesLocalRain.

        offset of event in simulation in seconds  # noqa: E501

        :param offset: The offset of this TimeseriesLocalRain.  # noqa: E501
        :type: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501
        if offset is not None and offset > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if offset is not None and offset < 0:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset = offset

    @property
    def values(self):
        """Gets the values of this TimeseriesLocalRain.  # noqa: E501


        :return: The values of this TimeseriesLocalRain.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this TimeseriesLocalRain.


        :param values: The values of this TimeseriesLocalRain.  # noqa: E501
        :type: list[list[float]]
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    @property
    def interpolate(self):
        """Gets the interpolate of this TimeseriesLocalRain.  # noqa: E501


        :return: The interpolate of this TimeseriesLocalRain.  # noqa: E501
        :rtype: bool
        """
        return self._interpolate

    @interpolate.setter
    def interpolate(self, interpolate):
        """Sets the interpolate of this TimeseriesLocalRain.


        :param interpolate: The interpolate of this TimeseriesLocalRain.  # noqa: E501
        :type: bool
        """

        self._interpolate = interpolate

    @property
    def units(self):
        """Gets the units of this TimeseriesLocalRain.  # noqa: E501

        m/s is only option for now  # noqa: E501

        :return: The units of this TimeseriesLocalRain.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this TimeseriesLocalRain.

        m/s is only option for now  # noqa: E501

        :param units: The units of this TimeseriesLocalRain.  # noqa: E501
        :type: str
        """
        allowed_values = ["m/s", "mm/h", "mm/min"]  # noqa: E501
        if units not in allowed_values:
            raise ValueError(
                "Invalid value for `units` ({0}), must be one of {1}"  # noqa: E501
                .format(units, allowed_values)
            )

        self._units = units

    @property
    def diameter(self):
        """Gets the diameter of this TimeseriesLocalRain.  # noqa: E501


        :return: The diameter of this TimeseriesLocalRain.  # noqa: E501
        :rtype: int
        """
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        """Sets the diameter of this TimeseriesLocalRain.


        :param diameter: The diameter of this TimeseriesLocalRain.  # noqa: E501
        :type: int
        """
        if diameter is None:
            raise ValueError("Invalid value for `diameter`, must not be `None`")  # noqa: E501
        if diameter is not None and diameter > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `diameter`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if diameter is not None and diameter < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `diameter`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._diameter = diameter

    @property
    def point(self):
        """Gets the point of this TimeseriesLocalRain.  # noqa: E501


        :return: The point of this TimeseriesLocalRain.  # noqa: E501
        :rtype: str
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this TimeseriesLocalRain.


        :param point: The point of this TimeseriesLocalRain.  # noqa: E501
        :type: str
        """
        if point is None:
            raise ValueError("Invalid value for `point`, must not be `None`")  # noqa: E501

        self._point = point

    @property
    def uid(self):
        """Gets the uid of this TimeseriesLocalRain.  # noqa: E501


        :return: The uid of this TimeseriesLocalRain.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this TimeseriesLocalRain.


        :param uid: The uid of this TimeseriesLocalRain.  # noqa: E501
        :type: str
        """

        self._uid = uid

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
        if not isinstance(other, TimeseriesLocalRain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
