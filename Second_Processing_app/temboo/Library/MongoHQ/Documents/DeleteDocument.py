# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteDocument
# Deletes a specific document within a collection.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteDocument(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteDocument Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/MongoHQ/Documents/DeleteDocument')


    def new_input_set(self):
        return DeleteDocumentInputSet()

    def _make_result_set(self, result, path):
        return DeleteDocumentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteDocumentChoreographyExecution(session, exec_id, path)

class DeleteDocumentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteDocument
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIToken(self, value):
        """
        Set the value of the APIToken input for this Choreo. ((required, string) The API Token provided by MongoHQ.)
        """
        InputSet._set_input(self, 'APIToken', value)
    def set_CollectionName(self, value):
        """
        Set the value of the CollectionName input for this Choreo. ((required, string) The name of the collection associated with the document to delete.)
        """
        InputSet._set_input(self, 'CollectionName', value)
    def set_DatabaseName(self, value):
        """
        Set the value of the DatabaseName input for this Choreo. ((required, string) The name of the database associated with the document to delete.)
        """
        InputSet._set_input(self, 'DatabaseName', value)
    def set_DocumentID(self, value):
        """
        Set the value of the DocumentID input for this Choreo. ((required, string) The ID of the document to delete.)
        """
        InputSet._set_input(self, 'DocumentID', value)

class DeleteDocumentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteDocument Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from MongoHQ.)
        """
        return self._output.get('Response', None)

class DeleteDocumentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteDocumentResultSet(response, path)
