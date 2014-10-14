# -*- coding: utf-8 -*-

###############################################################################
#
# AttachVolume
# Attaches an Amazon EBS volume to a running instance and exposes it as the specified device.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AttachVolume(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AttachVolume Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/AttachVolume')


    def new_input_set(self):
        return AttachVolumeInputSet()

    def _make_result_set(self, result, path):
        return AttachVolumeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AttachVolumeChoreographyExecution(session, exec_id, path)

class AttachVolumeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AttachVolume
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
    def set_Device(self, value):
        """
        Set the value of the Device input for this Choreo. ((required, string) How the device is exposed to the instance (i.e. " /dev/sdh" or "xvdh").)
        """
        InputSet._set_input(self, 'Device', value)
    def set_InstanceId(self, value):
        """
        Set the value of the InstanceId input for this Choreo. ((required, string) The ID of the instance to which the volume attaches. The volume and instance must be within the same Availability Zone and the instance must be running.)
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
    def set_VolumeId(self, value):
        """
        Set the value of the VolumeId input for this Choreo. ((required, string) The ID of the Amazon EBS volume. The volume and instance must be within the same Availability Zone and the instance must be running.)
        """
        InputSet._set_input(self, 'VolumeId', value)

class AttachVolumeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AttachVolume Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class AttachVolumeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AttachVolumeResultSet(response, path)
