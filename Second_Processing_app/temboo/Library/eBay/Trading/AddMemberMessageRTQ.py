# -*- coding: utf-8 -*-

###############################################################################
#
# AddMemberMessageRTQ
# Allows a seller to reply to a question about an active item listing.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AddMemberMessageRTQ(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddMemberMessageRTQ Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/eBay/Trading/AddMemberMessageRTQ')


    def new_input_set(self):
        return AddMemberMessageRTQInputSet()

    def _make_result_set(self, result, path):
        return AddMemberMessageRTQResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddMemberMessageRTQChoreographyExecution(session, exec_id, path)

class AddMemberMessageRTQInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddMemberMessageRTQ
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Body(self, value):
        """
        Set the value of the Body input for this Choreo. ((required, string) The message body which should answer the question that an eBay user ask the seller. HTML is not allowed.)
        """
        InputSet._set_input(self, 'Body', value)
    def set_DisplayToPublic(self, value):
        """
        Set the value of the DisplayToPublic input for this Choreo. ((optional, string) When set to true, this indicates that the member message is viewable in the item listing.)
        """
        InputSet._set_input(self, 'DisplayToPublic', value)
    def set_EmailCopyToSender(self, value):
        """
        Set the value of the EmailCopyToSender input for this Choreo. ((optional, boolean) A flag used to indicate that a copy should be sent to the sender.)
        """
        InputSet._set_input(self, 'EmailCopyToSender', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((optional, string) The unique ID of the item about which the question was asked.)
        """
        InputSet._set_input(self, 'ItemID', value)
    def set_ParentMessageID(self, value):
        """
        Set the value of the ParentMessageID input for this Choreo. ((required, string) The ID number of the question to which this message is responding.)
        """
        InputSet._set_input(self, 'ParentMessageID', value)
    def set_RecipientID(self, value):
        """
        Set the value of the RecipientID input for this Choreo. ((required, string) The recipient's eBay user ID.)
        """
        InputSet._set_input(self, 'RecipientID', value)
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
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        InputSet._set_input(self, 'UserToken', value)

class AddMemberMessageRTQResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddMemberMessageRTQ Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class AddMemberMessageRTQChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddMemberMessageRTQResultSet(response, path)
