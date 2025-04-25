# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# converts damages from string format to numeric USD format. returns list with numerical values, 'Damages not recorded' remains unchanged
def update_damages(damages):
  conversion = {"M": 1000000, "B": 1000000000}
  updated_damages = []
  for item in damages:
    if item == 'Damages not recorded':
      updated_damages.append(item)
    else:
      number = float(item[:-1])
      suffix = item[-1]
      converted = number * conversion[suffix]
      updated_damages.append(converted)
  return updated_damages
updated_damages = update_damages(damages)
print(updated_damages)
# creates dictionary of hurricanes using provided data lists, each hurricane name is a key, and value is dictionary of attributes (month, year, wind speed, affected areas, damage, deaths)
def define_hurricane(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  hurricanes = {}
  for i in range(len(names)):
    hurricane_info = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': updated_damages[i], 'Deaths': deaths[i]}
    hurricanes[names[i]] = hurricane_info
  return hurricanes
total = define_hurricane(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(total['Bahamas'])
# groups hurricanes based on year they happened, returns dictionary where each key is a year and each value is a list of hurricanes that occured within the year (does not include years with no hurricanes)
def hurricane_years(hurricanes):
  hurricanes_by_year = {}
  for hurricane in hurricanes.values():
    year = hurricane['Year']
    if year not in hurricanes_by_year:
      hurricanes_by_year[year] = []
    hurricanes_by_year[year].append(hurricane)
  return hurricanes_by_year
hurricanes_by_year = hurricane_years(total)
print(hurricanes_by_year[1932])
# counts how many times each area has been affected by hurricanes and returns a dictionary with area names as keys and frequency of occurences as values
def count_affected_areas(hurricanes):
  area_affected_num = {}
  for hurricane in hurricanes.values():
    areas = hurricane['Areas Affected']
    for area in areas:
      if area in area_affected_num:
        area_affected_num[area] += 1
      else:
        area_affected_num[area] = 1
  return area_affected_num
area_affected_num = (count_affected_areas(total))
# finds area that was most frequently attacked and returns name of the area + number of times it was hit
def most_affected_areas(areas_affected):
  most_affected_area = None
  highest_count = 0
  for area, count in areas_affected.items():
    if count > highest_count:
      highest_count = count
      most_affected_area = area
  return most_affected_area, highest_count
print(most_affected_areas(area_affected_num))
# identifies the hurricane that caused the highest number of deaths, returns name of hurricane and number of deaths
def most_devastating_hurricane(hurricane):
  most_devastating = None
  highest_deaths = 0
  for hurricane, data in hurricane.items():
    deaths = data['Deaths']
    if deaths > highest_deaths:
      highest_deaths = deaths
      most_devastating = hurricane
  return most_devastating, highest_deaths
print(most_devastating_hurricane(total))
# categorises hurricanes into mortality rating scale based on death count, returns dictionary where keys are ratings (out of 5) and values are lists of hurricanes in each category
def mortality_rating(hurricane):
  mortality_scale = {0: 0, 1: 100,  2: 500, 3: 1000, 4: 10000}
  mortality_ratings = {}
  for name, data in hurricane.items():
    deaths = data['Deaths']
    for key, value in mortality_scale.items():
      if deaths <= value:
        if key not in mortality_ratings:
          mortality_ratings[key] = []
        mortality_ratings[key].append(data)
        break
  return mortality_ratings
print(mortality_rating(total))
# finds hurricane that caused the most financial damage, skips unrecorded damage. returns name and total damage of the most damaging hurricane
def most_damage(hurricane):
  most_damaging = None
  damage_caused = 0
  for name, data in hurricane.items():
    damage = data['Damage']
    if damage != 'Damages not recorded':
      if damage > damage_caused:
        damage_caused = damage
        most_damaging = name
  return most_damaging, damage_caused
print(most_damage(total))
# categorises hurricanes into a damage rating scale based on the cost of damages. returns dictionary with keys as damage ratings and values as lists of hurricanes that fall into each rating
def damage_rating(hurricane):
  damage_scale = {0: 0,1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
  damage_ratings = {}
  for name, data in hurricane.items():
    damage = data['Damage']
    for key, value in damage_scale.items():
      if damage != 'Damages not recorded' and damage <= value:
        if key not in damage_ratings:
          damage_ratings[key] = []
        damage_ratings[key].append(data)
        break
  return damage_ratings
print(damage_rating(total))