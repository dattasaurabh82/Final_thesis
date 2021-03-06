# -*- coding: utf-8 -*-

###############################################################################
#
# FetchToken
# Completes the authentication process by retrieving an eBay user token after they have visited the authorization URL returned by the GetSessionID Choreo and clicked "I agree".
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FetchToken(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FetchToken Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/eBay/Trading/FetchToken')


    def new_input_set(self):
        return FetchTokenInputSet()

    def _make_result_set(self, result, path):
        return FetchTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FetchTokenChoreographyExecution(session, exec_id, path)

class FetchTokenInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FetchToken
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The unique identifier for the application.)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_CertID(self, value):
        """
        Set the value of the CertID input for this Choreo. ((required, string) The certificate that authenticates the application when making API calls.)
        """
        InputSet._set_input(self, 'CertID', value)
    def set_DevID(self, value):
        """
        Set the value of the DevID input for this Choreo. ((required, string) The unique identifier for the developer's account.)
        """
        InputSet._set_input(self, 'DevID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((optional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        InputSet._set_input(self, 'SandboxMode', value)
    def set_SessionID(self, value):
        """
        Set the value of the SessionID input for this Choreo. ((required, string) The SessionID returned from PayPal. This gets passed to the FetchToken Choreo after the user authorizes the request.)
        """
        InputSet._set_input(self, 'SessionID', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        InputSet._set_input(self, 'SiteID', value)
    def set_Timeout(self, value):
        """
        Set the value of the Timeout input for this Choreo. ((optional, integer) The amount of time (in seconds) to poll eBay to see if your app's user has allowed or denied the request for access. Defaults to 20. Max is 60.)
        """
        InputSet._set_input(self, 'Timeout', value)

class FetchTokenResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FetchToken Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)
    def get_UserToken(self):
        """
        Retrieve the value for the "UserToken" output from this Choreo execution. ((string) An eBay Auth Token which can be used to make requests the user's behalf.)
        """
        return self._output.get('UserToken', None)

class FetchTokenChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FetchTokenResultSet(response, path)
