train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


def f_to_c(f_temp):
  c_temp = (f_temp - 32) * (5/9)
  return c_temp

def c_to_f(c_temp):
  f_temp= (c_temp * 9/5) + 32
  return f_temp

def get_force(mass, acceleration):
    if mass < 0 or acceleration < 0:
        raise ValueError('Mass and acceleration must be positive')
    return mass * acceleration

def get_energy(mass, c = 3 * 10 ** 8):
  return mass * c ** 2

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance


train_force=get_force(train_mass, train_acceleration)
print(f'The GE train supplies {train_force} Newtons of force')


bomb_energy= get_energy(bomb_mass)
print(f'A 1kg bomb supplies {bomb_energy} Joules')

train_work= get_work(train_mass,train_acceleration, train_distance)
print(f'The GE train does {train_work} Joules of work over {train_distance} Meters')

