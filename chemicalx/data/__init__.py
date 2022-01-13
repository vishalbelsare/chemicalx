from class_resolver import Resolver

from .contextfeatureset import *  # noqa:F401,F403
from .drugfeatureset import *  # noqa:F401,F403
from .labeledtriples import *  # noqa:F401,F403
from .datasetloader import *  # noqa:F401,F403
from .drugpairbatch import *  # noqa:F401,F403
from .batchgenerator import *  # noqa:F401,F403

dataset_resolver = Resolver.from_subclasses(base=DatasetLoader)
