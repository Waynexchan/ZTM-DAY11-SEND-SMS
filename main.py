from twilio.rest import Client

account_sid = 'sid'
auth_token = 'token'
client = Client(account_sid, auth_token)

message = client.messages.create(
                             from_='+132dasdadad',
                             body='hello try it now',
                             to='+852sdadsada'
)

print(message.sid)