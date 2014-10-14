# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByCallLetters
# Retrieves local NPR member stations based on uniquely identifying call letters.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByCallLetters(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByCallLetters Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NPR/StationFinder/SearchByCallLetters')


    def new_input_set(self):
        return SearchByCallLettersInputSet()

    def _make_result_set(self, result, path):
        return SearchByCallLettersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByCallLettersChoreographyExecution(session, exec_id, path)

class SearchByCallLettersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByCallLetters
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NPR.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Band(self, value):
        """
        Set the value of the Band input for this Choreo. ((optional, string) Enter AM or FM.)
        """
        InputSet._set_input(self, 'Band', value)
    def set_CallLetters(self, value):
        """
        Set the value of the CallLetters input for this Choreo. ((required, string) Enter the unique identifier associated with a station.)
        """
        InputSet._set_input(self, 'CallLetters', value)

class SearchByCallLettersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByCallLetters Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) )
        """
        return self._output.get('Response', None)

class SearchByCallLettersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByCallLettersResultSet(response, path)
