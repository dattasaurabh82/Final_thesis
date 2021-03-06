# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateLike
# Creates an action that represents a user liking an object.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateLike(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateLike Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Actions/General/Likes/UpdateLike')


    def new_input_set(self):
        return UpdateLikeInputSet()

    def _make_result_set(self, result, path):
        return UpdateLikeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateLikeChoreographyExecution(session, exec_id, path)

class UpdateLikeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateLike
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
    def set_ExpiresIn(self, value):
        """
        Set the value of the ExpiresIn input for this Choreo. ((optional, integer) The amount of time (in milliseconds) from the publish_time that the action will expire.)
        """
        InputSet._set_input(self, 'ExpiresIn', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) A message attached to this fitness action. Setting this parameter requires enabling of message capabilities.)
        """
        InputSet._set_input(self, 'Message', value)
    def set_Object(self, value):
        """
        Set the value of the Object input for this Choreo. ((optional, string) The URL or ID for an Open Graph object  that was liked.)
        """
        InputSet._set_input(self, 'Object', value)
    def set_Place(self, value):
        """
        Set the value of the Place input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing the location associated with this action.)
        """
        InputSet._set_input(self, 'Place', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) A comma separated list of other profile IDs that also performed this action.)
        """
        InputSet._set_input(self, 'Tags', value)

class UpdateLikeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateLike Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class UpdateLikeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateLikeResultSet(response, path)
