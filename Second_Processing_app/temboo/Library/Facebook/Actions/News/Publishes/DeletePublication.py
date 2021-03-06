# -*- coding: utf-8 -*-

###############################################################################
#
# DeletePublication
# Deletes a given news publishing action.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeletePublication(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeletePublication Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Actions/News/Publishes/DeletePublication')


    def new_input_set(self):
        return DeletePublicationInputSet()

    def _make_result_set(self, result, path):
        return DeletePublicationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeletePublicationChoreographyExecution(session, exec_id, path)

class DeletePublicationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeletePublication
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ActionID(self, value):
        """
        Set the value of the ActionID input for this Choreo. ((required, string) The id of an action to delete.)
        """
        InputSet._set_input(self, 'ActionID', value)

class DeletePublicationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeletePublication Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((boolean) The response from Facebook. Returns "true" on success.)
        """
        return self._output.get('Response', None)

class DeletePublicationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeletePublicationResultSet(response, path)
