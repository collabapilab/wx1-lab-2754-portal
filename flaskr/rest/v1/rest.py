from requests import get, post, put, delete, packages, request
from requests.exceptions import RequestException, HTTPError
from requests.auth import HTTPBasicAuth
from requests import Session


class REST:
    """
    The REST Server class
    Use this class to connect and make API calls to an most REST-based devices.

    :param host: The Hostname / IP Address of the server
    :param username: The username of user with REST/API access
    :param password: The password for user
    :param port: (optional) The server port for API access (default: 443)
    :param base_url: (optional) The base URL, such as "/api/v1" for a given API
    :param headers: (optional) A dictionary of header key/value pairs
    :param tls_verify: (optional) Whether certificate validation will be performed.
    :type host: String
    :type username: String
    :type password: String
    :type port: Integer
    :type base_url: String
    :type headers: Dict
    :type tls_verify: Bool
    :returns: return an REST object
    :rtype: REST
    """

    def __init__(self, host, username=None, password=None, base_url=None, headers={}, port=443, tls_verify=False):
        """
        Initialize an object with the host, port, and base_url using the parameters passed in.
        """
        self.host = host
        self.port = str(port)
        self.base_url = base_url

        self.session = Session()
        self.session.auth = HTTPBasicAuth(username, password)
        self.session.verify = tls_verify
        self.session.headers.update(headers)

    def _send_request(self, api_method, parameters={}, payload=None, http_method='GET'):
        """
        Used to send a REST request using the desired http_method (GET, PUT, POST, DELETE) to the
        specified base_url + api_method.  Any specified parameters and payload, where applicable,
        will be included.

        :param api_method: API method, such as "users" requested. Will be combined with base_url
        :param parameters: (optional) Any URL parameters, such as {'filter': 'blah'}
        :param payload: (optional) A body/payload to be included in the request.
        :param http_method: (optional) The type of method (GET, PUT, POST, DELETE)

        :type api_method: String
        :type parameters: Dict
        :type payload: String (usually JSON-encoded)
        :type http_method: String (GET, PUT, POST, DELETE)

        :returns: returns a dictionary indicating success with the raw response or
                  a message indicating the error encountered.
        :returns: return a dictionary with the following keys:
           'success'  :rtype:Bool:   Whether the response received from the server is deemed a success
           'message'  :rtype:String: A message indicating success or details of any exception encountered
           'response' :rtype:requests.models.Response:   The raw response from the Python requests library
        :rtype: Dict
        """
        result = {'success': False, 'message': '', 'response': ''}
        # Set the URL using the parameters of the object and the api_method requested
        # in a format such as: https//host:port/api/v1/api_method
        url = "https://{}:{}{}/{}".format(self.host, self.port, self.base_url, api_method)

        # Send the request and handle RequestException that may occur
        try:
            if http_method in ['GET', 'POST', 'PUT', 'DELETE']:
                if http_method == 'GET':
                    raw_response = self.session.get(url, params=parameters)
                elif http_method == 'POST':
                    raw_response = self.session.post(url, data=payload, params=parameters)
                elif http_method == 'PUT':
                    raw_response = self.session.put(url, data=payload, params=parameters)
                elif http_method == 'DELETE':
                    raw_response = self.session.delete(url)

                result = {
                    'success': True,
                    'response': raw_response,
                    'message': 'Successful {} request to: {}'.format(http_method, url)
                }

        except RequestException as e:
            result = {
                'success': False,
                'message': 'RequestException {} request to: {} :: {}'.format(http_method, url, e)}
        return result

    def _check_response(self, raw_response):
        """
        Evaluates a response status.  If it has a non-2XX value, then set the 'success' result
        to false and place the exception in the 'message'

        :param raw_response: The raw response from a _send_request.

        :returns: Returns a the same dictionary passed to it, with the 'success' and 'message'
                  keys modified, if needed.
        :rtype:  Dict
        """
        try:
            # Raise HTTPError error for non-2XX responses
            raw_response['response'].raise_for_status()
        except HTTPError as e:
            raw_response['success'] = False
            raw_response['message'] = 'HTTPError Exception: {}'.format(e)
        return raw_response