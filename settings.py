from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0)
import random
apps = ['Amazon_relief_19']
random.shuffle(apps)
app_seq = ['Welcome']
for app in apps:
    app_seq.append(app)
app_seq.append('Demographic')
app_seq.append('Debrief')
SESSION_CONFIGS = [dict(name='Random_Order_1', num_demo_participants=2, app_sequence=app_seq)]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
ROOMS = [dict(name='my_room', display_name='my_room'), dict(name='dyad', display_name='dyad')]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']