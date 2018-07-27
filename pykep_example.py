import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from pykep import epoch, epoch_from_string, planet, AU, MU_SUN, DEG2RAD
from pykep.planet import jpl_lp, keplerian
from pykep.orbit_plots import plot_planet

mpl.rcParams['legend.fontsize'] = 10

# asteroid @ Epoch 2014-Dec-09 (JD 2,457,000.5)
ast_time = epoch_from_string('2014-12-09 00:00:00.000') #epoch(6800,"mjd2000")
ast_orbel = (2.77 * AU, 0.075, 9.65 * DEG2RAD, 80.33 * DEG2RAD, 72.52 * DEG2RAD, 95.99 * DEG2RAD) # a,e,i,W,w,M (SI and RAD)
ast_mu = 6e10
ast_radius = 1e5
ast_name = 'asteroid'
asteroid = keplerian(ast_time, ast_orbel, MU_SUN, ast_mu, ast_radius, ast_radius*1.1, ast_name)
rA, vA = asteroid.eph(ast_time)

#earth
pl = jpl_lp('earth')
rE, vE = pl.eph(ast_time)

# plot
fig = plt.figure()
axis = fig.gca(projection='3d')
axis.scatter([0], [0], [0], color='y') #sun
plot_planet(asteroid, t0=ast_time, color=(1, 0.4, 0), legend=True, units=AU, ax=axis) #asteroid
plot_planet(pl, t0=ast_time, color=(0.8, 0.8, 1), legend=True, units=AU, ax=axis) #earth
plt.show()
