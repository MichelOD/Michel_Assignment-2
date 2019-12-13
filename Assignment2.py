# -*- coding: utf-8 -*-
"""
Created on Fri Dec 06 09:53:41 2019

@author: nv023673
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 

"""       IMPORTING THE FLUXES """

#urao_data_2015 = np.genfromtxt("UoR_2015_September_Data.csv",\
# delimiter=',',skip_header=2, filling_values=np.nan)[:,1:6]
#urao_data_2015 = urao_data_2015 [~np.isnan(urao_data_2015).any(axis=1)]

#urao_data_2016_July = np.genfromtxt("UoR_2016_July_Data.csv",\
# delimiter=',',skip_header=2, filling_values=np.nan)[:,1:6]
#urao_data_2016_July = urao_data_2016_July [~np.isnan(urao_data_2016_July).any(axis=1)]
#duration=urao_data[:,0]
""" Ameriflux Site: US-Mpj      IMPORTING THE FLUXES """
ameri_data_US_Mpj = np.genfromtxt("AMF_US-Mpj_BASE_HH_12-5.csv",\
 delimiter=',',skip_header=3, filling_values=np.nan)[:,1:24]
ameri_data_US_Mpj = ameri_data_US_Mpj [~np.isnan(ameri_data_US_Mpj).any(axis=1)]


#co2_flux=urao_data_2015[:,1]
#co2_flux_2016_July=urao_data_2016_July[:,1]

co2_flux_US_Mpj=ameri_data_US_Mpj[:,5]


plt.plot(figsize=(15,5))
plt.plot(co2_flux_US_Mpj)
#plt.xlim(len(co2_flux_US_Mpj[:,5]))
#plt.xticks((0,720, 1440, 2160,2880,3600), ['01 Dec','15 Dec' ,'01 Jan', '15 Jan', '01 Feb', '15 Feb'], rotation=20)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Co2 Flux ($W m^{-2}$)", fontsize=14)
plt.title(' Carbon Dioxide Flux at US-Mpj site ', fontsize=15)
#plt.axis([2014, 2016, -10000, 2000])
plt.show()

