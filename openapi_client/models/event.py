# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 0.0.33   3Di core release: 2.0.4  deployed on:  03:28PM (UTC) on February 03, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Event(object):
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
        'lizardrasterrain': 'list[LizardRasterRain]',
        'lizardtimeseriesrain': 'list[LizardTimeseriesRain]',
        'timeseriesrain': 'list[TimeseriesRainOverview]',
        'breach': 'list[Breach]',
        'lizardrastersourcessinks': 'list[LizardRasterSourcesSinks]',
        'lizardtimeseriessourcessinks': 'list[LizardTimeseriesSourcesSinks]',
        'filerastersourcessinks': 'list[FileRasterSourcesSinks]',
        'filetimeseriessourcessinks': 'list[FileTimeseriesSourcesSinks]',
        'timeseriessourcessinks': 'list[TimeseriesSourcesSinksOverview]',
        'initial_twodwaterlevel': 'TwoDWaterLevel',
        'initial_onedwaterlevelpredefined': 'OneDWaterLevelPredefined',
        'initial_groundwaterlevel': 'GroundWaterLevel',
        'initial_groundwaterraster': 'GroundWaterRaster',
        'initial_onedwaterlevel': 'OneDWaterLevel',
        'initial_twodwaterraster': 'TwoDWaterRaster',
        'filerasterrain': 'list[FileRasterRain]',
        'filetimeseriesrain': 'list[FileTimeseriesRain]',
        'initial_savedstate': 'InitialSavedStateOverview',
        'savedstates': 'list[SavedStateOverview]',
        'laterals': 'list[Lateral]',
        'timedstructurecontrol': 'list[TimedStructureControl]',
        'rasteredits': 'list[RasterEdit]',
        'localrain': 'list[LocalRain]',
        'wind': 'list[Wind]'
    }

    attribute_map = {
        'lizardrasterrain': 'lizardrasterrain',
        'lizardtimeseriesrain': 'lizardtimeseriesrain',
        'timeseriesrain': 'timeseriesrain',
        'breach': 'breach',
        'lizardrastersourcessinks': 'lizardrastersourcessinks',
        'lizardtimeseriessourcessinks': 'lizardtimeseriessourcessinks',
        'filerastersourcessinks': 'filerastersourcessinks',
        'filetimeseriessourcessinks': 'filetimeseriessourcessinks',
        'timeseriessourcessinks': 'timeseriessourcessinks',
        'initial_twodwaterlevel': 'initial_twodwaterlevel',
        'initial_onedwaterlevelpredefined': 'initial_onedwaterlevelpredefined',
        'initial_groundwaterlevel': 'initial_groundwaterlevel',
        'initial_groundwaterraster': 'initial_groundwaterraster',
        'initial_onedwaterlevel': 'initial_onedwaterlevel',
        'initial_twodwaterraster': 'initial_twodwaterraster',
        'filerasterrain': 'filerasterrain',
        'filetimeseriesrain': 'filetimeseriesrain',
        'initial_savedstate': 'initial_savedstate',
        'savedstates': 'savedstates',
        'laterals': 'laterals',
        'timedstructurecontrol': 'timedstructurecontrol',
        'rasteredits': 'rasteredits',
        'localrain': 'localrain',
        'wind': 'wind'
    }

    def __init__(self, lizardrasterrain=None, lizardtimeseriesrain=None, timeseriesrain=None, breach=None, lizardrastersourcessinks=None, lizardtimeseriessourcessinks=None, filerastersourcessinks=None, filetimeseriessourcessinks=None, timeseriessourcessinks=None, initial_twodwaterlevel=None, initial_onedwaterlevelpredefined=None, initial_groundwaterlevel=None, initial_groundwaterraster=None, initial_onedwaterlevel=None, initial_twodwaterraster=None, filerasterrain=None, filetimeseriesrain=None, initial_savedstate=None, savedstates=None, laterals=None, timedstructurecontrol=None, rasteredits=None, localrain=None, wind=None, local_vars_configuration=None):  # noqa: E501
        """Event - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._lizardrasterrain = None
        self._lizardtimeseriesrain = None
        self._timeseriesrain = None
        self._breach = None
        self._lizardrastersourcessinks = None
        self._lizardtimeseriessourcessinks = None
        self._filerastersourcessinks = None
        self._filetimeseriessourcessinks = None
        self._timeseriessourcessinks = None
        self._initial_twodwaterlevel = None
        self._initial_onedwaterlevelpredefined = None
        self._initial_groundwaterlevel = None
        self._initial_groundwaterraster = None
        self._initial_onedwaterlevel = None
        self._initial_twodwaterraster = None
        self._filerasterrain = None
        self._filetimeseriesrain = None
        self._initial_savedstate = None
        self._savedstates = None
        self._laterals = None
        self._timedstructurecontrol = None
        self._rasteredits = None
        self._localrain = None
        self._wind = None
        self.discriminator = None

        if lizardrasterrain is not None:
            self.lizardrasterrain = lizardrasterrain
        if lizardtimeseriesrain is not None:
            self.lizardtimeseriesrain = lizardtimeseriesrain
        if timeseriesrain is not None:
            self.timeseriesrain = timeseriesrain
        if breach is not None:
            self.breach = breach
        if lizardrastersourcessinks is not None:
            self.lizardrastersourcessinks = lizardrastersourcessinks
        if lizardtimeseriessourcessinks is not None:
            self.lizardtimeseriessourcessinks = lizardtimeseriessourcessinks
        if filerastersourcessinks is not None:
            self.filerastersourcessinks = filerastersourcessinks
        if filetimeseriessourcessinks is not None:
            self.filetimeseriessourcessinks = filetimeseriessourcessinks
        if timeseriessourcessinks is not None:
            self.timeseriessourcessinks = timeseriessourcessinks
        if initial_twodwaterlevel is not None:
            self.initial_twodwaterlevel = initial_twodwaterlevel
        if initial_onedwaterlevelpredefined is not None:
            self.initial_onedwaterlevelpredefined = initial_onedwaterlevelpredefined
        if initial_groundwaterlevel is not None:
            self.initial_groundwaterlevel = initial_groundwaterlevel
        if initial_groundwaterraster is not None:
            self.initial_groundwaterraster = initial_groundwaterraster
        if initial_onedwaterlevel is not None:
            self.initial_onedwaterlevel = initial_onedwaterlevel
        if initial_twodwaterraster is not None:
            self.initial_twodwaterraster = initial_twodwaterraster
        if filerasterrain is not None:
            self.filerasterrain = filerasterrain
        if filetimeseriesrain is not None:
            self.filetimeseriesrain = filetimeseriesrain
        if initial_savedstate is not None:
            self.initial_savedstate = initial_savedstate
        if savedstates is not None:
            self.savedstates = savedstates
        if laterals is not None:
            self.laterals = laterals
        if timedstructurecontrol is not None:
            self.timedstructurecontrol = timedstructurecontrol
        if rasteredits is not None:
            self.rasteredits = rasteredits
        if localrain is not None:
            self.localrain = localrain
        if wind is not None:
            self.wind = wind

    @property
    def lizardrasterrain(self):
        """Gets the lizardrasterrain of this Event.  # noqa: E501


        :return: The lizardrasterrain of this Event.  # noqa: E501
        :rtype: list[LizardRasterRain]
        """
        return self._lizardrasterrain

    @lizardrasterrain.setter
    def lizardrasterrain(self, lizardrasterrain):
        """Sets the lizardrasterrain of this Event.


        :param lizardrasterrain: The lizardrasterrain of this Event.  # noqa: E501
        :type: list[LizardRasterRain]
        """

        self._lizardrasterrain = lizardrasterrain

    @property
    def lizardtimeseriesrain(self):
        """Gets the lizardtimeseriesrain of this Event.  # noqa: E501


        :return: The lizardtimeseriesrain of this Event.  # noqa: E501
        :rtype: list[LizardTimeseriesRain]
        """
        return self._lizardtimeseriesrain

    @lizardtimeseriesrain.setter
    def lizardtimeseriesrain(self, lizardtimeseriesrain):
        """Sets the lizardtimeseriesrain of this Event.


        :param lizardtimeseriesrain: The lizardtimeseriesrain of this Event.  # noqa: E501
        :type: list[LizardTimeseriesRain]
        """

        self._lizardtimeseriesrain = lizardtimeseriesrain

    @property
    def timeseriesrain(self):
        """Gets the timeseriesrain of this Event.  # noqa: E501


        :return: The timeseriesrain of this Event.  # noqa: E501
        :rtype: list[TimeseriesRainOverview]
        """
        return self._timeseriesrain

    @timeseriesrain.setter
    def timeseriesrain(self, timeseriesrain):
        """Sets the timeseriesrain of this Event.


        :param timeseriesrain: The timeseriesrain of this Event.  # noqa: E501
        :type: list[TimeseriesRainOverview]
        """

        self._timeseriesrain = timeseriesrain

    @property
    def breach(self):
        """Gets the breach of this Event.  # noqa: E501


        :return: The breach of this Event.  # noqa: E501
        :rtype: list[Breach]
        """
        return self._breach

    @breach.setter
    def breach(self, breach):
        """Sets the breach of this Event.


        :param breach: The breach of this Event.  # noqa: E501
        :type: list[Breach]
        """

        self._breach = breach

    @property
    def lizardrastersourcessinks(self):
        """Gets the lizardrastersourcessinks of this Event.  # noqa: E501


        :return: The lizardrastersourcessinks of this Event.  # noqa: E501
        :rtype: list[LizardRasterSourcesSinks]
        """
        return self._lizardrastersourcessinks

    @lizardrastersourcessinks.setter
    def lizardrastersourcessinks(self, lizardrastersourcessinks):
        """Sets the lizardrastersourcessinks of this Event.


        :param lizardrastersourcessinks: The lizardrastersourcessinks of this Event.  # noqa: E501
        :type: list[LizardRasterSourcesSinks]
        """

        self._lizardrastersourcessinks = lizardrastersourcessinks

    @property
    def lizardtimeseriessourcessinks(self):
        """Gets the lizardtimeseriessourcessinks of this Event.  # noqa: E501


        :return: The lizardtimeseriessourcessinks of this Event.  # noqa: E501
        :rtype: list[LizardTimeseriesSourcesSinks]
        """
        return self._lizardtimeseriessourcessinks

    @lizardtimeseriessourcessinks.setter
    def lizardtimeseriessourcessinks(self, lizardtimeseriessourcessinks):
        """Sets the lizardtimeseriessourcessinks of this Event.


        :param lizardtimeseriessourcessinks: The lizardtimeseriessourcessinks of this Event.  # noqa: E501
        :type: list[LizardTimeseriesSourcesSinks]
        """

        self._lizardtimeseriessourcessinks = lizardtimeseriessourcessinks

    @property
    def filerastersourcessinks(self):
        """Gets the filerastersourcessinks of this Event.  # noqa: E501


        :return: The filerastersourcessinks of this Event.  # noqa: E501
        :rtype: list[FileRasterSourcesSinks]
        """
        return self._filerastersourcessinks

    @filerastersourcessinks.setter
    def filerastersourcessinks(self, filerastersourcessinks):
        """Sets the filerastersourcessinks of this Event.


        :param filerastersourcessinks: The filerastersourcessinks of this Event.  # noqa: E501
        :type: list[FileRasterSourcesSinks]
        """

        self._filerastersourcessinks = filerastersourcessinks

    @property
    def filetimeseriessourcessinks(self):
        """Gets the filetimeseriessourcessinks of this Event.  # noqa: E501


        :return: The filetimeseriessourcessinks of this Event.  # noqa: E501
        :rtype: list[FileTimeseriesSourcesSinks]
        """
        return self._filetimeseriessourcessinks

    @filetimeseriessourcessinks.setter
    def filetimeseriessourcessinks(self, filetimeseriessourcessinks):
        """Sets the filetimeseriessourcessinks of this Event.


        :param filetimeseriessourcessinks: The filetimeseriessourcessinks of this Event.  # noqa: E501
        :type: list[FileTimeseriesSourcesSinks]
        """

        self._filetimeseriessourcessinks = filetimeseriessourcessinks

    @property
    def timeseriessourcessinks(self):
        """Gets the timeseriessourcessinks of this Event.  # noqa: E501


        :return: The timeseriessourcessinks of this Event.  # noqa: E501
        :rtype: list[TimeseriesSourcesSinksOverview]
        """
        return self._timeseriessourcessinks

    @timeseriessourcessinks.setter
    def timeseriessourcessinks(self, timeseriessourcessinks):
        """Sets the timeseriessourcessinks of this Event.


        :param timeseriessourcessinks: The timeseriessourcessinks of this Event.  # noqa: E501
        :type: list[TimeseriesSourcesSinksOverview]
        """

        self._timeseriessourcessinks = timeseriessourcessinks

    @property
    def initial_twodwaterlevel(self):
        """Gets the initial_twodwaterlevel of this Event.  # noqa: E501


        :return: The initial_twodwaterlevel of this Event.  # noqa: E501
        :rtype: TwoDWaterLevel
        """
        return self._initial_twodwaterlevel

    @initial_twodwaterlevel.setter
    def initial_twodwaterlevel(self, initial_twodwaterlevel):
        """Sets the initial_twodwaterlevel of this Event.


        :param initial_twodwaterlevel: The initial_twodwaterlevel of this Event.  # noqa: E501
        :type: TwoDWaterLevel
        """

        self._initial_twodwaterlevel = initial_twodwaterlevel

    @property
    def initial_onedwaterlevelpredefined(self):
        """Gets the initial_onedwaterlevelpredefined of this Event.  # noqa: E501


        :return: The initial_onedwaterlevelpredefined of this Event.  # noqa: E501
        :rtype: OneDWaterLevelPredefined
        """
        return self._initial_onedwaterlevelpredefined

    @initial_onedwaterlevelpredefined.setter
    def initial_onedwaterlevelpredefined(self, initial_onedwaterlevelpredefined):
        """Sets the initial_onedwaterlevelpredefined of this Event.


        :param initial_onedwaterlevelpredefined: The initial_onedwaterlevelpredefined of this Event.  # noqa: E501
        :type: OneDWaterLevelPredefined
        """

        self._initial_onedwaterlevelpredefined = initial_onedwaterlevelpredefined

    @property
    def initial_groundwaterlevel(self):
        """Gets the initial_groundwaterlevel of this Event.  # noqa: E501


        :return: The initial_groundwaterlevel of this Event.  # noqa: E501
        :rtype: GroundWaterLevel
        """
        return self._initial_groundwaterlevel

    @initial_groundwaterlevel.setter
    def initial_groundwaterlevel(self, initial_groundwaterlevel):
        """Sets the initial_groundwaterlevel of this Event.


        :param initial_groundwaterlevel: The initial_groundwaterlevel of this Event.  # noqa: E501
        :type: GroundWaterLevel
        """

        self._initial_groundwaterlevel = initial_groundwaterlevel

    @property
    def initial_groundwaterraster(self):
        """Gets the initial_groundwaterraster of this Event.  # noqa: E501


        :return: The initial_groundwaterraster of this Event.  # noqa: E501
        :rtype: GroundWaterRaster
        """
        return self._initial_groundwaterraster

    @initial_groundwaterraster.setter
    def initial_groundwaterraster(self, initial_groundwaterraster):
        """Sets the initial_groundwaterraster of this Event.


        :param initial_groundwaterraster: The initial_groundwaterraster of this Event.  # noqa: E501
        :type: GroundWaterRaster
        """

        self._initial_groundwaterraster = initial_groundwaterraster

    @property
    def initial_onedwaterlevel(self):
        """Gets the initial_onedwaterlevel of this Event.  # noqa: E501


        :return: The initial_onedwaterlevel of this Event.  # noqa: E501
        :rtype: OneDWaterLevel
        """
        return self._initial_onedwaterlevel

    @initial_onedwaterlevel.setter
    def initial_onedwaterlevel(self, initial_onedwaterlevel):
        """Sets the initial_onedwaterlevel of this Event.


        :param initial_onedwaterlevel: The initial_onedwaterlevel of this Event.  # noqa: E501
        :type: OneDWaterLevel
        """

        self._initial_onedwaterlevel = initial_onedwaterlevel

    @property
    def initial_twodwaterraster(self):
        """Gets the initial_twodwaterraster of this Event.  # noqa: E501


        :return: The initial_twodwaterraster of this Event.  # noqa: E501
        :rtype: TwoDWaterRaster
        """
        return self._initial_twodwaterraster

    @initial_twodwaterraster.setter
    def initial_twodwaterraster(self, initial_twodwaterraster):
        """Sets the initial_twodwaterraster of this Event.


        :param initial_twodwaterraster: The initial_twodwaterraster of this Event.  # noqa: E501
        :type: TwoDWaterRaster
        """

        self._initial_twodwaterraster = initial_twodwaterraster

    @property
    def filerasterrain(self):
        """Gets the filerasterrain of this Event.  # noqa: E501


        :return: The filerasterrain of this Event.  # noqa: E501
        :rtype: list[FileRasterRain]
        """
        return self._filerasterrain

    @filerasterrain.setter
    def filerasterrain(self, filerasterrain):
        """Sets the filerasterrain of this Event.


        :param filerasterrain: The filerasterrain of this Event.  # noqa: E501
        :type: list[FileRasterRain]
        """

        self._filerasterrain = filerasterrain

    @property
    def filetimeseriesrain(self):
        """Gets the filetimeseriesrain of this Event.  # noqa: E501


        :return: The filetimeseriesrain of this Event.  # noqa: E501
        :rtype: list[FileTimeseriesRain]
        """
        return self._filetimeseriesrain

    @filetimeseriesrain.setter
    def filetimeseriesrain(self, filetimeseriesrain):
        """Sets the filetimeseriesrain of this Event.


        :param filetimeseriesrain: The filetimeseriesrain of this Event.  # noqa: E501
        :type: list[FileTimeseriesRain]
        """

        self._filetimeseriesrain = filetimeseriesrain

    @property
    def initial_savedstate(self):
        """Gets the initial_savedstate of this Event.  # noqa: E501


        :return: The initial_savedstate of this Event.  # noqa: E501
        :rtype: InitialSavedStateOverview
        """
        return self._initial_savedstate

    @initial_savedstate.setter
    def initial_savedstate(self, initial_savedstate):
        """Sets the initial_savedstate of this Event.


        :param initial_savedstate: The initial_savedstate of this Event.  # noqa: E501
        :type: InitialSavedStateOverview
        """

        self._initial_savedstate = initial_savedstate

    @property
    def savedstates(self):
        """Gets the savedstates of this Event.  # noqa: E501


        :return: The savedstates of this Event.  # noqa: E501
        :rtype: list[SavedStateOverview]
        """
        return self._savedstates

    @savedstates.setter
    def savedstates(self, savedstates):
        """Sets the savedstates of this Event.


        :param savedstates: The savedstates of this Event.  # noqa: E501
        :type: list[SavedStateOverview]
        """

        self._savedstates = savedstates

    @property
    def laterals(self):
        """Gets the laterals of this Event.  # noqa: E501


        :return: The laterals of this Event.  # noqa: E501
        :rtype: list[Lateral]
        """
        return self._laterals

    @laterals.setter
    def laterals(self, laterals):
        """Sets the laterals of this Event.


        :param laterals: The laterals of this Event.  # noqa: E501
        :type: list[Lateral]
        """

        self._laterals = laterals

    @property
    def timedstructurecontrol(self):
        """Gets the timedstructurecontrol of this Event.  # noqa: E501


        :return: The timedstructurecontrol of this Event.  # noqa: E501
        :rtype: list[TimedStructureControl]
        """
        return self._timedstructurecontrol

    @timedstructurecontrol.setter
    def timedstructurecontrol(self, timedstructurecontrol):
        """Sets the timedstructurecontrol of this Event.


        :param timedstructurecontrol: The timedstructurecontrol of this Event.  # noqa: E501
        :type: list[TimedStructureControl]
        """

        self._timedstructurecontrol = timedstructurecontrol

    @property
    def rasteredits(self):
        """Gets the rasteredits of this Event.  # noqa: E501


        :return: The rasteredits of this Event.  # noqa: E501
        :rtype: list[RasterEdit]
        """
        return self._rasteredits

    @rasteredits.setter
    def rasteredits(self, rasteredits):
        """Sets the rasteredits of this Event.


        :param rasteredits: The rasteredits of this Event.  # noqa: E501
        :type: list[RasterEdit]
        """

        self._rasteredits = rasteredits

    @property
    def localrain(self):
        """Gets the localrain of this Event.  # noqa: E501


        :return: The localrain of this Event.  # noqa: E501
        :rtype: list[LocalRain]
        """
        return self._localrain

    @localrain.setter
    def localrain(self, localrain):
        """Sets the localrain of this Event.


        :param localrain: The localrain of this Event.  # noqa: E501
        :type: list[LocalRain]
        """

        self._localrain = localrain

    @property
    def wind(self):
        """Gets the wind of this Event.  # noqa: E501


        :return: The wind of this Event.  # noqa: E501
        :rtype: list[Wind]
        """
        return self._wind

    @wind.setter
    def wind(self, wind):
        """Sets the wind of this Event.


        :param wind: The wind of this Event.  # noqa: E501
        :type: list[Wind]
        """

        self._wind = wind

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
        if not isinstance(other, Event):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Event):
            return True

        return self.to_dict() != other.to_dict()
