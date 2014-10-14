# -*- coding: utf-8 -*-

###############################################################################
#
# InsertInstance
# Creates an Instance resource in the specified project.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class InsertInstance(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the InsertInstance Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/ComputeEngine/Instances/InsertInstance')


    def new_input_set(self):
        return InsertInstanceInputSet()

    def _make_result_set(self, result, path):
        return InsertInstanceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return InsertInstanceChoreographyExecution(session, exec_id, path)

class InsertInstanceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the InsertInstance
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_InstanceResource(self, value):
        """
        Set the value of the InstanceResource input for this Choreo. ((optional, json) A JSON string containing the instance resource properties to set. This an be used as an alternative to individual inputs representing instance properties.)
        """
        InputSet._set_input(self, 'InstanceResource', value)
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
        Set the value of the Description input for this Choreo. ((optional, string) The description of the instance.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_Disks(self, value):
        """
        Set the value of the Disks input for this Choreo. ((conditional, json) An array of persistent disks. This array contains the following properties: source, type, and boot.)
        """
        InputSet._set_input(self, 'Disks', value)
    def set_MachineType(self, value):
        """
        Set the value of the MachineType input for this Choreo. ((conditional, string) The fully-qualified URL of the machine type resource to use for this instance.)
        """
        InputSet._set_input(self, 'MachineType', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((conditional, string) The name of the instance being created.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_NetworkInterfaces(self, value):
        """
        Set the value of the NetworkInterfaces input for this Choreo. ((conditional, json) An array of network configurations for this instance. This array contains the following properties: network, accessConfigs[], accessConfigs[].name, and accessConfigs[].type.)
        """
        InputSet._set_input(self, 'NetworkInterfaces', value)
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
    def set_Zone(self, value):
        """
        Set the value of the Zone input for this Choreo. ((required, string) The name of the zone associated with this request.)
        """
        InputSet._set_input(self, 'Zone', value)

class InsertInstanceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the InsertInstance Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)

class InsertInstanceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return InsertInstanceResultSet(response, path)
