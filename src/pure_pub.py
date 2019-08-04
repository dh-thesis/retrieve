from tqdm import tqdm

from pybman import utils
from pybman import Client
from pybman.rest import ContextRestController

from .utils_paths import BASE_DIR

PURE_DIR = BASE_DIR + 'pure/'
ITEMS_DIR = BASE_DIR + 'items/'

################################
### RETRIEVE RECORDS OF CTXs ###
################################

ctxs = utils.read_json(PURE_DIR + "ctx/all.json")

ctx_meta = {}

for rec in ctxs['records']:
    objectId = rec['data']['objectId']
    ctx_meta[objectId] = rec['data']['name']

ctx_ids = list(ctx_meta.keys())
ctx_ids.sort()

client = Client()

for ctx_idx in tqdm(ctx_ids):
    print("retrieve data of context:", ctx_meta[ctx_idx])
    ctx_data = client.get_data(ctx_id=ctx_idx)
    utils.write_json(ITEMS_DIR +ctx_idx+".json",ctx_data.collection)
