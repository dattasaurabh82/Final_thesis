# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteObject
# Deletes a given object.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteObject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteObject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Parse/Objects/DeleteObject')


    def new_input_set(self):
        return DeleteObjectInputSet()

    def _make_result_set(self, result, path):
        return DeleteObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteObjectChoreographyExecution(session, exec_id, path)

class DeleteObjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteObject
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        InputSet._set_input(self, 'ApplicationID', value)
    def set_ClassName(self, value):
        """
        Set the value of the ClassName input for this Choreo. ((required, string) The class name for the object being deleted.)
        """
        InputSet._set_input(self, 'ClassName', value)
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((required, string) The ID of the object to delete.)
        """
        InputSet._set_input(self, 'ObjectID', value)
    def set_RESTAPIKey(self, value):
        """
        Set the value of the RESTAPIKey input for this Choreo. ((required, string) The REST API Key provided by Parse.)
        """
        InputSet._set_input(self, 'RESTAPIKey', value)

class DeleteObjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteObject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class DeleteObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteObjectResultSet(response, path)
