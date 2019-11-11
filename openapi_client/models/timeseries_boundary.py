# coding: utf-8

"""
    3Di API

    3Di simulation API   Framework release: 0.0.17   3Di core release: 2.0.2  deployed on:  10:18AM (UTC) on October 30, 2019  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class TimeseriesBoundary(object):
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
        'boundary_condition': 'int',
        'url': 'str',
        'simulation': 'str',
        'offset': 'int',
        'values': 'list[list[float]]',
        'interpolate': 'bool',
        'units': 'str'
    }

    attribute_map = {
        'boundary_condition': 'boundary_condition',
        'url': 'url',
        'simulation': 'simulation',
        'offset': 'offset',
        'values': 'values',
        'interpolate': 'interpolate',
        'units': 'units'
    }

    def __init__(self, boundary_condition=None, url=None, simulation=None, offset=None, values=None, interpolate=None, units=None):  # noqa: E501
        """TimeseriesBoundary - a model defined in OpenAPI"""  # noqa: E501

        self._boundary_condition = None
        self._url = None
        self._simulation = None
        self._offset = None
        self._values = None
        self._interpolate = None
        self._units = None
        self.discriminator = None

        self.boundary_condition = boundary_condition
        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.offset = offset
        self.values = values
        if interpolate is not None:
            self.interpolate = interpolate
        self.units = units

    @property
    def boundary_condition(self):
        """Gets the boundary_condition of this TimeseriesBoundary.  # noqa: E501


        :return: The boundary_condition of this TimeseriesBoundary.  # noqa: E501
        :rtype: int
        """
        return self._boundary_condition

    @boundary_condition.setter
    def boundary_condition(self, boundary_condition):
        """Sets the boundary_condition of this TimeseriesBoundary.


        :param boundary_condition: The boundary_condition of this TimeseriesBoundary.  # noqa: E501
        :type: int
        """
        if boundary_condition is None:
            raise ValueError("Invalid value for `boundary_condition`, must not be `None`")  # noqa: E501

        self._boundary_condition = boundary_condition

    @property
    def url(self):
        """Gets the url of this TimeseriesBoundary.  # noqa: E501


        :return: The url of this TimeseriesBoundary.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TimeseriesBoundary.


        :param url: The url of this TimeseriesBoundary.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this TimeseriesBoundary.  # noqa: E501


        :return: The simulation of this TimeseriesBoundary.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this TimeseriesBoundary.


        :param simulation: The simulation of this TimeseriesBoundary.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def offset(self):
        """Gets the offset of this TimeseriesBoundary.  # noqa: E501

        offset of event in simulation in seconds  # noqa: E501

        :return: The offset of this TimeseriesBoundary.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TimeseriesBoundary.

        offset of event in simulation in seconds  # noqa: E501

        :param offset: The offset of this TimeseriesBoundary.  # noqa: E501
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
        """Gets the values of this TimeseriesBoundary.  # noqa: E501


        :return: The values of this TimeseriesBoundary.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this TimeseriesBoundary.


        :param values: The values of this TimeseriesBoundary.  # noqa: E501
        :type: list[list[float]]
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    @property
    def interpolate(self):
        """Gets the interpolate of this TimeseriesBoundary.  # noqa: E501


        :return: The interpolate of this TimeseriesBoundary.  # noqa: E501
        :rtype: bool
        """
        return self._interpolate

    @interpolate.setter
    def interpolate(self, interpolate):
        """Sets the interpolate of this TimeseriesBoundary.


        :param interpolate: The interpolate of this TimeseriesBoundary.  # noqa: E501
        :type: bool
        """

        self._interpolate = interpolate

    @property
    def units(self):
        """Gets the units of this TimeseriesBoundary.  # noqa: E501


        :return: The units of this TimeseriesBoundary.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this TimeseriesBoundary.


        :param units: The units of this TimeseriesBoundary.  # noqa: E501
        :type: str
        """
        if units is None:
            raise ValueError("Invalid value for `units`, must not be `None`")  # noqa: E501
        allowed_values = ["m/s", "m/h", "m/min", "cm/h", "m3/s", "m3/h", "l/s", "l/h", "m MSL", "dimensionless"]  # noqa: E501
        if units not in allowed_values:
            raise ValueError(
                "Invalid value for `units` ({0}), must be one of {1}"  # noqa: E501
                .format(units, allowed_values)
            )

        self._units = units

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
        if not isinstance(other, TimeseriesBoundary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other