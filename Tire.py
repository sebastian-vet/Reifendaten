import pandas as pd
import matplotlib.pyplot as plt
import os


class Tire:
    """ In der Klasse Tire werden alle Informationen zu einem Reifen gespeichert. """

    def __init__(self, size, data, pressure_keys):
        self.size = size
        self.data = data
        self.pressure_keys = pressure_keys
        self.sortedLonData = {pressure_keys[0]: []}
        self.bool_index = []

    # Sortiert die Daten nach "Situationen".
    def sortLonData(self, ia_keys, fz_keys, sa_keys, iaLowerBorder, 
                    iaUpperBorder, fzLowerBorder, fzUpperBorder, 
                    slipAngleLowerBorder, slipAngleUpperBorder):
        z = 0
        for pressure_key in self.pressure_keys:
            # self.sortedLonData[pressure_key]=pd.DataFrame()
            df_new = []
            for sa_index in range(len(sa_keys)):
                sa = 0
                sa = (self.data[pressure_key]["SA"] < slipAngleUpperBorder[sa_index]) & (
                    self.data[pressure_key]["SA"] > slipAngleLowerBorder[sa_index])
                for fz_index in range(len(fz_keys)):
                    fz = 0
                    fz = (self.data[pressure_key]["FZ"] < fzUpperBorder[fz_index]) & (
                        self.data[pressure_key]["SA"] > fzLowerBorder[fz_index])
                    for ia_index in range(len(ia_keys)):
                        ia = 0
                        ia = (self.data[pressure_key]["IA"] < iaUpperBorder[ia_index]) & (
                            self.data[pressure_key]["SA"] > iaLowerBorder[ia_index])
                        bool_index = []

                        for m, n, b in zip(sa, fz, ia):
                            if (m == n) & (m == b) & (b == n):
                                bool_index.append(True)
                            else:
                                bool_index.append(False)

                        # print(bool_index)
                        #bool_index = (sa==fz) & (sa == ia) & (ia == fz) & (sa == True) & (fz == True) & (ia == True)
                        bool_series = pd.Series(bool_index, name='bool')
                        df_loop = pd.DataFrame()
                        df_loop = pd.DataFrame(
                            self.data[pressure_key][bool_series])

                        # for index_index in range(len(bool_index)):
                        #    if bool_index[index_index]:
                        #        df_loop.append(self.data[pressure_key].loc[index_index])

                        df_new.append(df_loop)
                        # df_new.append(pd.DataFrame(self.data[pressure_key].iloc[index_index]))
                        # df_new.append(pd.DataFrame(self.data[pressure_key][bool_index]))
                        # self.bool_index.append(bool_index)
                        # z=z+1

            df_finish = pd.DataFrame()
            df_finish = pd.concat(df_new, keys=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                                                '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37'])
            self.sortedLonData[pressure_key] = df_finish

    def plotLonData(self, ia_keys):
        z = list(self.sortedLonData["10PSI"].index.get_level_values(0))
        z = list(dict.fromkeys(z))
        plt.figure(1)
        for i in range(len(self.pressure_keys)):
            plt.plot(self.sortedLonData[self.pressure_keys[i]].loc['0']['SL'],
                     self.sortedLonData[self.pressure_keys[i]].loc['0']['FX'], label=self.pressure_keys[i])

        plt.xlabel('Slip ratio [-]')
        plt.ylabel('Fx [N]')
        plt.title(
            'Fx over slip ratio at -1557N normal force and 0° inclination angle')
        plt.legend()
        plt.show()
        plt.figure(2)
        for j in range(len(ia_keys)):
            plt.plot(self.sortedLonData['10PSI'].loc[z[j]]['SL'],
                     self.sortedLonData['10PSI'].loc[z[j]]['FX'], label=ia_keys[j])

        plt.xlabel('Slip ratio [-]')
        plt.ylabel('Fx [N]')
        plt.title(
            'Fx over slip ratio for different inclination angles at 10 psi and -1557 N normal force')
        plt.legend()
        plt.show()
