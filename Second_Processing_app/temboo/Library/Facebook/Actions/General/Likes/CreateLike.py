# -*- coding: utf-8 -*-

###############################################################################
#
# CreateLike
# Creates an action representing someone liking an object.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateLike(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateLike Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Actions/General/Likes/CreateLike')


    def new_input_set(self):
        return CreateLikeInputSet()

    def _make_result_set(self, result, path):
        return CreateLikeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateLikeChoreographyExecution(session, exec_id, path)

class CreateLikeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateLike
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_CreatedTime(self, value):
        """
        Set the value of the CreatedTime input for this Choreo. ((optional, date) The time that the action was created (e.g. 2013-06-24T18:53:35+0000).)
        """
        InputSet._set_input(self, 'CreatedTime', value)
    def set_EndTime(self, value):
        """
        Set the value of the EndTime input for this Choreo. ((optional, date) The time that the user ended the action (e.g. 2013-06-24T18:53:35+0000).)
        """
        InputSet._set_input(self, 'EndTime', value)
    def set_ExpiresIn(self, value):
        """
        Set the value of the ExpiresIn input for this Choreo. ((optional, integer) The amount of time (in milleseconds) from the publish_time that the action will expire.)
        """
        InputSet._set_input(self, 'ExpiresIn', value)
    def set_ExplicitlyShared(self, value):
        """
        Set the value of the ExplicitlyShared input for this Choreo. ((optional, boolean) Indicates that the user is explicitly sharing this action. Requires the explicitly_shared capability to be enabled.)
        """
        InputSet._set_input(self, 'ExplicitlyShared', value)
    def set_ExplicityShared(self, value):
        """
        Set the value of the ExplicityShared input for this Choreo. ((optional, boolean) Deprecated (retained for backward compatibility only).)
        """
        InputSet._set_input(self, 'ExplicityShared', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) A message attached to this fitness action. Setting this parameter requires enabling of message capabilities.)
        """
        InputSet._set_input(self, 'Message', value)
    def set_NoFeedStory(self, value):
        """
        Set the value of the NoFeedStory input for this Choreo. ((optional, boolean) Whether or not this action should be posted to the users feed.)
        """
        InputSet._set_input(self, 'NoFeedStory', value)
    def set_Object(self, value):
        """
        Set the value of the Object input for this Choreo. ((required, string) The URL or ID for an Open Graph object to be liked.)
        """
        InputSet._set_input(self, 'Object', value)
    def set_Place(self, value):
        """
        Set the value of the Place input for this Choreo. ((optional, string) The Facebook Page ID of the location associated with this action.)
        """
        InputSet._set_input(self, 'Place', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The id of the profile to retrieve fitness actions for. Defaults to "me" indicating the authenticated user.)
        """
        InputSet._set_input(self, 'ProfileID', value)
    def set_Reference(self, value):
        """
        Set the value of the Reference input for this Choreo. ((optional, string) A string identifier up to 50 characters used for tracking and insights.)
        """
        InputSet._set_input(self, 'Reference', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_StartTime(self, value):
        """
        Set the value of the StartTime input for this Choreo. ((optional, date) The time that the user started the action (e.g. 2013-06-24T18:53:35+0000).)
        """
        InputSet._set_input(self, 'StartTime', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) A comma separated list of other profile IDs that also performed this action.)
        """
        InputSet._set_input(self, 'Tags', value)

class CreateLikeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateLike Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ActivityURL(self):
        """
        Retrieve the value for the "ActivityURL" output from this Choreo execution. ((string) The URL for the newly created action.)
        """
        return self._output.get('ActivityURL', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class CreateLikeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateLikeResultSet(response, path)
