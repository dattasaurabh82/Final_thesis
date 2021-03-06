# -*- coding: utf-8 -*-

###############################################################################
#
# SearchCalendarsByName
# Retrieves information about a calendar including the id with a given calendar name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchCalendarsByName(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchCalendarsByName Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Calendar/SearchCalendarsByName')


    def new_input_set(self):
        return SearchCalendarsByNameInputSet()

    def _make_result_set(self, result, path):
        return SearchCalendarsByNameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchCalendarsByNameChoreographyExecution(session, exec_id, path)

class SearchCalendarsByNameInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchCalendarsByName
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_CalendarName(self, value):
        """
        Set the value of the CalendarName input for this Choreo. ((required, string) The name of the calendar that you want to retrieve information for. Note that if there are multiple calendars with the same name, only the first one will be returned.)
        """
        InputSet._set_input(self, 'CalendarName', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) The maximum number of calendars to search by name. The default is 15.)
        """
        InputSet._set_input(self, 'Count', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)

class SearchCalendarsByNameResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchCalendarsByName Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_CalendarSummary(self):
        """
        Retrieve the value for the "CalendarSummary" output from this Choreo execution. ((string) The summary or calendar name parsed from the Google response.)
        """
        return self._output.get('CalendarSummary', None)
    def get_CalendarDescription(self):
        """
        Retrieve the value for the "CalendarDescription" output from this Choreo execution. ((string) The calendar description parsed from the Google response.)
        """
        return self._output.get('CalendarDescription', None)
    def get_CalendarTimezone(self):
        """
        Retrieve the value for the "CalendarTimezone" output from this Choreo execution. ((string) The calendar timezone parsed from the Google response.)
        """
        return self._output.get('CalendarTimezone', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)
    def get_CalendarId(self):
        """
        Retrieve the value for the "CalendarId" output from this Choreo execution. ((string) The calendar id parsed from the Google response.)
        """
        return self._output.get('CalendarId', None)

class SearchCalendarsByNameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchCalendarsByNameResultSet(response, path)
