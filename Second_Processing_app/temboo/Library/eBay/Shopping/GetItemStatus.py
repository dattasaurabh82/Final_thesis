# -*- coding: utf-8 -*-

###############################################################################
#
# GetItemStatus
# Allows you to get the status for a group of items.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetItemStatus(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetItemStatus Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/eBay/Shopping/GetItemStatus')


    def new_input_set(self):
        return GetItemStatusInputSet()

    def _make_result_set(self, result, path):
        return GetItemStatusResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetItemStatusChoreographyExecution(session, exec_id, path)

class GetItemStatusInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetItemStatus
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The unique identifier for the application.)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((required, string) The ID of an item to retrieve the status for. Multiple item IDs can be separated by commas.)
        """
        InputSet._set_input(self, 'ItemID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((optional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        InputSet._set_input(self, 'SandboxMode', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        InputSet._set_input(self, 'SiteID', value)

class GetItemStatusResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetItemStatus Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class GetItemStatusChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetItemStatusResultSet(response, path)
