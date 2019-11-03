"""Prerequesites"""

import pandas as pd
import matplotlib.pyplot as plt
import os
class Tire:
    """ In der Klasse Tire werden alle Informationen zu einem Reifen gespeichert. """

    def __init__(self,size,data,pressure_keys):
        self.size=size
        self.data=data
        self.pressure_keys=pressure_keys
        self.sortedLonData = {pressure_keys[0]:[]}
        self.bool_index=[]

    def sortLonData(self, ia_keys, fz_keys,sa_keys, iaLowerBorder, iaUpperBorder, fzLowerBorder, fzUpperBorder, slipAngleLowerBorder, slipAngleUpperBorder): # Sortiert die Daten nach "Situationen".
        z = 0
        for i in range(len(self.pressure_keys)):
            #self.sortedLonData[pressure_keys[i]]=pd.DataFrame()
            df_new=[]
            for sa_index in range(len(sa_keys)):
                sa = 0
                sa = (self.data[self.pressure_keys[i]]["SA"] < slipAngleUpperBorder[sa_index]) & (self.data[self.pressure_keys[i]]["SA"] > slipAngleLowerBorder[sa_index])
                for fz_index in range(len(fz_keys)):
                    fz = 0
                    fz = (self.data[self.pressure_keys[i]]["FZ"] < fzUpperBorder[fz_index]) & (self.data[self.pressure_keys[i]]["SA"] >fzLowerBorder[fz_index])
                    for ia_index in range(len(ia_keys)):
                        ia = 0
                        ia = (self.data[self.pressure_keys[i]]["IA"] < iaUpperBorder[ia_index]) & (self.data[self.pressure_keys[i]]["SA"] > iaLowerBorder[ia_index])
                        bool_index=[]

                        for m,n,b in zip(sa,fz,ia):
                            if (m==n) & (m==b) & (b==n):
                                bool_index.append(True)
                            else:
                                bool_index.append(False)

                        #print(bool_index)
                        #bool_index = (sa==fz) & (sa == ia) & (ia == fz) & (sa == True) & (fz == True) & (ia == True)
                        bool_series=pd.Series(bool_index, name='bool')
                        df_loop = pd.DataFrame()
                        df_loop = pd.DataFrame(self.data[pressure_keys[i]][bool_series])
                        
                        #for index_index in range(len(bool_index)):
                        #    if bool_index[index_index]:
                        #        df_loop.append(self.data[pressure_keys[i]].loc[index_index])

                        df_new.append(df_loop)
                                #df_new.append(pd.DataFrame(self.data[pressure_keys[i]].iloc[index_index]))
                        #df_new.append(pd.DataFrame(self.data[pressure_keys[i]][bool_index]))
                        #self.bool_index.append(bool_index)
                        #z=z+1

            df_finish = pd.DataFrame()
            df_finish = pd.concat(df_new, keys=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37'])
            self.sortedLonData[pressure_keys[i]] = df_finish

    def plotLonData(self, ia_keys):
        z = list(self.sortedLonData["10PSI"].index.get_level_values(0))
        z = list(dict.fromkeys(z))
        plt.figure(1)
        for i in range(len(self.pressure_keys)):
            plt.plot(self.sortedLonData[self.pressure_keys[i]].loc['0']['SL'],self.sortedLonData[self.pressure_keys[i]].loc['0']['FX'],label=self.pressure_keys[i])

        plt.xlabel('Slip ratio [-]')
        plt.ylabel('Fx [N]')
        plt.title('Fx over slip ratio at -1557N normal force and 0° inclination angle')
        plt.legend()
        plt.show()
        plt.figure(2)
        for j in range(len(ia_keys)):
            plt.plot(self.sortedLonData['10PSI'].loc[z[j]]['SL'],self.sortedLonData['10PSI'].loc[z[j]]['FX'],label=ia_keys[j])
        
        plt.xlabel('Slip ratio [-]')
        plt.ylabel('Fx [N]')
        plt.title('Fx over slip ratio for different inclination angles at 10 psi and -1557 N normal force')
        plt.legend()
        plt.show()

   



"""Data import"""
#Import boundary values for sorting
df = pd.read_table("Grenzen.txt",header=None)
keys = df[0].tolist()
lowerBorders = df[1].tolist()
upperBorders = df[2].tolist()
key_dict = {"ia_keys": keys[0:3], "fz_keys": keys[3:7],"sa_keys":keys[7:]}
lowerBorder_dict = {"ia_lBorder":lowerBorders[0:3],"fz_lBorder":lowerBorders[3:7], "sa_lBorder":lowerBorders[7:]}
upperBorder_dict = {"ia_uBorder": upperBorders[0:3], "fz_uBorder": upperBorders[3:7], "sa_uBorder": upperBorders[7:]}

#Import Braking files
files_braking = os.listdir("Data\Braking")
files_braking = [('Data\\Braking\\' + i ) for i in files_braking]

#Import Cornering Files


#Import pressure levels
pressure_keys_df = pd.read_table("Druck.txt",header=None)
pressure_keys = pressure_keys_df[0].tolist()
data = {pressure_keys[0]: 0}

#Import raw data
for i in range(len(files_braking)):
      data[pressure_keys[i]] = pd.read_table(files_braking[i],header=[1],skiprows=[2])

#Create new object of class Tire and use the object function to sort data in "situations"
hoosier13=Tire(13,data,pressure_keys)
hoosier13.sortLonData(key_dict["ia_keys"],key_dict["fz_keys"],key_dict["sa_keys"], lowerBorder_dict["ia_lBorder"], upperBorder_dict["ia_uBorder"], lowerBorder_dict["fz_lBorder"], upperBorder_dict["fz_uBorder"], lowerBorder_dict["sa_lBorder"], upperBorder_dict["sa_uBorder"] )
#hoosier13.sortLatData(key_dict["ia_keys"],key_dict["fz_keys"],key_dict["sa_keys"], lowerBorder_dict["ia_lBorder"], upperBorder_dict["ia_uBorder"], lowerBorder_dict["fz_lBorder"], upperBorder_dict["fz_uBorder"], lowerBorder_dict["sa_lBorder"], upperBorder_dict["sa_uBorder"] )


#Plot sorted data
#hoosier13.plotLonData(key_dict["ia_keys"])
#hoosier13.plotLatData(key_dict["ia_keys"])

