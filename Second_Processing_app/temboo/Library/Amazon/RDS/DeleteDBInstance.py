# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteDBInstance
# Deletes a specified database instance.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteDBInstance(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteDBInstance Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/DeleteDBInstance')


    def new_input_set(self):
        return DeleteDBInstanceInputSet()

    def _make_result_set(self, result, path):
        return DeleteDBInstanceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteDBInstanceChoreographyExecution(session, exec_id, path)

class DeleteDBInstanceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteDBInstance
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
    def set_DBInstanceIdentifier(self, value):
        """
        Set the value of the DBInstanceIdentifier input for this Choreo. ((required, string) The ID for the DB instance to delete.)
        """
        InputSet._set_input(self, 'DBInstanceIdentifier', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the RDS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        InputSet._set_input(self, 'UserRegion', value)

class DeleteDBInstanceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteDBInstance Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class DeleteDBInstanceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteDBInstanceResultSet(response, path)
