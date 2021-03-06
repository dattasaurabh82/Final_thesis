# -*- coding: utf-8 -*-

###############################################################################
#
# ListDocuments
# Lists or queries documents within a collection.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListDocuments(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListDocuments Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/MongoHQ/Documents/ListDocuments')


    def new_input_set(self):
        return ListDocumentsInputSet()

    def _make_result_set(self, result, path):
        return ListDocumentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListDocumentsChoreographyExecution(session, exec_id, path)

class ListDocumentsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListDocuments
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIToken(self, value):
        """
        Set the value of the APIToken input for this Choreo. ((required, string) The API Token provided by MongoHQ.)
        """
        InputSet._set_input(self, 'APIToken', value)
    def set_CollectionName(self, value):
        """
        Set the value of the CollectionName input for this Choreo. ((required, string) The name of the collection associated with the documents to list.)
        """
        InputSet._set_input(self, 'CollectionName', value)
    def set_DatabaseName(self, value):
        """
        Set the value of the DatabaseName input for this Choreo. ((required, string) The name of the database associated with the documents to list.)
        """
        InputSet._set_input(self, 'DatabaseName', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, json) A JSON array of fields to return.)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of documents to return. Used with the Skip parameter to paginate through a large set of results.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, json) A JSON string used to query documents.)
        """
        InputSet._set_input(self, 'Query', value)
    def set_Skip(self, value):
        """
        Set the value of the Skip input for this Choreo. ((optional, integer) The number of documents to skip. Used with Limit parameter to paginate through a large set of results.)
        """
        InputSet._set_input(self, 'Skip', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, json) A JSON string describing how the results should be sorted.)
        """
        InputSet._set_input(self, 'Sort', value)

class ListDocumentsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListDocuments Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_DocumentCount(self):
        """
        Retrieve the value for the "DocumentCount" output from this Choreo execution. ((integer) The total number of documents that match the query or list.)
        """
        return self._output.get('DocumentCount', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from MongoHQ.)
        """
        return self._output.get('Response', None)

class ListDocumentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListDocumentsResultSet(response, path)
