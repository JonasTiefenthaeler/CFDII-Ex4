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

plt.figure(figsize=(7,5))
plt.plot(turb_freq,y_plus, label ="turbulence frequency")
plt.plot(tke,y_plus, label="turbulent kinetic energy")
plt.plot( dissip,y_plus, label = "dissipation rate")
plt.ylabel("wall distance")
plt.title("Task 4.3 (1.)")
#plt.ylim(-1,6)
plt.xlim(-1,6)
#plt.xlabel("turbulent kinetic energy")
plt.legend()


#TASK 2

eq_nu_t = uv/du_dy

C_mu = 0.09
eddy_visc = C_mu *(np.pow(tke,2)/dissip)

plt.figure(figsize=(7,5))
plt.plot(eq_nu_t, y_plus,label = "equivalent eddy viscosity")
plt.plot(eddy_visc,y_plus,  label = "eddy viscosity")
plt.xlabel("viscosity")
plt.ylabel("wall distance")
plt.title("Task 4.3 (2.)")
plt.legend()


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
plt.plot(equi,y_plus,  label="reynolds stress tensor with equivalent eddy viscosity")
plt.plot(eddy, y_plus, label="reynolds stress tensor with eddy viscosity")
plt.plot(R_ij_dev, y_plus, label="R_ij^dev")
plt.title("Task 4.3 (4.)")
plt.ylabel("Wall distance")
plt.xlabel("Stress")
plt.legend()
plt.show() 