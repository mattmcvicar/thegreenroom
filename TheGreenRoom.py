# Imports --------------------------------------
print ''
print '  importing...'
from instagram.client import InstagramAPI
import urllib2, urllib
import matplotlib.pylab as plt
from PIL import Image
import cStringIO

# Parameters -----------------------------------
CLIENT_ID =	"58e08193e2f147b7a3f509964870894c"
CLIENT_SECRET = "14a8f2af907549bc88316c829c59c073"
CODE = "359d790f939d4c1a8bdb0ae1e09ea7d7"
ACCESS_TOKEN = "2024656005.58e0819.808bbdd81e06460d907844d812502da6"

TAG = "green"

# functions -------------------------------------
def get_photos(tag):
	media_ids, next = api.tag_recent_media(tag_name=TAG, count=5)
	return media_ids

def read_photos(media_ids):
    images = []
    n_photos = len(media_ids)
    for iphoto, m in enumerate(media_ids):
        print "  reading photo " + str(iphoto + 1) + " of " + str(n_photos)
        #url = m.get_standard_resolution_url()
        url = m.get_low_resolution_url()
        images.append(Image.open(cStringIO.StringIO(urllib.urlopen(url).read())))

    return images


def display_photos(media_ids):
    for im in images:
        plt.figure()
        plt.imshow(im)
        plt.xticks([], [])
        plt.yticks([], [])
        plt.show()


# Main ------------------------------------------
api = InstagramAPI(access_token=ACCESS_TOKEN, client_secret=CLIENT_SECRET)

print "  getting pictures tagged with #" + TAG + "..."
photos = get_photos(TAG)
images = read_photos(photos)
display_photos(images)
print ''

