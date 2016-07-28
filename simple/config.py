from authomatic.providers import oauth2, oauth1

CONFIG = {
    
    'tw': { # Your internal provider name
        
        # Provider class
        'class_': oauth1.Twitter,
        
        # Twitter is an AuthorizationProvider so we need to set several other properties too:
        'consumer_key': 'i5kSIFav5k85d8nhORtaSZYhW',
        'consumer_secret': 'cH12dv61ujPZFuxKUA4L0NztjVoI7clslE6kueHZvy42C02B5A',
        'access_token' : '1362707197-6Eu0rmnlPHaj6cZMtbxUaW9SOIYOx571a4KdMg0',
        'access_secret' : 'fwClOx7brVjSyJYW4EBDWXM5i9t9ON6BPnU1CKL187J7f'
    }
}