"""Prerequesites"""
'Prerequesites'
import pandas as pd
import matplotlib.pyplot as plt
class Tire:
    """ In der Klasse Tire werden alle Informationen zu einem Reifen gespeichert. """

    def __init__(self,size,data,pressure_keys):
        self.size=size
        self.data=data
        self.pressure_keys=pressure_keys
        self.sortedLonData = {pressure_keys[0]:[]}
        self.index=[]

    def sortLonData(self, ia_keys, fz_keys,sa_keys, iaLowerBorder, iaUpperBorder, fzLowerBorder, fzUpperBorder, slipAngleLowerBorder, slipAngleUpperBorder): # Sortiert die Daten nach "Situationen".
        z = 0
        for i in range(len(self.pressure_keys)):
            #self.sortedLonData[pressure_keys[i]]=pd.DataFrame()
            df_new=[]

            for sa_index in range(len(sa_keys)):
                sa = (self.data[self.pressure_keys[i]]["SA"] < slipAngleUpperBorder[sa_index]) & (self.data[self.pressure_keys[i]]["SA"] > slipAngleLowerBorder[sa_index])
                for fz_index in range(len(fz_keys)):
                    fz = (self.data[self.pressure_keys[i]]["FZ"] < fzUpperBorder[fz_index]) & (self.data[self.pressure_keys[i]]["SA"] >fzLowerBorder[fz_index])
                    for ia_index in range(len(ia_keys)):
                        ia = (self.data[self.pressure_keys[i]]["IA"] < iaUpperBorder[ia_index]) & (self.data[self.pressure_keys[i]]["SA"] > iaLowerBorder[ia_index])

                        index = (sa==fz) & (sa == ia) & (ia == fz) & (sa == True) & (fz == True) & (ia == True)
                        df_new.append(pd.DataFrame(self.data[pressure_keys[i]][index]))
                        self.index.append(index)
                        z=z+1
                        

           
           # keyTuple = tuple(keyList)
            self.sortedLonData[pressure_keys[i]] = pd.concat(df_new, keys=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37'])

    #def plotLonData(self, ia keys):       
    #     z = 
    #    keyRange = range(z)
    #        keyList = [*keyRange]
    #        keyString=[str(j) for j in keyList]
    #    plt.figure(1)
    #    for i in range(len(self.pressure_keys[i])):
    #        plt.plot(self.sortedLonData[self.pressure_keys[i]].loc['0']['SL'],self.sortedLonData['12PSI'].loc['0']['FX'],label=self.pressure_keys[i],'o')

    #    plt.xlabel('Slip Ratio [-]')
    #    plt.yLabel('FX [N]')
    #    plt.title('FX over Slip Ratio at ...N normal force and 0° inclination angle')
    #    plt.legend()
    #    plt.show()
    #    plt.figure(2)
    #    for j in range(len(ia_keys))
    #        plt.plot(hoosier13.sortedLonData['10PSI'].loc['0']['SL'],hoosier13.sortedLonData['10PSI'].loc['0']['FX'],label=ia_keys[j],'o')
        
    #    plt.xlabel('Slip Ratio [-]')
    #    plt.yLabel('FX [N]')
    #    plt.title('FX over Slip Ratio for different inclination angles at 10 PSI and -1557 N normal force')
    #    plt.legend()
    #    plt.show()

   



"""Data import"""
'Data import'
df = pd.read_table("Grenzen.txt",header=None)
keys = df[0].tolist()
lowerBorders = df[1].tolist()
upperBorders = df[2].tolist()
key_dict = {"ia_keys": keys[0:3], "fz_keys": keys[3:7],"sa_keys":keys[7:]}
lowerBorder_dict = {"ia_lBorder":lowerBorders[0:3],"fz_lBorder":lowerBorders[3:7], "sa_lBorder":lowerBorders[7:]}
upperBorder_dict = {"ia_uBorder": upperBorders[0:3], "fz_uBorder": upperBorders[3:7], "sa_uBorder": upperBorders[7:]}
files_braking = [".\Data\B1320run4.dat",".\Data\B1320run5.dat"]
pressure_keys = ["12PSI","10PSI"]
data = {pressure_keys[0]: 0}
for i in range(len(files_braking)):
      data[pressure_keys[i]] = pd.read_table(files_braking[i],header=[1],skiprows=[2])

#print(data)

hoosier13=Tire(13,data,pressure_keys)
hoosier13.sortLonData(key_dict["ia_keys"],key_dict["fz_keys"],key_dict["sa_keys"], lowerBorder_dict["ia_lBorder"], upperBorder_dict["ia_uBorder"], lowerBorder_dict["fz_lBorder"], upperBorder_dict["fz_uBorder"], lowerBorder_dict["sa_lBorder"], upperBorder_dict["sa_uBorder"] )
#print(hoosier13.sortedLonData)
#print(hoosier13.index)

#hoosier13.plotLonData(key_dict["ia_keys"])
