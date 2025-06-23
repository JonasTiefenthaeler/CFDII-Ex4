import numpy as np
import matplotlib.pyplot as plt

filename = "Exercise4_TKE_budegts_simson_ReTau2000.txt"

data = np.loadtxt(filename, comments = '%')

y_h         =   data[:,0]
y_plus      =   data[:,1]
tke         =   data[:,2]
uv          =   data[:,3]
du_dy       =   data[:,4]
dissip      =   data[:,5]
prod        =   data[:,6]
press_trans =   data[:,7]
turb_trans  =   data[:,8]
visc_diff   =   data[:,9]
conv        =   data[:,10]


#TASK 1
turb_freq = dissip/tke

plt.figure(figsize=(5,5))
plt.plot(y_plus, turb_freq, label ="turbulence frequence")
plt.plot(y_plus, tke, label="turbulent kinetic energy")
plt.plot(y_plus, dissip, label = "dissipation rate")
plt.ylabel("wall distance")
plt.ylim(-1,6)
#plt.xlim(-0.5,1)
#plt.xlabel("turbulent kinetic energy")
plt.legend()


#TASK 2

eq_nu_t = uv/du_dy

C_mu = 0.09
eddy_visc = C_mu *(np.pow(tke,2)/dissip)

plt.figure(figsize=(5,5))
plt.plot(y_plus,eq_nu_t, label = "equivalent eddy viscosity")
plt.plot(y_plus, eddy_visc, label = "eddy viscosity")

plt.legend()

"""
#TASK 3


#TASK 4

R_ij = uv
R_kk = 2*tke
delta_ij = 1
R_ij_dev = R_ij #- ((R_kk*delta_ij)/3)

S_ij = du_dy/2

equi = -2*eq_nu_t*S_ij
eddy = -2*eddy_visc*S_ij

plt.figure(figsize=(7,5))
plt.plot(y_plus, equi, label="reynolds stress tensor with equivalent eddy viscosity")
plt.plot(y_plus, eddy, label="reynolds stress tensor with eddy viscosity")
plt.plot(y_plus, R_ij_dev, label="R_ij^dev")
plt.legend()
"""
plt.show() 