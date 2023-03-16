from pprint import pprint
import project
from project import base, utils

print(project.logger)
print(base.logger, utils.logger)
print(base.logger.handlers)
pprint(base.logger.parent.handlers)
base.func1()
utils.func2()