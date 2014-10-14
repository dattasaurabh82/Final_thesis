# -*- coding: utf-8 -*-

###############################################################################
#
# GetTopAlbums
# Retrieves the top albums listened to by a user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetTopAlbums(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTopAlbums Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetTopAlbums')


    def new_input_set(self):
        return GetTopAlbumsInputSet()

    def _make_result_set(self, result, path):
        return GetTopAlbumsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTopAlbumsChoreographyExecution(session, exec_id, path)

class GetTopAlbumsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTopAlbums
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Your Last.fm API Key.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to fetch per page. Defaults to 50.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page number to fetch. Defaults to 1.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_Period(self, value):
        """
        Set the value of the Period input for this Choreo. ((optional, string) The time period over which to retrieve top albums for. Valid values are: overall, 7day, 3month, 6month, 12month. Defaults to 'overall'.)
        """
        InputSet._set_input(self, 'Period', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((string) The Last.fm username to fetch top albums for.)
        """
        InputSet._set_input(self, 'User', value)

class GetTopAlbumsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTopAlbums Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetTopAlbumsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTopAlbumsResultSet(response, path)
