# -*- coding: utf-8 -*-

###############################################################################
#
# LikeMedia
# Sets the specified media as being liked by the authenticating user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class LikeMedia(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LikeMedia Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Instagram/LikeMedia')


    def new_input_set(self):
        return LikeMediaInputSet()

    def _make_result_set(self, result, path):
        return LikeMediaResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LikeMediaChoreographyExecution(session, exec_id, path)

class LikeMediaInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LikeMedia
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth 2.0 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_MediaID(self, value):
        """
        Set the value of the MediaID input for this Choreo. ((required, string) The ID of the media to like.)
        """
        InputSet._set_input(self, 'MediaID', value)

class LikeMediaResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LikeMedia Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class LikeMediaChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LikeMediaResultSet(response, path)
