# -*- coding: utf-8 -*-

###############################################################################
#
# AddUserIdentity
# Allows an agent to add new identities for a given user ID. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AddUserIdentity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddUserIdentity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/UserIdentities/AddUserIdentity')


    def new_input_set(self):
        return AddUserIdentityInputSet()

    def _make_result_set(self, result, path):
        return AddUserIdentityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddUserIdentityChoreographyExecution(session, exec_id, path)

class AddUserIdentityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddUserIdentity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((conditional, string) The ID of the user.)
        """
        InputSet._set_input(self, 'ID', value)
    def set_Identity(self, value):
        """
        Set the value of the Identity input for this Choreo. ((required, string) The unique idenity (e.g.  test@test.com, test@gmail.com, screen_name))
        """
        InputSet._set_input(self, 'Identity', value)
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
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((conditional, string) Type of identity to add (e.g. email, facebook, twitter, google))
        """
        InputSet._set_input(self, 'Type', value)

class AddUserIdentityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddUserIdentity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class AddUserIdentityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddUserIdentityResultSet(response, path)
