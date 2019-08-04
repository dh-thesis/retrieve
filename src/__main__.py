import time

print("start retrieval!")

start_time = time.time()

# ///////////////// #
# /// JOURNALS /// #
# /////////////// #

from .cone_jour import *

# ////////////////// #
# /// LANGUAGES /// #
# //////////////// #

from .cone_lang import *

# //////////////// #
# /// PERSONS /// #
# ////////////// #

from .cone_pers import *

# ///////////////// #
# /// CONTEXTS /// #
# /////////////// #

from .pure_ctx import *

# ////////////////////// #
# /// ORGANIZATIONS /// #
# //////////////////// #

from .pure_ous import *

# ///////////////////// #
# /// PUBLICATIONS /// #
# /////////////////// #

from .pure_pub import *

# /////////////////// #
# /// INSTITUTES /// #
# ///////////////// #

from .crawl_mpis_eng import *
from .crawl_mpis_deu import *

from .map_mpis_eng import *
from .map_mpis_deu import *

from .map_mpis import *
from .map_post import *

# ///////////// #

print("finished retrieval after %s sec!" % round(time.time() - start_time, 2))
