# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateWatch
# Updates an existing watch action.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateWatch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateWatch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Actions/Video/Watches/UpdateWatch')


    def new_input_set(self):
        return UpdateWatchInputSet()

    def _make_result_set(self, result, path):
        return UpdateWatchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateWatchChoreographyExecution(session, exec_id, path)

class UpdateWatchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateWatch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ActionID(self, value):
        """
        Set the value of the ActionID input for this Choreo. ((required, string) The id of the action to update.)
        """
        InputSet._set_input(self, 'ActionID', value)
    def set_EndTime(self, value):
        """
        Set the value of the EndTime input for this Choreo. ((optional, date) The time that the user ended the action (e.g. 2013-06-24T18:53:35+0000).)
        """
        InputSet._set_input(self, 'EndTime', value)
    def set_Episode(self, value):
        """
        Set the value of the Episode input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing an episode of a show.)
        """
        InputSet._set_input(self, 'Episode', value)
    def set_ExpiresIn(self, value):
        """
        Set the value of the ExpiresIn input for this Choreo. ((optional, integer) The amount of time (in milliseconds) from the publish_time that the action will expire.)
        """
        InputSet._set_input(self, 'ExpiresIn', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) A message attached to this action. Setting this parameter requires enabling of message capabilities.)
        """
        InputSet._set_input(self, 'Message', value)
    def set_Movie(self, value):
        """
        Set the value of the Movie input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing a movie.)
        """
        InputSet._set_input(self, 'Movie', value)
    def set_Place(self, value):
        """
        Set the value of the Place input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing the location associated with this action.)
        """
        InputSet._set_input(self, 'Place', value)
    def set_TVShow(self, value):
        """
        Set the value of the TVShow input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing a TV show.)
        """
        InputSet._set_input(self, 'TVShow', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) A comma separated list of other profile IDs that also performed this action.)
        """
        InputSet._set_input(self, 'Tags', value)
    def set_Video(self, value):
        """
        Set the value of the Video input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing any general video content.)
        """
        InputSet._set_input(self, 'Video', value)

class UpdateWatchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateWatch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook.)
        """
        return self._output.get('Response', None)

class UpdateWatchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateWatchResultSet(response, path)
