# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateUser
# Updates an existing user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Users/UpdateUser')


    def new_input_set(self):
        return UpdateUserInputSet()

    def _make_result_set(self, result, path):
        return UpdateUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateUserChoreographyExecution(session, exec_id, path)

class UpdateUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        InputSet._set_input(self, 'Server', value)
    def set_UserData(self, value):
        """
        Set the value of the UserData input for this Choreo. ((required, json) A JSON-formatted string containing the user properties you wish to set.)
        """
        InputSet._set_input(self, 'UserData', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, integer) The ID of the user being updated.)
        """
        InputSet._set_input(self, 'UserID', value)

class UpdateUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class UpdateUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateUserResultSet(response, path)
