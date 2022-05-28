# Import Yamale and make a schema object
from yamale import YamaleError
import yamale
schema = yamale.make_schema(r'C:\Users\User\OneDrive\Documents\HPE\Task 1\schema.yml', parser='ruamel')

# Create a Data object
data = yamale.make_data(r'C:\Users\User\OneDrive\Documents\HPE\Task 1\tools-main\tools-main\config\fam_memoryserver_config.yaml', parser='ruamel')

#To validate
try:
    yamale.validate(schema, data)
    print('Validation success! 👍')
except ValueError as e:
    print('Validation failed!\n%s' % str(e))