# -*- coding: utf-8 -*-

###############################################################################
#
# CreateTags
# Adds or overwrites one or more tags for the specified EC2 resource or resources.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateTags(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateTags Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/CreateTags')


    def new_input_set(self):
        return CreateTagsInputSet()

    def _make_result_set(self, result, path):
        return CreateTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateTagsChoreographyExecution(session, exec_id, path)

class CreateTagsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateTags
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
    def set_ResourceId(self, value):
        """
        Set the value of the ResourceId input for this Choreo. ((required, string) The ID of a resource to tag. This can be a comma-separated list of up to 10  Resource IDs.)
        """
        InputSet._set_input(self, 'ResourceId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_TagKey(self, value):
        """
        Set the value of the TagKey input for this Choreo. ((required, string) The key for a tag.)
        """
        InputSet._set_input(self, 'TagKey', value)
    def set_TagValue(self, value):
        """
        Set the value of the TagValue input for this Choreo. ((conditional, string) The value for a tag. If empty, the value will be set to be an empty string.)
        """
        InputSet._set_input(self, 'TagValue', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the EC2 endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        InputSet._set_input(self, 'UserRegion', value)

class CreateTagsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateTags Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateTagsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateTagsResultSet(response, path)
