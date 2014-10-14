# -*- coding: utf-8 -*-

###############################################################################
#
# StructuredQuery
# Retrieves a list-based feed containing data in your Google spreadsheet that meets a specified criteria.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class StructuredQuery(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the StructuredQuery Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/StructuredQuery')


    def new_input_set(self):
        return StructuredQueryInputSet()

    def _make_result_set(self, result, path):
        return StructuredQueryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return StructuredQueryChoreographyExecution(session, exec_id, path)

class StructuredQueryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the StructuredQuery
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) A valid structured query (i.e. id>4).)
        """
        InputSet._set_input(self, 'Query', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((required, string) The unique key of the spreadsheet associated with the feed you want to retrieve.)
        """
        InputSet._set_input(self, 'SpreadsheetKey', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        InputSet._set_input(self, 'Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((required, string) The unique ID of the worksheet associated with the feed you want to retrieve.)
        """
        InputSet._set_input(self, 'WorksheetId', value)

class StructuredQueryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the StructuredQuery Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google.)
        """
        return self._output.get('Response', None)

class StructuredQueryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return StructuredQueryResultSet(response, path)
