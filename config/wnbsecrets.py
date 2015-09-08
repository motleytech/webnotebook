# WARNING : make sure to change the password hash on your system.
# DO NOT use the default value on production systems.
#
# This file, the 'defaultPassword' and its hash are all available
# publicly on github.
#
#
# Use the following commands to generate a new password hash
#
# from IPython.lib import passwd
# passwd()
#
# After setting a new password hash, restart the notebook server process
#
# This is the hash for 'defaultPassword', unless modified.

passwordHash = u'sha1:c758adf8ce8e:f5f7ef28d3c11b69f5d2802ca50188c79667bf1b'

# Use the following command to generate a new cookie
# makepasswd --minchars=55 --maxchars=60 --count=20
cookie_secret = u'uAtsCyGSWMhwcrGgzDeM2mj8dbEWTMoPxjqiCzcdP1sDE2MWfiKci0w'
