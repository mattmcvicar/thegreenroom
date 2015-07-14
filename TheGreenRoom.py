# Imports --------------------------------------
print ''
print ' importing...'
from instagram.client import InstagramAPI


# Parameters -----------------------------------
CLIENT_ID =	"58e08193e2f147b7a3f509964870894c"
CLIENT_SECRET = "14a8f2af907549bc88316c829c59c073"
CODE = "359d790f939d4c1a8bdb0ae1e09ea7d7"
ACCESS_TOKEN = "2024656005.58e0819.808bbdd81e06460d907844d812502da6"

TAG = "green"
# Main ------------------------------------------
api = InstagramAPI(access_token=ACCESS_TOKEN, client_secret=CLIENT_SECRET)

print '  getting pictures tagged with ', TAG
media_ids,next = api.tag_recent_media(tag_name=TAG, count=80)

for m in media_ids:
	url = m.get_standard_resolution_url()
	print url