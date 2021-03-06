# -*- coding: utf-8 -*-

###############################################################################
#
# ListActivitiesByChannel
# Returns a list of activities for a specified channel.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListActivitiesByChannel(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListActivitiesByChannel Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/YouTube/Activities/ListActivitiesByChannel')


    def new_input_set(self):
        return ListActivitiesByChannelInputSet()

    def _make_result_set(self, result, path):
        return ListActivitiesByChannelResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListActivitiesByChannelChoreographyExecution(session, exec_id, path)

class ListActivitiesByChannelInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListActivitiesByChannel
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The API Key provided by Google for simple API access when you do not need to access user data.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required for OAuth authentication unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ChannelID(self, value):
        """
        Set the value of the ChannelID input for this Choreo. ((required, string) The id of the channel to list activities for.)
        """
        InputSet._set_input(self, 'ChannelID', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Allows you to specify a subset of fields to include in the response using an xpath-like syntax (i.e. items/snippet/title).)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The maximum number of results to return.)
        """
        InputSet._set_input(self, 'MaxResults', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((optional, string) The "nextPageToken" found in the response which is used to page through results.)
        """
        InputSet._set_input(self, 'PageToken', value)
    def set_Part(self, value):
        """
        Set the value of the Part input for this Choreo. ((optional, string) Specifies a comma-separated list of one or more activity resource properties that the API response will include. Part names that you can pass are id, snippet, and contentDetails.)
        """
        InputSet._set_input(self, 'Part', value)
    def set_PublishedAfter(self, value):
        """
        Set the value of the PublishedAfter input for this Choreo. ((optional, date) Returns only results created after the specified time (formatted as a RFC 3339 date-time i.e. 1970-01-01T00:00:00Z).)
        """
        InputSet._set_input(self, 'PublishedAfter', value)
    def set_PublishedBefore(self, value):
        """
        Set the value of the PublishedBefore input for this Choreo. ((optional, date) Returns only results created before the specified time (formatted as a RFC 3339 date-time i.e. 1970-01-01T00:00:00Z).)
        """
        InputSet._set_input(self, 'PublishedBefore', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)

class ListActivitiesByChannelResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListActivitiesByChannel Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from YouTube.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class ListActivitiesByChannelChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListActivitiesByChannelResultSet(response, path)
