# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteUser
# Deletes an existing user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/OneLogin/Users/DeleteUser')


    def new_input_set(self):
        return DeleteUserInputSet()

    def _make_result_set(self, result, path):
        return DeleteUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteUserChoreographyExecution(session, exec_id, path)

class DeleteUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by OneLogin.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, integer) The id the user you want to delete.)
        """
        InputSet._set_input(self, 'ID', value)

class DeleteUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from OneLogin.)
        """
        return self._output.get('Response', None)

class DeleteUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteUserResultSet(response, path)
