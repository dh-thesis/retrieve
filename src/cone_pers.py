from tqdm import tqdm
from pybman import utils
from pybman.rest import PersonConeController

from .utils_paths import BASE_DIR

PURE_DIR = BASE_DIR + 'pure/'

#######################################
### RETRIEVE LIST OF PERSONS (CoNE) ###
#######################################

pers_controller = PersonConeController()
pers = pers_controller.get_entities()

utils.write_json(PURE_DIR + "pers/all.json", pers)

##############################
### EXTRACT UNIQUE PERSONS ###
##############################

pers_unique = {}

for p in pers:
    idx = p['id'].split("/")[-1:][0]
    if idx in pers_unique:
        pers_unique[idx].append(p['value'])
    else:
        pers_unique[idx] = [p['value']]

utils.write_json(PURE_DIR + "pers/unique.json", pers_unique)

###############################################
### RETRIEVE INDIVIDUAL ENTRIES FOR PERSONS ###
###############################################

pers_ids = list(pers_unique.keys())
pers_ids.sort()

# request data
pers_data = {}
for idx in tqdm(pers_ids):
    pers_details = pers_controller.get_entity(idx)
    pers_data[idx] = pers_details

utils.write_json(PURE_DIR + "pers/collection.json", pers_data)
