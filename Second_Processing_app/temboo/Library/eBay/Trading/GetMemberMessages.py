# -*- coding: utf-8 -*-

###############################################################################
#
# GetMemberMessages
# Retrieves a list of the messages that buyers have posted about your active item listings.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetMemberMessages(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetMemberMessages Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/eBay/Trading/GetMemberMessages')


    def new_input_set(self):
        return GetMemberMessagesInputSet()

    def _make_result_set(self, result, path):
        return GetMemberMessagesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMemberMessagesChoreographyExecution(session, exec_id, path)

class GetMemberMessagesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetMemberMessages
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DisplayToPublic(self, value):
        """
        Set the value of the DisplayToPublic input for this Choreo. ((optional, boolean) When set to true, only public messages (viewable in the Item listing) are returned.)
        """
        InputSet._set_input(self, 'DisplayToPublic', value)
    def set_EndCreationTime(self, value):
        """
        Set the value of the EndCreationTime input for this Choreo. ((optional, date) Used to filter by date range (e.g., 2013-02-08T00:00:00.000Z).)
        """
        InputSet._set_input(self, 'EndCreationTime', value)
    def set_EntriesPerPage(self, value):
        """
        Set the value of the EntriesPerPage input for this Choreo. ((optional, integer) The maximum number of records to return in the result.)
        """
        InputSet._set_input(self, 'EntriesPerPage', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((optional, string) The ID of the item the message is about.)
        """
        InputSet._set_input(self, 'ItemID', value)
    def set_MailMessageType(self, value):
        """
        Set the value of the MailMessageType input for this Choreo. ((required, string) The type of message to retrieve. Valid values are: All and AskSellerQuestion. When set to AskSellerQuestion, ItemID or a date range filter must be specified.)
        """
        InputSet._set_input(self, 'MailMessageType', value)
    def set_MemberMessageID(self, value):
        """
        Set the value of the MemberMessageID input for this Choreo. ((optional, string) An ID that uniquely identifies the message for a given user to be retrieved.)
        """
        InputSet._set_input(self, 'MemberMessageID', value)
    def set_MessageStatus(self, value):
        """
        Set the value of the MessageStatus input for this Choreo. ((optional, string) The status of the message. Valid values are: Answered and Unanswered.)
        """
        InputSet._set_input(self, 'MessageStatus', value)
    def set_PageNumber(self, value):
        """
        Set the value of the PageNumber input for this Choreo. ((optional, integer) Specifies the page number of the results to return.)
        """
        InputSet._set_input(self, 'PageNumber', value)
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
    def set_SenderID(self, value):
        """
        Set the value of the SenderID input for this Choreo. ((optional, string) The seller's UserID.)
        """
        InputSet._set_input(self, 'SenderID', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        InputSet._set_input(self, 'SiteID', value)
    def set_StartCreationTime(self, value):
        """
        Set the value of the StartCreationTime input for this Choreo. ((optional, date) Used to filter by date range (e.g., 2013-02-08T00:00:00.000Z).)
        """
        InputSet._set_input(self, 'StartCreationTime', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        InputSet._set_input(self, 'UserToken', value)

class GetMemberMessagesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetMemberMessages Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class GetMemberMessagesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetMemberMessagesResultSet(response, path)
