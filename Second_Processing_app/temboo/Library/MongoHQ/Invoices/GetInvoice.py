# -*- coding: utf-8 -*-

###############################################################################
#
# GetInvoice
# Retrieves a specific invoice by ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetInvoice(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetInvoice Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/MongoHQ/Invoices/GetInvoice')


    def new_input_set(self):
        return GetInvoiceInputSet()

    def _make_result_set(self, result, path):
        return GetInvoiceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetInvoiceChoreographyExecution(session, exec_id, path)

class GetInvoiceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetInvoice
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIToken(self, value):
        """
        Set the value of the APIToken input for this Choreo. ((required, string) The API Token provided by MongoHQ.)
        """
        InputSet._set_input(self, 'APIToken', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, string) The ID of the invoice to retrieve.)
        """
        InputSet._set_input(self, 'ID', value)

class GetInvoiceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetInvoice Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from MongoHQ.)
        """
        return self._output.get('Response', None)

class GetInvoiceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetInvoiceResultSet(response, path)
