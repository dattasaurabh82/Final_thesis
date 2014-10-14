# -*- coding: utf-8 -*-

###############################################################################
#
# CreateCommitComment
# Creates a comment on a specified commit.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateCommitComment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateCommitComment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GitHub/ReposAPI/Comments/CreateCommitComment')


    def new_input_set(self):
        return CreateCommitCommentInputSet()

    def _make_result_set(self, result, path):
        return CreateCommitCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateCommitCommentChoreographyExecution(session, exec_id, path)

class CreateCommitCommentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateCommitComment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Body(self, value):
        """
        Set the value of the Body input for this Choreo. ((required, string) The comment text.)
        """
        InputSet._set_input(self, 'Body', value)
    def set_Line(self, value):
        """
        Set the value of the Line input for this Choreo. ((required, integer) The line number in the file to comment on.)
        """
        InputSet._set_input(self, 'Line', value)
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((required, string) The relative path of the file to comment on.)
        """
        InputSet._set_input(self, 'Path', value)
    def set_Position(self, value):
        """
        Set the value of the Position input for this Choreo. ((required, integer) The line index in the diff to comment on.)
        """
        InputSet._set_input(self, 'Position', value)
    def set_Repo(self, value):
        """
        Set the value of the Repo input for this Choreo. ((required, string) The name of the repo that the comment is associated with.)
        """
        InputSet._set_input(self, 'Repo', value)
    def set_SHA(self, value):
        """
        Set the value of the SHA input for this Choreo. ((required, string) The SHA or id of the commit.)
        """
        InputSet._set_input(self, 'SHA', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) The GitHub username.)
        """
        InputSet._set_input(self, 'User', value)

class CreateCommitCommentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateCommitComment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from GitHub.)
        """
        return self._output.get('Response', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The remaining number of API requests available to you. This is returned in the GitHub response header.)
        """
        return self._output.get('Remaining', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The available rate limit for your account. This is returned in the GitHub response header.)
        """
        return self._output.get('Limit', None)

class CreateCommitCommentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateCommitCommentResultSet(response, path)
