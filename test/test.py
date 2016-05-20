import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from playlyfe import Playlyfe, PlaylyfeException


def test_auth():
  query = '''
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
  '''
  try:
    pl = Playlyfe(
      secret = "wrong_secret",
      debug = True,
    )
    token = pl.create_jwt(user_id="wrong_user_id")
    result = pl.graphql(token, query)
  except PlaylyfeException as e:
    assert "user_not_found" in e.name
    assert "A user with id 'wrong_user_id' does not exist" in e.message

  try:
    pl = Playlyfe(
      secret = "wrong_secret",
      debug = True,
    )
    token = pl.create_jwt(user_id="db55271e-1e5e-11e6-8369-201a06e4e14a")
    result = pl.graphql(token, query)
  except PlaylyfeException as e:
    assert "forbidden" in e.name
    assert "signature is invalid" in e.message

  pl = Playlyfe(
    secret = "OThjMTE5M2QtZTViYS00YzJjLTg5ZDctNzg3ODg2YzE0Mjcx",
    debug = True,
  )
  token = pl.create_jwt(user_id="db55271e-1e5e-11e6-8369-201a06e4e14a")
  result = pl.graphql(token, query)
  assert len(result["data"]["root"]["games"]["edges"]) == 0

  try:
    result = pl.graphql(token, '''
      query Game {
        node(id: "{\\"id\\":\\"test\\",\\"type\\":\\"Game\\"}") {
          ... on Game {
            id
            name
          }
        }
      }
    ''')
  except PlaylyfeException as e:
    assert "game_not_found" in e.name
    assert "A game with id 'test' does not exist" in e.message

  try:
    result = pl.graphql(token, '''
      query Game($input:PLGlobalID!) {
        node(id: $input) {
          ... on Game {
            id
            name
          }
        }
      }
    ''', {'input': '{\"id\":\"test\",\"type\":\"Game\"}'})
  except PlaylyfeException as e:
    assert "game_not_found" in e.name
    assert "A game with id 'test' does not exist" in e.message

test_auth()
