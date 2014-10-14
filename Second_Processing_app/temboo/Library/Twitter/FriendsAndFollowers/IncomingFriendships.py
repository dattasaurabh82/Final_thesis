# -*- coding: utf-8 -*-

###############################################################################
#
# IncomingFriendships
# Retrieves a list of numeric IDs for every user who has a pending request to follow the authenticating user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class IncomingFriendships(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the IncomingFriendships Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twitter/FriendsAndFollowers/IncomingFriendships')


    def new_input_set(self):
        return IncomingFriendshipsInputSet()

    def _make_result_set(self, result, path):
        return IncomingFriendshipsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return IncomingFriendshipsChoreographyExecution(session, exec_id, path)

class IncomingFriendshipsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the IncomingFriendships
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Twitter.)
        """
        InputSet._set_input(self, 'ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Twitter.)
        """
        InputSet._set_input(self, 'ConsumerSecret', value)
    def set_Cursor(self, value):
        """
        Set the value of the Cursor input for this Choreo. ((optional, integer) Allows you to pass in the previous_cursor or next_cursor in order to page through results.)
        """
        InputSet._set_input(self, 'Cursor', value)
    def set_StringifyIDs(self, value):
        """
        Set the value of the StringifyIDs input for this Choreo. ((optional, boolean) A boolean flag indicating that Tweet IDs should be returned as strings.)
        """
        InputSet._set_input(self, 'StringifyIDs', value)

class IncomingFriendshipsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the IncomingFriendships Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The number of requests left for the 15 minute window.)
        """
        return self._output.get('Remaining', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The rate limit ceiling for this particular request.)
        """
        return self._output.get('Limit', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)
    def get_Reset(self):
        """
        Retrieve the value for the "Reset" output from this Choreo execution. ((date) The remaining window before the rate limit resets in UTC epoch seconds.)
        """
        return self._output.get('Reset', None)

class IncomingFriendshipsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return IncomingFriendshipsResultSet(response, path)
