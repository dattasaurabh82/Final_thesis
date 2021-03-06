# -*- coding: utf-8 -*-

###############################################################################
#
# CreateRating
# Creates an action that represents a user giving a book a rating.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateRating(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateRating Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Actions/Books/Rates/CreateRating')


    def new_input_set(self):
        return CreateRatingInputSet()

    def _make_result_set(self, result, path):
        return CreateRatingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateRatingChoreographyExecution(session, exec_id, path)

class CreateRatingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateRating
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Book(self, value):
        """
        Set the value of the Book input for this Choreo. ((required, string) The URL or ID for an Open Graph object representing the book.)
        """
        InputSet._set_input(self, 'Book', value)
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
        Set the value of the ExpiresIn input for this Choreo. ((optional, integer) The amount of time (in milliseconds) from the publish_time that the action will expire.)
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
        Set the value of the Message input for this Choreo. ((optional, string) A message attached to this action. Setting this parameter requires enabling of message capabilities.)
        """
        InputSet._set_input(self, 'Message', value)
    def set_NoFeedStory(self, value):
        """
        Set the value of the NoFeedStory input for this Choreo. ((optional, boolean) Whether or not this action should be posted to the users feed.)
        """
        InputSet._set_input(self, 'NoFeedStory', value)
    def set_Place(self, value):
        """
        Set the value of the Place input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing the location associated with this action.)
        """
        InputSet._set_input(self, 'Place', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The id of the user's profile. Defaults to "me" indicating the authenticated user.)
        """
        InputSet._set_input(self, 'ProfileID', value)
    def set_RatingNormalizedValue(self, value):
        """
        Set the value of the RatingNormalizedValue input for this Choreo. ((required, decimal) The rating expressed as a decimal value between 0 and 1.0.)
        """
        InputSet._set_input(self, 'RatingNormalizedValue', value)
    def set_RatingScale(self, value):
        """
        Set the value of the RatingScale input for this Choreo. ((required, integer) The highest possible value in the rating scale.)
        """
        InputSet._set_input(self, 'RatingScale', value)
    def set_RatingValue(self, value):
        """
        Set the value of the RatingValue input for this Choreo. ((required, decimal) The value of the book rating.)
        """
        InputSet._set_input(self, 'RatingValue', value)
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
    def set_ReviewText(self, value):
        """
        Set the value of the ReviewText input for this Choreo. ((conditional, string) The text content of the book review.)
        """
        InputSet._set_input(self, 'ReviewText', value)
    def set_Review(self, value):
        """
        Set the value of the Review input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing a book review.)
        """
        InputSet._set_input(self, 'Review', value)
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

class CreateRatingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateRating Choreo.
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
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook.)
        """
        return self._output.get('Response', None)

class CreateRatingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateRatingResultSet(response, path)
