# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteReading
# Deletes a given book reading action.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteReading(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteReading Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Actions/Books/Reads/DeleteReading')


    def new_input_set(self):
        return DeleteReadingInputSet()

    def _make_result_set(self, result, path):
        return DeleteReadingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteReadingChoreographyExecution(session, exec_id, path)

class DeleteReadingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteReading
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

class DeleteReadingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteReading Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((boolean) The response from Facebook. Returns "true" on success.)
        """
        return self._output.get('Response', None)

class DeleteReadingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteReadingResultSet(response, path)
