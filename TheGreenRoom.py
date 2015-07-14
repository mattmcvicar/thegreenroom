# Imports --------------------------------------
from instagram.client import InstagramAPI
import urllib2, urllib
import matplotlib.pylab as plt
from PIL import Image
import cStringIO
import numpy as np
import matplotlib.gridspec as gridspec
import sys

# Parameters -----------------------------------
CLIENT_ID =	"58e08193e2f147b7a3f509964870894c"
CLIENT_SECRET = "14a8f2af907549bc88316c829c59c073"
CODE = "359d790f939d4c1a8bdb0ae1e09ea7d7"
ACCESS_TOKEN = "2024656005.58e0819.808bbdd81e06460d907844d812502da6"

TAG = "sunset"
N = 16 # should be a square

# functions -------------------------------------
def get_photos(tag, n):
	media_ids, next = api.tag_recent_media(tag_name=TAG, count=n)
	return media_ids

def read_photos(media_ids):
    images = []
    n_photos = len(media_ids)
    for iphoto, m in enumerate(media_ids):
        print "  reading photo " + str(iphoto + 1) + " of " + str(n_photos)
        try:
            #url = m.get_standard_resolution_url()
            url = m.get_low_resolution_url()
            images.append(Image.open(cStringIO.StringIO(urllib.urlopen(url).read())))
        except:
            pass

    return images


def display_photos(media_ids, n):
    sqrt_n = int(np.sqrt(n))
    plt.figure(figsize=(8, 8))
    gs1 = gridspec.GridSpec(n, n)
    gs1.update(wspace=0.0, hspace=0.0)
    for iphoto, im in enumerate(media_ids):
        ax = plt.subplot(sqrt_n, sqrt_n, iphoto)
        plt.imshow(im)
        #plt.xticks([], [])
        #plt.yticks([], [])
        plt.axis('off')
        ax.set_aspect('equal')

    plt.subplots_adjust(wspace=0.01, hspace=0.01)
    plt.show()

def die_with_usage():

    print """
    TheGreenRoom.py
    ---------------

    usage:
    $ python TheGreenRoom.py tag n

    inputs:
      tag - tag to search instagram for
      n - number of photos to display in grid
    """
    exit()
# Main ------------------------------------------
if __name__ == "__main__":

    if len(sys.argv) != 3:
    	die_with_usage()

    api = InstagramAPI(access_token=ACCESS_TOKEN, client_secret=CLIENT_SECRET)
    print "  getting pictures tagged with #" + TAG + "..."
    
    TAG, N = sys.argv[1:]
    photos = get_photos(TAG, N)
    images = read_photos(photos)
    display_photos(images, N)
    print ''

