# -*- coding: utf-8 -*-

###############################################################################
#
# Insert
# Inserts a new activity into a user's stream.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Insert(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Insert Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Plus/Domains/Activities/Insert')


    def new_input_set(self):
        return InsertInputSet()

    def _make_result_set(self, result, path):
        return InsertResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return InsertChoreographyExecution(session, exec_id, path)

class InsertInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Insert
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ActivityResource(self, value):
        """
        Set the value of the ActivityResource input for this Choreo. ((optional, string) A JSON-formatted string containing the activity properties you wish to set. This can be used as an alternative to setting individual inputs representing resource properties.)
        """
        InputSet._set_input(self, 'ActivityResource', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Callback(self, value):
        """
        Set the value of the Callback input for this Choreo. ((optional, string) Specifies a JavaScript function that will be passed the response data for using the API with JSONP.)
        """
        InputSet._set_input(self, 'Callback', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_Content(self, value):
        """
        Set the value of the Content input for this Choreo. ((required, string) Content to post to your stream.)
        """
        InputSet._set_input(self, 'Content', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A description for the new activity being created.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Used to specify fields to include in a partial response. This can be used to reduce the amount of data returned. See documentation for syntax rules.)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_PrettyPrint(self, value):
        """
        Set the value of the PrettyPrint input for this Choreo. ((optional, boolean) A flag used to pretty print the JSON response to make it more readable. Defaults to "true".)
        """
        InputSet._set_input(self, 'PrettyPrint', value)
    def set_Preview(self, value):
        """
        Set the value of the Preview input for this Choreo. ((optional, boolean) If "true", extract the potential media attachments for a URL. The response will include all possible attachments for a URL, including video, photos, and articles based on the content of the page.)
        """
        InputSet._set_input(self, 'Preview', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)
    def set_ShareWithDomain(self, value):
        """
        Set the value of the ShareWithDomain input for this Choreo. ((optional, boolean) Set to 1 to share this activity with the entire Domain.)
        """
        InputSet._set_input(self, 'ShareWithDomain', value)
    def set_ShareWithExtendedCircles(self, value):
        """
        Set the value of the ShareWithExtendedCircles input for this Choreo. ((optional, boolean) Set to 1 to share this activity your circles plus all the people in their circles.)
        """
        InputSet._set_input(self, 'ShareWithExtendedCircles', value)
    def set_ShareWithMyCircles(self, value):
        """
        Set the value of the ShareWithMyCircles input for this Choreo. ((optional, boolean) Set to 1 to share this activity with everyone in your Circles.)
        """
        InputSet._set_input(self, 'ShareWithMyCircles', value)
    def set_ShareWithPublic(self, value):
        """
        Set the value of the ShareWithPublic input for this Choreo. ((optional, boolean) Set to 1 to share this activity with everyone on the web.)
        """
        InputSet._set_input(self, 'ShareWithPublic', value)
    def set_ShareWithTheseCircles(self, value):
        """
        Set the value of the ShareWithTheseCircles input for this Choreo. ((optional, string) Comma-seperated list of up to 10 IDs of the circles you want to share this activity with.)
        """
        InputSet._set_input(self, 'ShareWithTheseCircles', value)
    def set_ShareWithThesePeople(self, value):
        """
        Set the value of the ShareWithThesePeople input for this Choreo. ((optional, string) Comma-seperated list of up to 10 IDs of persons you want to share this activity with.)
        """
        InputSet._set_input(self, 'ShareWithThesePeople', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The ID of the user to create a circle for. The value "me" is set as the default to indicate the authenticated user.)
        """
        InputSet._set_input(self, 'UserID', value)
    def set_UserIP(self, value):
        """
        Set the value of the UserIP input for this Choreo. ((optional, string) Identifies the IP address of the end user for whom the API call is being made. Used to enforce per-user quotas.)
        """
        InputSet._set_input(self, 'UserIP', value)

class InsertResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Insert Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)

class InsertChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return InsertResultSet(response, path)
