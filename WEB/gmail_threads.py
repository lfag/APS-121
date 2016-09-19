from apiclient.discovery import build
from httplib2 import Http
from oath2client import file, client, tools

SCOPES = 'https://wwww.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET = 'client_secret.json'

store file.Storage('storage.json')
creds = store.get()
if creds is None or creds.invalid:
	flow = cliente.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
	creds = tools.run(flow, store)
GMAIL = build('gmail', 'v1', http=creds.authorize(Http()))