# -*- coding: utf-8 -*-

###############################################################################
#
# Shout
# Creates a message in a user's shoutbox 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Shout(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Shout Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/Shout')


    def new_input_set(self):
        return ShoutInputSet()

    def _make_result_set(self, result, path):
        return ShoutResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShoutChoreographyExecution(session, exec_id, path)

class ShoutInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Shout
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your Last.fm API Key.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) Your Last.fm API Secret.)
        """
        InputSet._set_input(self, 'APISecret', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((required, string) The message to post to the shoutbox.)
        """
        InputSet._set_input(self, 'Message', value)
    def set_SessionKey(self, value):
        """
        Set the value of the SessionKey input for this Choreo. ((required, string) The session key retrieved in the last step of the authorization process.)
        """
        InputSet._set_input(self, 'SessionKey', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) The name of the user to shout on.)
        """
        InputSet._set_input(self, 'User', value)

class ShoutResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Shout Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class ShoutChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShoutResultSet(response, path)
