# -*- coding: utf-8 -*-

###############################################################################
#
# CreateCheckin
# Creates a checkin at a location represented by a Page.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateCheckin(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateCheckin Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Publishing/CreateCheckin')


    def new_input_set(self):
        return CreateCheckinInputSet()

    def _make_result_set(self, result, path):
        return CreateCheckinResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateCheckinChoreographyExecution(session, exec_id, path)

class CreateCheckinInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateCheckin
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((optional, decimal) Deprecated (retained for backward compatibility only).)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((optional, decimal) Deprecated (retained for backward compatibility only).)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) A message to include with the Checkin.)
        """
        InputSet._set_input(self, 'Message', value)
    def set_PlaceID(self, value):
        """
        Set the value of the PlaceID input for this Choreo. ((conditional, string) The ID of the place associated with your Checkin.)
        """
        InputSet._set_input(self, 'PlaceID', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The id of the profile to create a checkin for. Defaults to "me" indicating the authenticated user.)
        """
        InputSet._set_input(self, 'ProfileID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class CreateCheckinResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateCheckin Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class CreateCheckinChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateCheckinResultSet(response, path)
