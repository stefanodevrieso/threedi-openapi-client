# coding: utf-8

"""
    3DI API

    3DI simulation API  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class UploadRasterSourcesSinks(object):
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
        'multiplier': 'float',
        'simulation': 'str',
        'start_timestep': 'int',
        'end_timestep': 'int',
        'timestamps': 'list[int]',
        'interval': 'int',
        'values_reference': 'str',
        'units': 'str',
        'geotransform': 'list[float]',
        'epsg_code': 'int',
        'upload': 'UploadReadOnly'
    }

    attribute_map = {
        'url': 'url',
        'multiplier': 'multiplier',
        'simulation': 'simulation',
        'start_timestep': 'start_timestep',
        'end_timestep': 'end_timestep',
        'timestamps': 'timestamps',
        'interval': 'interval',
        'values_reference': 'values_reference',
        'units': 'units',
        'geotransform': 'geotransform',
        'epsg_code': 'epsg_code',
        'upload': 'upload'
    }

    def __init__(self, url=None, multiplier=None, simulation=None, start_timestep=None, end_timestep=None, timestamps=None, interval=None, values_reference=None, units=None, geotransform=None, epsg_code=None, upload=None):  # noqa: E501
        """UploadRasterSourcesSinks - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._multiplier = None
        self._simulation = None
        self._start_timestep = None
        self._end_timestep = None
        self._timestamps = None
        self._interval = None
        self._values_reference = None
        self._units = None
        self._geotransform = None
        self._epsg_code = None
        self._upload = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if multiplier is not None:
            self.multiplier = multiplier
        if simulation is not None:
            self.simulation = simulation
        self.start_timestep = start_timestep
        self.end_timestep = end_timestep
        self.timestamps = timestamps
        self.interval = interval
        self.values_reference = values_reference
        self.units = units
        if geotransform is not None:
            self.geotransform = geotransform
        if epsg_code is not None:
            self.epsg_code = epsg_code
        if upload is not None:
            self.upload = upload

    @property
    def url(self):
        """Gets the url of this UploadRasterSourcesSinks.  # noqa: E501


        :return: The url of this UploadRasterSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UploadRasterSourcesSinks.


        :param url: The url of this UploadRasterSourcesSinks.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def multiplier(self):
        """Gets the multiplier of this UploadRasterSourcesSinks.  # noqa: E501


        :return: The multiplier of this UploadRasterSourcesSinks.  # noqa: E501
        :rtype: float
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        """Sets the multiplier of this UploadRasterSourcesSinks.


        :param multiplier: The multiplier of this UploadRasterSourcesSinks.  # noqa: E501
        :type: float
        """

        self._multiplier = multiplier

    @property
    def simulation(self):
        """Gets the simulation of this UploadRasterSourcesSinks.  # noqa: E501


        :return: The simulation of this UploadRasterSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this UploadRasterSourcesSinks.


        :param simulation: The simulation of this UploadRasterSourcesSinks.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def start_timestep(self):
        """Gets the start_timestep of this UploadRasterSourcesSinks.  # noqa: E501

        Start of event in simulation in seconds  # noqa: E501

        :return: The start_timestep of this UploadRasterSourcesSinks.  # noqa: E501
        :rtype: int
        """
        return self._start_timestep

    @start_timestep.setter
    def start_timestep(self, start_timestep):
        """Sets the start_timestep of this UploadRasterSourcesSinks.

        Start of event in simulation in seconds  # noqa: E501

        :param start_timestep: The start_timestep of this UploadRasterSourcesSinks.  # noqa: E501
        :type: int
        """
        if start_timestep is not None and start_timestep > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `start_timestep`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if start_timestep is not None and start_timestep < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `start_timestep`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._start_timestep = start_timestep

    @property
    def end_timestep(self):
        """Gets the end_timestep of this UploadRasterSourcesSinks.  # noqa: E501

        End of event in simulation in seconds  # noqa: E501

        :return: The end_timestep of this UploadRasterSourcesSinks.  # noqa: E501
        :rtype: int
        """
        return self._end_timestep

    @end_timestep.setter
    def end_timestep(self, end_timestep):
        """Sets the end_timestep of this UploadRasterSourcesSinks.

        End of event in simulation in seconds  # noqa: E501

        :param end_timestep: The end_timestep of this UploadRasterSourcesSinks.  # noqa: E501
        :type: int
        """
        if end_timestep is not None and end_timestep > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `end_timestep`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if end_timestep is not None and end_timestep < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `end_timestep`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._end_timestep = end_timestep

    @property
    def timestamps(self):
        """Gets the timestamps of this UploadRasterSourcesSinks.  # noqa: E501

        in simulation in seconds  # noqa: E501

        :return: The timestamps of this UploadRasterSourcesSinks.  # noqa: E501
        :rtype: list[int]
        """
        return self._timestamps

    @timestamps.setter
    def timestamps(self, timestamps):
        """Sets the timestamps of this UploadRasterSourcesSinks.

        in simulation in seconds  # noqa: E501

        :param timestamps: The timestamps of this UploadRasterSourcesSinks.  # noqa: E501
        :type: list[int]
        """

        self._timestamps = timestamps

    @property
    def interval(self):
        """Gets the interval of this UploadRasterSourcesSinks.  # noqa: E501

        interval in seconds  # noqa: E501

        :return: The interval of this UploadRasterSourcesSinks.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this UploadRasterSourcesSinks.

        interval in seconds  # noqa: E501

        :param interval: The interval of this UploadRasterSourcesSinks.  # noqa: E501
        :type: int
        """
        if interval is not None and interval > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `interval`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if interval is not None and interval < 0:  # noqa: E501
            raise ValueError("Invalid value for `interval`, must be a value greater than or equal to `0`")  # noqa: E501

        self._interval = interval

    @property
    def values_reference(self):
        """Gets the values_reference of this UploadRasterSourcesSinks.  # noqa: E501


        :return: The values_reference of this UploadRasterSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._values_reference

    @values_reference.setter
    def values_reference(self, values_reference):
        """Sets the values_reference of this UploadRasterSourcesSinks.


        :param values_reference: The values_reference of this UploadRasterSourcesSinks.  # noqa: E501
        :type: str
        """
        if values_reference is not None and len(values_reference) > 255:
            raise ValueError("Invalid value for `values_reference`, length must be less than or equal to `255`")  # noqa: E501

        self._values_reference = values_reference

    @property
    def units(self):
        """Gets the units of this UploadRasterSourcesSinks.  # noqa: E501


        :return: The units of this UploadRasterSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this UploadRasterSourcesSinks.


        :param units: The units of this UploadRasterSourcesSinks.  # noqa: E501
        :type: str
        """
        if units is None:
            raise ValueError("Invalid value for `units`, must not be `None`")  # noqa: E501
        allowed_values = ["mm", "mm/h", "mm/hr"]  # noqa: E501
        if units not in allowed_values:
            raise ValueError(
                "Invalid value for `units` ({0}), must be one of {1}"  # noqa: E501
                .format(units, allowed_values)
            )

        self._units = units

    @property
    def geotransform(self):
        """Gets the geotransform of this UploadRasterSourcesSinks.  # noqa: E501


        :return: The geotransform of this UploadRasterSourcesSinks.  # noqa: E501
        :rtype: list[float]
        """
        return self._geotransform

    @geotransform.setter
    def geotransform(self, geotransform):
        """Sets the geotransform of this UploadRasterSourcesSinks.


        :param geotransform: The geotransform of this UploadRasterSourcesSinks.  # noqa: E501
        :type: list[float]
        """

        self._geotransform = geotransform

    @property
    def epsg_code(self):
        """Gets the epsg_code of this UploadRasterSourcesSinks.  # noqa: E501


        :return: The epsg_code of this UploadRasterSourcesSinks.  # noqa: E501
        :rtype: int
        """
        return self._epsg_code

    @epsg_code.setter
    def epsg_code(self, epsg_code):
        """Sets the epsg_code of this UploadRasterSourcesSinks.


        :param epsg_code: The epsg_code of this UploadRasterSourcesSinks.  # noqa: E501
        :type: int
        """
        if epsg_code is not None and epsg_code > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `epsg_code`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if epsg_code is not None and epsg_code < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `epsg_code`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._epsg_code = epsg_code

    @property
    def upload(self):
        """Gets the upload of this UploadRasterSourcesSinks.  # noqa: E501


        :return: The upload of this UploadRasterSourcesSinks.  # noqa: E501
        :rtype: UploadReadOnly
        """
        return self._upload

    @upload.setter
    def upload(self, upload):
        """Sets the upload of this UploadRasterSourcesSinks.


        :param upload: The upload of this UploadRasterSourcesSinks.  # noqa: E501
        :type: UploadReadOnly
        """

        self._upload = upload

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
        if not isinstance(other, UploadRasterSourcesSinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
