# -*- coding: utf-8 -*-

###############################################################################
#
# InsertNetwork
# Creates a new Network resource in the specified project.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class InsertNetwork(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the InsertNetwork Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/ComputeEngine/Networks/InsertNetwork')


    def new_input_set(self):
        return InsertNetworkInputSet()

    def _make_result_set(self, result, path):
        return InsertNetworkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return InsertNetworkChoreographyExecution(session, exec_id, path)

class InsertNetworkInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the InsertNetwork
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_NetworkResource(self, value):
        """
        Set the value of the NetworkResource input for this Choreo. ((optional, json) A JSON string containing the network resource properties you wish to set. This can be used as an alternative to individual inputs that represent network resource properties.)
        """
        InputSet._set_input(self, 'NetworkResource', value)
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
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A description of the network.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_GatewayIP(self, value):
        """
        Set the value of the GatewayIP input for this Choreo. ((optional, string) An optional address used for default routing to other networks. Must be within the range specified by IPRange.)
        """
        InputSet._set_input(self, 'GatewayIP', value)
    def set_IPRange(self, value):
        """
        Set the value of the IPRange input for this Choreo. ((conditional, string) The range of internal addresses that are allowed on the network.)
        """
        InputSet._set_input(self, 'IPRange', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((conditional, string) The name of the network.)
        """
        InputSet._set_input(self, 'Name', value)
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

class InsertNetworkResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the InsertNetwork Choreo.
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

class InsertNetworkChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return InsertNetworkResultSet(response, path)
