# -*- coding: utf-8 -*-

###############################################################################
#
# RestoreFileToRevision
# Restores a specified file to a previous revision.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RestoreFileToRevision(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RestoreFileToRevision Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Dropbox/FilesAndMetadata/RestoreFileToRevision')


    def new_input_set(self):
        return RestoreFileToRevisionInputSet()

    def _make_result_set(self, result, path):
        return RestoreFileToRevisionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RestoreFileToRevisionChoreographyExecution(session, exec_id, path)

class RestoreFileToRevisionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RestoreFileToRevision
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
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
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Dropbox (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'AppKey', value)
    def set_AppSecret(self, value):
        """
        Set the value of the AppSecret input for this Choreo. ((required, string) The App Secret provided by Dropbox (AKA the OAuth Consumer Secret).)
        """
        InputSet._set_input(self, 'AppSecret', value)
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((required, string) The path to the file that you want to return revisions for (i.e. RootFolder/SubFolder/MyFile.txt).)
        """
        InputSet._set_input(self, 'Path', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Revision(self, value):
        """
        Set the value of the Revision input for this Choreo. ((required, string) The revision of the file to restore. The revision ID can be retrieved by running the GetFileRevision Choreo.)
        """
        InputSet._set_input(self, 'Revision', value)
    def set_Root(self, value):
        """
        Set the value of the Root input for this Choreo. ((conditional, string) The root relative to which path is specified. Valid values are "sandbox" and "dropbox" (the default). When your access token has the App folder level of access, this should be set to "sandbox".)
        """
        InputSet._set_input(self, 'Root', value)

class RestoreFileToRevisionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RestoreFileToRevision Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class RestoreFileToRevisionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RestoreFileToRevisionResultSet(response, path)
