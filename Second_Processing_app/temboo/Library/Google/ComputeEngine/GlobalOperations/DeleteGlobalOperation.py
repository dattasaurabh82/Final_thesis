# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteGlobalOperation
# Deletes the specified Global Operation.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteGlobalOperation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteGlobalOperation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/ComputeEngine/GlobalOperations/DeleteGlobalOperation')


    def new_input_set(self):
        return DeleteGlobalOperationInputSet()

    def _make_result_set(self, result, path):
        return DeleteGlobalOperationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteGlobalOperationChoreographyExecution(session, exec_id, path)

class DeleteGlobalOperationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteGlobalOperation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_Operation(self, value):
        """
        Set the value of the Operation input for this Choreo. ((required, string) The name of the operation to delete.)
        """
        InputSet._set_input(self, 'Operation', value)
    def set_Project(self, value):
        """
        Set the value of the Project input for this Choreo. ((required, string) The ID of a Google Compute project.)
        """
        InputSet._set_input(self, 'Project', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)

class DeleteGlobalOperationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteGlobalOperation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Google. A 204 is expected for a successful delete operation.)
        """
        return self._output.get('ResponseStatusCode', None)

class DeleteGlobalOperationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteGlobalOperationResultSet(response, path)
