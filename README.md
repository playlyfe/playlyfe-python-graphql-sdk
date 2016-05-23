![Playlyfe Python GraphQL SDK](https://dev.playlyfe.com/images/assets/pl-python-sdk.png "Playlyfe Python GraphQL SDK")

Playlyfe Python GraphQL SDK [![PyPI version](https://badge.fury.io/py/playlyfe-graphql.svg)](http://badge.fury.io/py/playlyfe-graphql)
=================
This is the official Playlyfe Python GraphQL API V3 SDK for the Playlyfe V3 API.
It uses the JWT Auth Flow.

Requires
--------
Python 3.5.1

Install
----------
```python
pip install playlyfe_grapqhl
```
or if you are using django or flask
Just add it to your requirements.txt file
```python
playlyfe_grapqhl==0.1.0
```
and do a pip install -r requirements.txt

Using
-----
A typical flask app with a single route would look something like this
```python
@app.route("/root")
def client():
  pl = Playlyfe(
    secret = "Your user secret",
    debug = True,
  )
  token = pl.create_jwt(user_id="your user id")
  root = pl.graphql(token, '''
  query K {
    root {
      games {
        edges {
          node {
            id
          }
        }
      }
    }
  }
  ''')
  return json.dumps(root).encode('utf-8')
```

# Documentation
You can initiate a client by giving the secret params
```python
Playlyfe(
   secret # the secret of your user
   endPoint = "http://localhost:3212/graphql" # The endPoint of the api server
   debug = False # whether you would like to see debug logs when developing
)
```

**graphql**
```python
graphql(
    token = '' # the jwt token that you have generated
    query =  '' # the query you would like to make
    variables = {} # The variables you would like to send
)
```

**create_jwt**
```python
create_jwt(
  user_id # the id of the user who you want to make requests with
  expires = 3600 # the expiry time of the token in seconds
)
```

**Errors**

A ```PlaylyfeException``` is thrown whenever an error is returned from our servers in each call.
The Error contains a name and message field which can be used to determine the type of error that occurred.

License
=======
Playlyfe Python GraphQL SDK v0.1.0

http://dev.playlyfe.com/

Copyright(c) 2015-2016, Playlyfe IT Solutions Pvt. Ltd, support@playlyfe.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Contributing
============
```python
pip install twine wheel
python setup.py bdist_wheel
# if this is a new project then you need to do this twine register dist/*
twine upload dist/*
```
