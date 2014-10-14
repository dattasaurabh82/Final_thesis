# -*- coding: utf-8 -*-

###############################################################################
#
# RestorePost
# Restore a deleted post.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RestorePost(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RestorePost Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Posts/RestorePost')


    def new_input_set(self):
        return RestorePostInputSet()

    def _make_result_set(self, result, path):
        return RestorePostResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RestorePostChoreographyExecution(session, exec_id, path)

class RestorePostInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RestorePost
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth 2.0 access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_PostID(self, value):
        """
        Set the value of the PostID input for this Choreo. ((required, integer) The post ID which is to be restored (undeleted).)
        """
        InputSet._set_input(self, 'PostID', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        InputSet._set_input(self, 'PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and jsonp.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)


class RestorePostResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RestorePost Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Disqus.)
        """
        return self._output.get('Response', None)

class RestorePostChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RestorePostResultSet(response, path)
