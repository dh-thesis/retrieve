from tqdm import tqdm
from pybman import utils
from pybman.rest import JournalConeController

from .utils_paths import BASE_DIR

PURE_DIR = BASE_DIR + 'pure/'

#################################
### RETRIEVE LIST OF JOURNALS ###
#################################

jour_controller = JournalConeController()
journals = jour_controller.get_entities()

utils.write_json(PURE_DIR + 'jour/all.json', journals)

################################################
### RETRIEVE INDIVIDUAL ENTRIES FOR JOURNALS ###
################################################

jour_meta = {}

for jour in journals:
    idx = jour['id'].split("/")[-1]
    jour_meta[idx] = jour['value']

jour_ids = list(jour_meta.keys())

# request data
jour_data = {}
for idx in tqdm(jour_ids):
    jour_details = jour_controller.get_entity(idx)
    jour_data[idx] = jour_details

utils.write_json(PURE_DIR + 'jour/collection.json', jour_data)
