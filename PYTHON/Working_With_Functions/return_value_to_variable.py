def trip_planner_welcome(name):
  print(f'Welcome to tripplanner v1.0 {name}')
trip_planner_welcome('Eitan')

def estimated_time(raw_time):
  hours=int(raw_time)
  minutes=int((raw_time-hours)*60)
  return f'{hours}:{minutes:02d}'

# Saving the return value as a global variable so it can be used efficiently 
# in future functions.
estimate=estimated_time(6.0833) 

def destination_setup(origin, destination, estimated_time, mode_of_transport='Car'):
  print('''Your trip starts off in {}
  And you are traveling to {}
  You will be traveling by {}
  It will take approximately {} hours'''.format(origin, destination, mode_of_transport,estimated_time))

destination_setup('Jamaica','Algeria', estimate, 'Plane')