from pybman import utils
from pybman.rest import OrgUnitRestController

from .utils_paths import BASE_DIR

PURE_DIR = BASE_DIR + 'pure/'

###########################################
### RETRIEVE ORGANIZATIONAL UNITS (OUS) ###
###########################################

ou_controller = OrgUnitRestController()
ous = ou_controller.get_all()

utils.write_json(PURE_DIR + "ous/all.json", ous)
