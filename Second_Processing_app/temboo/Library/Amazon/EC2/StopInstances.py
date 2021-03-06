# -*- coding: utf-8 -*-

###############################################################################
#
# StopInstances
# Stops an Amazon EBS-backed instance.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class StopInstances(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the StopInstances Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/StopInstances')


    def new_input_set(self):
        return StopInstancesInputSet()

    def _make_result_set(self, result, path):
        return StopInstancesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return StopInstancesChoreographyExecution(session, exec_id, path)

class StopInstancesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the StopInstances
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSSecretKeyId', value)
    def set_InstanceId(self, value):
        """
        Set the value of the InstanceId input for this Choreo. ((required, string) The instance ID to stop. This can be a comma-separated list of up to 10 instance IDs.)
        """
        InputSet._set_input(self, 'InstanceId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the EC2 endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        InputSet._set_input(self, 'UserRegion', value)

class StopInstancesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the StopInstances Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class StopInstancesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return StopInstancesResultSet(response, path)
