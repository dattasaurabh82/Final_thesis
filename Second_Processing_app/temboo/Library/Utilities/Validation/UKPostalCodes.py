# -*- coding: utf-8 -*-

###############################################################################
#
# UKPostalCodes
# Verifies that a given zip code matches the format expected for UK addresses.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UKPostalCodes(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UKPostalCodes Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/Validation/UKPostalCodes')


    def new_input_set(self):
        return UKPostalCodesInputSet()

    def _make_result_set(self, result, path):
        return UKPostalCodesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UKPostalCodesChoreographyExecution(session, exec_id, path)

class UKPostalCodesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UKPostalCodes
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ZipCode(self, value):
        """
        Set the value of the ZipCode input for this Choreo. ((required, string) The zip code to validate. Letters must be in uppercase to be valid.)
        """
        InputSet._set_input(self, 'ZipCode', value)

class UKPostalCodesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UKPostalCodes Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Match(self):
        """
        Retrieve the value for the "Match" output from this Choreo execution. ((string) Contains a string indicating the result of the match -- "valid" or "invalid".)
        """
        return self._output.get('Match', None)

class UKPostalCodesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UKPostalCodesResultSet(response, path)
