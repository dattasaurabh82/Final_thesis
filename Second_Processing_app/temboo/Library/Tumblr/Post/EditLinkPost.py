# -*- coding: utf-8 -*-

###############################################################################
#
# EditLinkPost
# Updates a specified link post on a Tumblr blog.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class EditLinkPost(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the EditLinkPost Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Tumblr/Post/EditLinkPost')


    def new_input_set(self):
        return EditLinkPostInputSet()

    def _make_result_set(self, result, path):
        return EditLinkPostResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EditLinkPostChoreographyExecution(session, exec_id, path)

class EditLinkPostInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the EditLinkPost
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((required, string) The link you want to post.)
        """
        InputSet._set_input(self, 'URL', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Tumblr (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_BaseHostname(self, value):
        """
        Set the value of the BaseHostname input for this Choreo. ((required, string) The standard or custom blog hostname (i.e. temboo.tumblr.com).)
        """
        InputSet._set_input(self, 'BaseHostname', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, date) The GMT date and time of the post. Can be an epoch timestamp in milliseconds or formatted like: Dec 8th, 2011 4:03pm. Defaults to NOW().)
        """
        InputSet._set_input(self, 'Date', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A user-supplied description. HTML is allowed.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, integer) The ID of the post you want to edit.)
        """
        InputSet._set_input(self, 'ID', value)
    def set_Markdown(self, value):
        """
        Set the value of the Markdown input for this Choreo. ((optional, boolean) Indicates whether the post uses markdown syntax. Defaults to false. Set to 1 to indicate true.)
        """
        InputSet._set_input(self, 'Markdown', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, multiline) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by Tumblr (AKA the OAuth Consumer Secret).)
        """
        InputSet._set_input(self, 'SecretKey', value)
    def set_Slug(self, value):
        """
        Set the value of the Slug input for this Choreo. ((optional, string) Adds a short text summary to the end of the post URL.)
        """
        InputSet._set_input(self, 'Slug', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) The state of the post. Specify one of the following:  published, draft, queue. Defaults to published.)
        """
        InputSet._set_input(self, 'State', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) Comma-separated tags for this post.)
        """
        InputSet._set_input(self, 'Tags', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, string) The title of the page the link points to. HTML entities should be escaped.)
        """
        InputSet._set_input(self, 'Title', value)
    def set_Tweet(self, value):
        """
        Set the value of the Tweet input for this Choreo. ((optional, string) Manages the autotweet (if enabled) for this post. Defaults to off for no tweet. Enter text to override the default tweet.)
        """
        InputSet._set_input(self, 'Tweet', value)

class EditLinkPostResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the EditLinkPost Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Tumblr. Default is JSON, can be set to XML by entering 'xml' in ResponseFormat.)
        """
        return self._output.get('Response', None)

class EditLinkPostChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EditLinkPostResultSet(response, path)
