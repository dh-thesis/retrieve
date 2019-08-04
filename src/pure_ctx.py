from pybman import utils
from pybman.rest import ContextRestController

from .utils_paths import BASE_DIR

PURE_DIR = BASE_DIR + 'pure/'

################################
### RETRIEVE CONTEXTS (CTXs) ###
################################

ctx_controller = ContextRestController()
ctxs = ctx_controller.get_all()

utils.write_json(PURE_DIR + "ctx/all.json", ctxs)
