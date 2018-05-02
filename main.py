import pprint
from aws import cf


if __name__ == '__main__':
    pprint.pprint(cf.delete_stacks_in_state('ROLLBACK_COMPLETE'))
