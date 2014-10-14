# -*- coding: utf-8 -*-

###############################################################################
#
# ShowSubscriber
# Verifies that the specified user is a subscriber of the specified list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ShowSubscriber(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ShowSubscriber Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Lists/ShowSubscriber')


    def new_input_set(self):
        return ShowSubscriberInputSet()

    def _make_result_set(self, result, path):
        return ShowSubscriberResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShowSubscriberChoreographyExecution(session, exec_id, path)

class ShowSubscriberInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ShowSubscriber
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Twitter.)
        """
        InputSet._set_input(self, 'ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Twitter.)
        """
        InputSet._set_input(self, 'ConsumerSecret', value)
    def set_IncludeEntities(self, value):
        """
        Set the value of the IncludeEntities input for this Choreo. ((optional, boolean) The "entities" node containing extra metadata will not be included when set to false.)
        """
        InputSet._set_input(self, 'IncludeEntities', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((conditional, string) The numerical ID of the list. Required unless Slug is provided.)
        """
        InputSet._set_input(self, 'ListId', value)
    def set_OwnerId(self, value):
        """
        Set the value of the OwnerId input for this Choreo. ((optional, string) The user ID of the user who owns the list being requested by a slug.)
        """
        InputSet._set_input(self, 'OwnerId', value)
    def set_OwnerScreenName(self, value):
        """
        Set the value of the OwnerScreenName input for this Choreo. ((optional, string) The screen name of the user who owns the list being requested by a slug.)
        """
        InputSet._set_input(self, 'OwnerScreenName', value)
    def set_ScreenName(self, value):
        """
        Set the value of the ScreenName input for this Choreo. ((conditional, string) The screen name of the user to retrieve from the list. Required unless providing the UserId.)
        """
        InputSet._set_input(self, 'ScreenName', value)
    def set_SkipStatus(self, value):
        """
        Set the value of the SkipStatus input for this Choreo. ((optional, boolean) When set to either true, statuses will not be included in the returned user objects.)
        """
        InputSet._set_input(self, 'SkipStatus', value)
    def set_Slug(self, value):
        """
        Set the value of the Slug input for this Choreo. ((optional, string) When identifying a list by a slug, either OwnerScreenName or OwnerId must be provided.)
        """
        InputSet._set_input(self, 'Slug', value)
    def set_UserId(self, value):
        """
        Set the value of the UserId input for this Choreo. ((conditional, string) The ID of the user to retrieve from the list. Required unless providing the ScreenName.)
        """
        InputSet._set_input(self, 'UserId', value)

class ShowSubscriberResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ShowSubscriber Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The number of requests left for the 15 minute window.)
        """
        return self._output.get('Remaining', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)
    def get_Reset(self):
        """
        Retrieve the value for the "Reset" output from this Choreo execution. ((date) The remaining window before the rate limit resets in UTC epoch seconds.)
        """
        return self._output.get('Reset', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The rate limit ceiling for this particular request.)
        """
        return self._output.get('Limit', None)

class ShowSubscriberChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShowSubscriberResultSet(response, path)
