# -*- coding: utf-8 -*-

###############################################################################
#
# Subscribe
# Allows your application to subscribe users to notifications. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Subscribe(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Subscribe Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Withings/Notification/Subscribe')


    def new_input_set(self):
        return SubscribeInputSet()

    def _make_result_set(self, result, path):
        return SubscribeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SubscribeChoreographyExecution(session, exec_id, path)

class SubscribeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Subscribe
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Application(self, value):
        """
        Set the value of the Application input for this Choreo. ((optional, integer) Specifies the device type for which the notification is to be activated. Set to 1 for Bodyscale.)
        """
        InputSet._set_input(self, 'Application', value)
    def set_CallbackURL(self, value):
        """
        Set the value of the CallbackURL input for this Choreo. ((required, string) The URL the API notification will be pushed to.)
        """
        InputSet._set_input(self, 'CallbackURL', value)
    def set_Comment(self, value):
        """
        Set the value of the Comment input for this Choreo. ((optional, string) A comment string used for a description to display to the user when presenting them with your notification setup.)
        """
        InputSet._set_input(self, 'Comment', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Withings.)
        """
        InputSet._set_input(self, 'ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Withings.)
        """
        InputSet._set_input(self, 'ConsumerSecret', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The ID of the user to setup a subscription for.)
        """
        InputSet._set_input(self, 'UserID', value)

class SubscribeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Subscribe Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Withings.)
        """
        return self._output.get('Response', None)

class SubscribeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SubscribeResultSet(response, path)
