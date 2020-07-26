from twilio.rest import Client
# sid and auth
account_sid = 'AC4649b5dcef1dc7bf9076a178167e8caa'
auth_token = 'a465f67bdba171291e3feee797511b04'

client = Client(account_sid,auth_token)

my_contact = 'whatsapp:+14155238886'

# contact list
close = 'whatsapp:+62895401144676'



contact_list = [str(close)]







