# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateUserIdentity
# Updates the User Identity.    This API method only allows you to set an identity as verified.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateUserIdentity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateUserIdentity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/UserIdentities/UpdateUserIdentity')


    def new_input_set(self):
        return UpdateUserIdentityInputSet()

    def _make_result_set(self, result, path):
        return UpdateUserIdentityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateUserIdentityChoreographyExecution(session, exec_id, path)

class UpdateUserIdentityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateUserIdentity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_IdentityID(self, value):
        """
        Set the value of the IdentityID input for this Choreo. ((conditional, string) The ID of the Identity to be updated.)
        """
        InputSet._set_input(self, 'IdentityID', value)
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
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((conditional, string) The ID of the user.)
        """
        InputSet._set_input(self, 'UserID', value)
    def set_Verified(self, value):
        """
        Set the value of the Verified input for this Choreo. ((required, string) Specifies whether the identity has been verified (true or false).)
        """
        InputSet._set_input(self, 'Verified', value)

class UpdateUserIdentityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateUserIdentity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class UpdateUserIdentityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateUserIdentityResultSet(response, path)
