# -*- coding: utf-8 -*-

###############################################################################
#
# GetActivityMetrics
# Retrieves activity metrics for the specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetActivityMetrics(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetActivityMetrics Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Withings/Measure/GetActivityMetrics')


    def new_input_set(self):
        return GetActivityMetricsInputSet()

    def _make_result_set(self, result, path):
        return GetActivityMetricsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetActivityMetricsChoreographyExecution(session, exec_id, path)

class GetActivityMetricsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetActivityMetrics
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
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((required, date) The date for the log in YYYY-MM-DD format.)
        """
        InputSet._set_input(self, 'Date', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The ID of the user to retrieve activity metrics for.)
        """
        InputSet._set_input(self, 'UserID', value)

class GetActivityMetricsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetActivityMetrics Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Withings.)
        """
        return self._output.get('Response', None)

class GetActivityMetricsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetActivityMetricsResultSet(response, path)
