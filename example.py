#!/usr/bin/env python

import repov

# Example usage.
print('Default: ' + repov.get_version())
print('%branch%: ' + repov.get_version('%branch%'))
print('%branch-any%: ' + repov.get_version('%branch-any%'))
print('%branch-all%: ' + repov.get_version('%branch-all%'))
print('%hash%: ' + repov.get_version('%hash%'))
print('%hash-full%: ' + repov.get_version('%hash-full%'))
print('%count%: ' + repov.get_version('%count%'))
print('%count-hex%: ' + repov.get_version('%count-hex%'))
print('%last-commit%: ' + repov.get_version('%last-commit%'))
print('get_raw(\'last-commit\'): ' + repr(repov.get_raw('last-commit')))
