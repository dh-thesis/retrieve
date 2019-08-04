from tqdm import tqdm
from pybman import utils
from pybman.rest import LanguageConeController

from .utils_paths import BASE_DIR

PURE_DIR = BASE_DIR + 'pure/'

#################################################
### RETRIEVE LIST OF LANGUAGES (CoNE/ISO 639) ###
#################################################

lang_controller = LanguageConeController()
langs = lang_controller.get_entities()

utils.write_json(PURE_DIR + "lang/all.json", langs)

#################################################
### RETRIEVE INDIVIDUAL ENTRIES FOR LANGUAGES ###
#################################################

lang_meta = {}

for lang in langs:
    idx = lang['id'].split("/")[-1]
    lang_meta[idx] = lang['value']

lang_ids = list(lang_meta.keys())

# request data
lang_data = {}
for idx in tqdm(lang_ids):
    lang_details = lang_controller.get_entity(idx)
    lang_data[idx] = lang_details

utils.write_json(PURE_DIR + "lang/collection.json", lang_data)
