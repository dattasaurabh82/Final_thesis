# -*- coding: utf-8 -*-

###############################################################################
#
# PasswordChange
# Updates a user's password.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PasswordChange(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PasswordChange Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/CloudMine/UserAccountManagement/PasswordChange')


    def new_input_set(self):
        return PasswordChangeInputSet()

    def _make_result_set(self, result, path):
        return PasswordChangeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PasswordChangeChoreographyExecution(session, exec_id, path)

class PasswordChangeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PasswordChange
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by CloudMine after registering your app.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ApplicationIdentifier(self, value):
        """
        Set the value of the ApplicationIdentifier input for this Choreo. ((required, string) The application identifier provided by CloudMine after registering your app.)
        """
        InputSet._set_input(self, 'ApplicationIdentifier', value)
    def set_NewPassword(self, value):
        """
        Set the value of the NewPassword input for this Choreo. ((required, string) The user's new password.)
        """
        InputSet._set_input(self, 'NewPassword', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, string) The password for the user that needs to authenticate.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The username for the user that needs to authenticate.)
        """
        InputSet._set_input(self, 'Username', value)

class PasswordChangeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PasswordChange Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from CloudMine.)
        """
        return self._output.get('Response', None)

class PasswordChangeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PasswordChangeResultSet(response, path)
