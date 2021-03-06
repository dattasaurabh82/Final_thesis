# -*- coding: utf-8 -*-

###############################################################################
#
# GetBodyMetrics
# Retrieves body metrics for the specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetBodyMetrics(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBodyMetrics Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Withings/Measure/GetBodyMetrics')


    def new_input_set(self):
        return GetBodyMetricsInputSet()

    def _make_result_set(self, result, path):
        return GetBodyMetricsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBodyMetricsChoreographyExecution(session, exec_id, path)

class GetBodyMetricsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBodyMetrics
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((optional, integer) Set to 2 to retrieve objectives or to 1 to retrieve actual measurements.)
        """
        InputSet._set_input(self, 'Category', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Withings.)
        """
        InputSet._set_input(self, 'ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Withings.)
        """
        InputSet._set_input(self, 'ConsumerSecret', value)
    def set_DeviceType(self, value):
        """
        Set the value of the DeviceType input for this Choreo. ((optional, integer) Retrieves data for a particular device type. Specifying 1 will retrieve all body scale related measures and 0 will retrieve all user personal data entered at user creation time.)
        """
        InputSet._set_input(self, 'DeviceType', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, date) Retrieves results dated before the specified EPOCH formatted date.)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_LastUpdated(self, value):
        """
        Set the value of the LastUpdated input for this Choreo. ((optional, date) Retrieves results added or modified since the specified EPOCH formatted date.)
        """
        InputSet._set_input(self, 'LastUpdated', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Limits the number of measure groups returned in the result.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_MeasurementType(self, value):
        """
        Set the value of the MeasurementType input for this Choreo. ((optional, integer) Filters by the measurement type. Set to 1 to filter by weight or 4 to filter by height.)
        """
        InputSet._set_input(self, 'MeasurementType', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Used in combination with the Limit parameter to page through results.)
        """
        InputSet._set_input(self, 'Offset', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, date) Retrieves results dated after the specified EPOCH formatted date.)
        """
        InputSet._set_input(self, 'StartDate', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The ID of the user to retrieve body metrics for.)
        """
        InputSet._set_input(self, 'UserID', value)

class GetBodyMetricsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBodyMetrics Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Withings.)
        """
        return self._output.get('Response', None)

class GetBodyMetricsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBodyMetricsResultSet(response, path)
