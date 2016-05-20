import socket
import urllib.request
from urllib.error import URLError, HTTPError

import json
import time
import jwt
import datetime

class PlaylyfeException(Exception):

  def __init__(self, error, error_description):
    self.name = error
    self.message = error_description
    self.msg = error_description

  def __str__(self):
    return "%s %s" %(self.name, self.message)

class Playlyfe:

  def __init__(self, secret, endpoint="http://localhost:3212/graphql", debug=False):
    self.secret = secret
    self.endpoint = endpoint
    self.debug = debug

  def create_jwt(self, user_id='', expires = 3600):
    token = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expires)}, self.secret, algorithm='HS256')
    token = user_id + ':' + token.decode('utf-8')
    return token

  def graphql(self, token='', query='', variables=None):
    if self.debug:
      print("Token:", token)
      print("Query:", query)
    data = {'query': query, 'variables': variables}
    reqBody = json.dumps(data).encode('utf-8')
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    req = urllib.request.Request(self.endpoint+"?"+"access_token="+token, reqBody, headers)
    try:
      response = urllib.request.urlopen(req)
      response_text = response.read().decode("utf-8")
      json_data = json.loads(response_text)
      if 'errors' in json_data:
        err = json_data['errors'][0]
        if self.debug:
          print("Error:", err)
        if 'code' in err:
          raise PlaylyfeException(err['code'], err['message'])
        else:
          raise PlaylyfeException('graphql_syntax_err', err['message'])
      if self.debug:
        print("Result:", json_data)
      response.close()
      return json_data
    except HTTPError as e:
      err = json.loads(e.read().decode("utf-8"))
      if self.debug:
        print("Error:", err)
      e.close()
      if 'error' in err:
        raise PlaylyfeException(err['error'], err['error_description'])
      else:
        raise e