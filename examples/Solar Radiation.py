
# coding: utf-8

# # Solar Radiation Examples for pveducation.org
# mainly uses the sun module

# Do the normal imports

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import photovoltaic as pv


# Determine the emission at a single wavelength

# In[3]:


wavelength = 600  # (nm)
print(pv.sun.blackbody_spectrum(wavelength))  # just a single variable, using default T = 6000 K
print('Blackbody radiation is {:.2e} at {:.2f} nm using the default temperature of 6000 K'.format(
    pv.sun.blackbody_spectrum(wavelength), wavelength))  # same but nicely formatted.


# plot the blackbody radiation as a function of wavelength

# In[4]:


wavelength = np.linspace(200, 3000, 200)  # 200 eo 3000 nm, 200 points
temperature = 4500  # (K)

plt.figure('blackbody_plot')
plt.plot(wavelength, pv.sun.blackbody_spectrum(wavelength, temperature))
plt.xlabel('wavelength (nm)')  # add axis labels and plot title
plt.ylabel('spectral irradiance (W m$^{-2}$ nm$^{-1}$)')  # tex formating works in Matplotlib but not for all strings.
plt.title('Blackbody Radiation at ' + str(temperature) + ' K')
plt.savefig('blackbody_plot.png')
plt.show()

