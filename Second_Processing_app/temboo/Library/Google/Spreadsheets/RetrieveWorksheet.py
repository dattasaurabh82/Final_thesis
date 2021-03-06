# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveWorksheet
# Retrieves a specified worksheet from a Google spreadsheet in CSV, XML, or JSON format.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RetrieveWorksheet(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveWorksheet Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/RetrieveWorksheet')


    def new_input_set(self):
        return RetrieveWorksheetInputSet()

    def _make_result_set(self, result, path):
        return RetrieveWorksheetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveWorksheetChoreographyExecution(session, exec_id, path)

class RetrieveWorksheetInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveWorksheet
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password)
        """
        InputSet._set_input(self, 'Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: csv (the default), xml, and json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((required, string) The unique key of the spreadsheet associated with the worksheet you want to retrieve. Required unless SpreadsheetName and WorksheetName are supplied.)
        """
        InputSet._set_input(self, 'SpreadsheetKey', value)
    def set_SpreadsheetName(self, value):
        """
        Set the value of the SpreadsheetName input for this Choreo. ((optional, string) The name of the spreadsheet to retrieve. This and WorksheetName can be used as an alternative to SpreadsheetKey and WorksheetId to lookup spreadsheet details by name.)
        """
        InputSet._set_input(self, 'SpreadsheetName', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        InputSet._set_input(self, 'Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((required, string) The unique ID of the worksheet that you want to retrieve. Required unless SpreadsheetName and WorksheetName are supplied.)
        """
        InputSet._set_input(self, 'WorksheetId', value)
    def set_WorksheetName(self, value):
        """
        Set the value of the WorksheetName input for this Choreo. ((optional, string) The name of the worksheet to retrieve. This and SpreadsheetName can be used as an alternative to SpreadsheetKey and WorksheetId to lookup spreadsheet details by name.)
        """
        InputSet._set_input(self, 'WorksheetName', value)

class RetrieveWorksheetResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveWorksheet Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((multiline) The response from Google.)
        """
        return self._output.get('Response', None)

class RetrieveWorksheetChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveWorksheetResultSet(response, path)
