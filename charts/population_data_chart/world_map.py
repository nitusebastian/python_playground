import pygal
import json

from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country"""
    for code, name in COUNTRIES.items():
        if name==country_name:
            return code
    #If the country wasn't found, return None
    return None

pop_data = []

# Load the data into a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data
cc_populations = {}

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population

# Group the countries into 3 population levels
cc_pops_1, cc_pops_2, cc_pops3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops3[cc] = pop


wm = pygal.maps.world.World()
wm.title = 'World Population in 2010, by Country'

wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops3)
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

#wm.render_to_file('americas.svg')
#wm.render_to_file('na_populations.svg')
wm.render_to_file('world_population.svg')
