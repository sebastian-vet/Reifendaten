import pandas as pd
import matplotlib.pyplot as plt
import os


class Tire:
    """ In der Klasse Tire werden alle Informationen zu einem Reifen gespeichert. """

    def __init__(self, data_braking, data_cornering,  pressure_keys):
        self.data_braking = data_braking
        self.data_cornering = data_cornering
        self.pressure_keys = pressure_keys
        self.sortedLonData = {pressure_keys[0]: []}
        self.sortedLatData = {pressure_keys[0]: []}
        self.bool_index = []

    # Sortiert die Braking Daten nach "Situationen".
    def sortLonData(self, ia_keys, fz_keys, sa_keys, iaLowerBorder, 
                    iaUpperBorder, fzLowerBorder, fzUpperBorder, 
                    slipAngleLowerBorder, slipAngleUpperBorder):
        z = 0
        for pressure_key in self.pressure_keys:
            # self.sortedLonData[pressure_key]=pd.DataFrame()
            df_new = []
            for sa_index in range(len(sa_keys)):
                sa = 0
                sa = (self.data_braking[pressure_key]["SA"] < slipAngleUpperBorder[sa_index]) & (
                    self.data_braking[pressure_key]["SA"] > slipAngleLowerBorder[sa_index])
                for fz_index in range(len(fz_keys)):
                    fz = 0
                    fz = (self.data_braking[pressure_key]["FZ"] < fzUpperBorder[fz_index]) & (
                        self.data_braking[pressure_key]["FZ"] > fzLowerBorder[fz_index])
                    for ia_index in range(len(ia_keys)):
                        ia = 0
                        ia = (self.data_braking[pressure_key]["IA"] < iaUpperBorder[ia_index]) & (
                            self.data_braking[pressure_key]["IA"] > iaLowerBorder[ia_index])
                        bool_index = []

                        for m, n, b in zip(sa, fz, ia):
                            if m & n & b:
                                bool_index.append(True)
                            else:
                                bool_index.append(False)

                        # print(bool_index)
                        #bool_index = (sa==fz) & (sa == ia) & (ia == fz) & (sa == True) & (fz == True) & (ia == True)
                        bool_series = pd.Series(bool_index, name='bool')
                        df_loop = pd.DataFrame()
                        df_loop = pd.DataFrame(
                        self.data_braking[pressure_key][bool_series])

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

    def plotLonData(self, ia_keys, tireName):
        z = list(self.sortedLonData["10PSI"].index.get_level_values(0))
        z = list(dict.fromkeys(z))
        plt.figure()
        for i in range(len(self.pressure_keys)):
            plt.plot(self.sortedLonData[self.pressure_keys[i]].loc['0']['SL'],
                     self.sortedLonData[self.pressure_keys[i]].loc['0']['FX'], label=self.pressure_keys[i], marker='.', linestyle = "None")

        plt.xlabel('Slip ratio [-]')
        plt.ylabel('Fx [N]')
        plt.title(
            'Fx over slip ratio for different pressures at -1557N normal force and 0° inclination angle')
        plt.legend()
        #plt.show()
        plt.savefig("Figures/"+tireName+"/FX_over_slipRatio_for_p.pdf", bbox_inches = 'tight')
        plt.close
        plt.figure()
        for j in range(len(ia_keys)):
            plt.plot(self.sortedLonData['10PSI'].loc[z[j]]['SL'],
                     self.sortedLonData['10PSI'].loc[z[j]]['FX'], label=ia_keys[j], marker='.', linestyle = "None")

        plt.xlabel('Slip ratio [-]')
        plt.ylabel('Fx [N]')
        plt.title(
            'Fx over slip ratio for different inclination angles at 10 psi and -1557 N normal force')
        plt.legend()
        #plt.show()
        plt.savefig("Figures/"+tireName+"/FX_over_slipRatio_for_ia.pdf", bbox_inches = 'tight')
        plt.close

        plt.figure()
        for j in range(len(ia_keys)):
            plt.plot(self.sortedLonData['10PSI'].loc[z[j]]['SL'],
                     self.sortedLonData['10PSI'].loc[z[j]]['TSTC'], label=ia_keys[j], marker='.', linestyle = "None")

        plt.xlabel('Slip ratio [-]')
        plt.ylabel('T [°C]')
        plt.title(
            'T over slip ratio for different inclination angles at 10 psi and -1557 N normal force')
        plt.legend()
        #plt.show()
        plt.savefig("Figures/"+tireName+"/T_over_slipRatio_for_ia.pdf", bbox_inches = 'tight')
        plt.close

        #plt.plot(self.sortedLonData['10PSI'].loc["0"]['FZ'],
        #             self.sortedLonData['10PSI'].loc["0"]['FX'], label=ia_keys[j])

        #plt.xlabel('Slip ratio [-]')
        #plt.ylabel('Fx [N]')
        #plt.title(
        #    'Fx over Fz for different slip ratios at 10 psi and -1557 N normal force')
        #plt.legend()
        ##plt.show()
        #plt.savefig("Figures/FX_over_slipRatio_for_ia.pdf", bbox_inches = 'tight')




    # Sortiert die Cornering Daten nach "Situationen".
    def sortLatData(self, ia_keys, fz_keys, sa_keys, iaLowerBorder, 
                    iaUpperBorder, fzLowerBorder, fzUpperBorder, 
                    slipAngleLowerBorder, slipAngleUpperBorder):
        for pressure_key in self.pressure_keys:
            df_new = []
            for fz_index in range(len(fz_keys)):
                fz = 0
                fz = (self.data_cornering[pressure_key]["FZ"] < fzUpperBorder[fz_index]) & (
                       self.data_cornering[pressure_key]["FZ"] > fzLowerBorder[fz_index])
                for ia_index in range(len(ia_keys)):
                    ia = 0
                    ia = (self.data_cornering[pressure_key]["IA"] < iaUpperBorder[ia_index]) & (
                            self.data_cornering[pressure_key]["IA"] > iaLowerBorder[ia_index])
                    bool_index = []

                    for  n, b in zip(fz, ia):
                        if  n & b:
                            bool_index.append(True)
                        else:
                            bool_index.append(False)

                    bool_series = pd.Series(bool_index, name='bool')
                    df_loop = pd.DataFrame()
                    df_loop = pd.DataFrame(
                    self.data_cornering[pressure_key][bool_series])
                    df_new.append(df_loop)


            df_finish = pd.DataFrame()
            df_finish = pd.concat(df_new, keys=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                                                '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37'])
            self.sortedLatData[pressure_key] = df_finish


    def plotLatData(self, ia_keys, fz_keys, sa_keys, tireName):
            z = list(self.sortedLatData["10PSI"].index.get_level_values(0))
            z = list(dict.fromkeys(z))
            plt.figure()
            for i in range(len(self.pressure_keys)):
                plt.plot(self.sortedLatData[self.pressure_keys[i]].loc["0"]['SA'],
                         self.sortedLatData[self.pressure_keys[i]].loc["0"]['FY'], label=self.pressure_keys[i], marker='.', linestyle = "None")

            plt.xlabel('Slip angle [°]')
            plt.ylabel('Fy [N]')
            plt.title(
                'Fy over slip angle for different pressures at -1557N normal force and 0° inclination angle')
            plt.legend()
            #plt.show()
            plt.savefig("Figures/"+tireName+"/FY_over_slipAngle_for_p.pdf", bbox_inches = 'tight')
            plt.close


            plt.figure()
            for j in range(len(ia_keys)):
                plt.plot(self.sortedLatData['10PSI'].loc[z[j]]['SA'],
                         self.sortedLatData['10PSI'].loc[z[j]]['FY'], label=ia_keys[j], marker='.', linestyle = "None")

            plt.xlabel('Slip angle [°]')
            plt.ylabel('Fy [N]')
            plt.title(
                'Fy over slip angle for different inclination angles at 10 psi and -1557 N normal force')
            plt.legend()
            #plt.show()
            plt.savefig("Figures/"+tireName+"/FY_over_slipAngle_for_ia.pdf", bbox_inches = 'tight')
            plt.close

            plt.figure()
            for j in range(len(ia_keys)):
                plt.plot(self.sortedLatData['10PSI'].loc[z[j]]['SA'],
                     self.sortedLatData['10PSI'].loc[z[j]]['TSTC'], label=ia_keys[j], marker='.', linestyle = "None")

            plt.xlabel('Slip angle [°]')
            plt.ylabel('T [°C]')
            plt.title(
                'T over slip angle for different inclination angles at 10 psi and -1557 N normal force')
            plt.legend()
            #plt.show()
            plt.savefig("Figures/"+tireName+"/T_over_slipAngle_for_ia.pdf", bbox_inches = 'tight')
            plt.close

            plt.figure()
            for j in range(len(fz_keys)):
                plt.plot(self.sortedLatData['10PSI'].loc[z[j*3]]['SA'],
                     self.sortedLatData['10PSI'].loc[z[j*3]]['MZ'], label=fz_keys[j], marker='.', linestyle = "None")

            plt.xlabel('Slip angle [°]')
            plt.ylabel('Mz [Nm]')
            plt.title(
                'Mz over slip angle for different normal loads at 10 psi and inclination angle = 0')
            plt.legend()
            #plt.show()
            plt.savefig("Figures/"+tireName+"/Mz_over_slipAngle_for_fz.pdf", bbox_inches = 'tight')
            plt.close

