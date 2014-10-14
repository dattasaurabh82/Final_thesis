# -*- coding: utf-8 -*-

###############################################################################
#
# AddAccessConfig
# Adds an access config to an instance's network interface.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AddAccessConfig(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddAccessConfig Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/ComputeEngine/Instances/AddAccessConfig')


    def new_input_set(self):
        return AddAccessConfigInputSet()

    def _make_result_set(self, result, path):
        return AddAccessConfigResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddAccessConfigChoreographyExecution(session, exec_id, path)

class AddAccessConfigInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddAccessConfig
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessConfiguration(self, value):
        """
        Set the value of the AccessConfiguration input for this Choreo. ((optional, json) A JSON string containing the access configuration properties you wish to set. This can be used as an alternative to individual inputs that represent access configuration properties.)
        """
        InputSet._set_input(self, 'AccessConfiguration', value)
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
    def set_Instance(self, value):
        """
        Set the value of the Instance input for this Choreo. ((required, string) Name of the instance for which to add an access configuration.)
        """
        InputSet._set_input(self, 'Instance', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((optional, string) The name of this access configuration. Defaults to "External NAT" if not specified.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_NatIP(self, value):
        """
        Set the value of the NatIP input for this Choreo. ((optional, string) An external IP address associated with this instance. Specify an unused static IP address available to the project. An external IP will be drawn from a shared ephemeral pool when not specified.)
        """
        InputSet._set_input(self, 'NatIP', value)
    def set_NetworkInterface(self, value):
        """
        Set the value of the NetworkInterface input for this Choreo. ((required, string) The name of the network interface to add the access config (e.g. nic0, nic1, etc).)
        """
        InputSet._set_input(self, 'NetworkInterface', value)
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
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((required, string) Type of configuration. Must be set to ONE_TO_ONE_NAT.)
        """
        InputSet._set_input(self, 'Type', value)
    def set_Zone(self, value):
        """
        Set the value of the Zone input for this Choreo. ((required, string) The name of the zone associated with this request.)
        """
        InputSet._set_input(self, 'Zone', value)

class AddAccessConfigResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddAccessConfig Choreo.
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

class AddAccessConfigChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddAccessConfigResultSet(response, path)
