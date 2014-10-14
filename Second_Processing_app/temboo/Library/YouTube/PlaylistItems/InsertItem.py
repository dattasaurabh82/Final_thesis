# -*- coding: utf-8 -*-

###############################################################################
#
# InsertItem
# Creates a new item within a playlist.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class InsertItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the InsertItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/YouTube/PlaylistItems/InsertItem')


    def new_input_set(self):
        return InsertItemInputSet()

    def _make_result_set(self, result, path):
        return InsertItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return InsertItemChoreographyExecution(session, exec_id, path)

class InsertItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the InsertItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required for OAuth authentication unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
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
    def set_Part(self, value):
        """
        Set the value of the Part input for this Choreo. ((optional, string) A comma-separated list of fields that are being set and that will be returned in the response. Part names that can be passed are: snippet and contentDetails.)
        """
        InputSet._set_input(self, 'Part', value)
    def set_PlaylistID(self, value):
        """
        Set the value of the PlaylistID input for this Choreo. ((required, string) The id of the playlist to add an item to.)
        """
        InputSet._set_input(self, 'PlaylistID', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)
    def set_VideoID(self, value):
        """
        Set the value of the VideoID input for this Choreo. ((required, string) The id of the video to add to the playlist.)
        """
        InputSet._set_input(self, 'VideoID', value)

class InsertItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the InsertItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)

class InsertItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return InsertItemResultSet(response, path)
