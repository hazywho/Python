import pandas as pd
#import excel spreadsheet and remove NAN values
df = pd.read_excel(r"Copy of Oilcomp EN_200 MS xxxx_v110-Dr.Hii.xlsm", sheet_name="Database")
df = df.iloc[9:154,]
df.dropna()
df = df.loc[:, (df != 0).all(axis=0)]
print(df)
df.to_csv('file2.csv', header=True, index=False) #for testing purposes only, please ignore this line
df.set_index("DATABASE",inplace=True)

#rename columns
columnIndex = 0
samplecount = 0
for i in range(3,len(df.columns),2):
    df.columns.values[i-1]=f"sample{samplecount}Ret"
    df.columns.values[i]=f"sample{samplecount}Value"
    samplecount+=1
print(df.loc["1_1-M-Adam"])

#function to remove numbering at the front (eg: 1_1-M-Adam to 1-M-Adam)
def removeFN(string):
    string=string[string.find("_")+1:]
    return string

#function to calculate ratio of compounds (1 sample only)
def ratio(compound1,compound2,sample=0,Normative=True):
    print("Starting the ratio of "+compound1+" and "+compound2)
    if df.loc[compound1][f"sample{sample}Value"]>1 and df.loc[compound2][f"sample{sample}Value"]>1:
        if Normative:
            return ["NR-"+removeFN(compound1)+"/"+removeFN(compound2), 100*(df.loc[compound1][f"sample{sample}Value"]/df.loc[compound2][f"sample{sample}Value"])]
        else:
            return [removeFN(compound1)+"/"+removeFN(compound2), 100*(df.loc[compound1][f"sample{sample}Value"]/df.loc[compound2][f"sample{sample}Value"])]
    else:
        if Normative:
            return ["NR-"+removeFN(compound1)+"/"+removeFN(compound2), 0.0001]
        else:
            return [removeFN(compound1)+"/"+removeFN(compound2), 0.0001]

#creating dataframes of ratios  
def createRatio(sampleNo=0):
    NormarativeRatio=[]
    NormarativeRatio.append(ratio("1_1-M-Adam","2_1,2-DM-Adam",sampleNo))
    NormarativeRatio.append(ratio("1_1-M-Adam","8_2-E-Adam",sampleNo))
    NormarativeRatio.append(ratio("3_i-C13","4_2-M-Tetralin",sampleNo))
    NormarativeRatio.append(ratio("5_c-1,3,4-TM-Adam","8_2-E-Adam",sampleNo)) #checked
    NormarativeRatio.append(ratio("6_C6_Benz","12_C7_Benz",sampleNo))
    NormarativeRatio.append(ratio("8_2-E-Adam","7_i-C14",sampleNo))
    NormarativeRatio.append(ratio("9_BS1","11_BS2",sampleNo))
    NormarativeRatio.append(ratio("10_C3-de peak","11_BS2",sampleNo)) #checked
    NormarativeRatio.append(ratio("13_B","14_2-E-N",sampleNo))
    NormarativeRatio.append(ratio("14_2-E-N","15_2,6+2,7-DM-N",sampleNo))
    NormarativeRatio.append(ratio("17_BS4","18_BS5",sampleNo))
    NormarativeRatio.append(ratio("16_Br-Alk 169-3","20_n-C15",sampleNo))
    NormarativeRatio.append(ratio("18_BS5","19_BS6",sampleNo)) #checked
    NormarativeRatio.append(ratio("21_BS8","22_BS9",sampleNo))
    NormarativeRatio.append(ratio("23_m-C8-Tol","25_o-C8-Tol",sampleNo))
    NormarativeRatio.append(ratio("24_BS10","26_Norpri",sampleNo))
    NormarativeRatio.append(ratio("26_Norpri","27_m-C9-Tol",sampleNo))
    NormarativeRatio.append(ratio("28_C10_Benz","31_n-C11-CyC6",sampleNo))
    NormarativeRatio.append(ratio("29_n-C17","30_Pri",sampleNo)) #checked
    NormarativeRatio.append(ratio("30_Pri","33_Phy",sampleNo))
    NormarativeRatio.append(ratio("32_n-C18","33_Phy",sampleNo))
    NormarativeRatio.append(ratio("34_4-M-Dbt","37_1-M-Dbt",sampleNo))
    NormarativeRatio.append(ratio("35_Br-Alk 225-3","36_n-C19",sampleNo))
    NormarativeRatio.append(ratio("38_2-M-Phe","40_1-M-Phe",sampleNo))
    NormarativeRatio.append(ratio("39_FAME 16:0","43_FAME 18:0",sampleNo))
    NormarativeRatio.append(ratio("41_C2-dbt_s","42_C2-phe_s",sampleNo)) #checked
    NormarativeRatio.append(ratio("44_2-M-Fl","49_4-M-Py",sampleNo))
    NormarativeRatio.append(ratio("45_C15-Benz","53_C17-Benz",sampleNo))
    NormarativeRatio.append(ratio("46_BaF","49_4-M-Py",sampleNo))
    NormarativeRatio.append(ratio("47_Retene","59_29bbR+S",sampleNo))
    NormarativeRatio.append(ratio("48_2-M-Py","49_4-M-Py",sampleNo))
    NormarativeRatio.append(ratio("50_1-M-Py","49_4-M-Py",sampleNo))
    NormarativeRatio.append(ratio("51_C23Tr","52_C24Tr",sampleNo))
    NormarativeRatio.append(ratio("54_27bbR+S","59_29bbR+S",sampleNo))
    NormarativeRatio.append(ratio("55_27Ts","64_30ab",sampleNo))
    NormarativeRatio.append(ratio("56_SC26 TA","58_RC26TA+SC27 TA",sampleNo)) #checked
    NormarativeRatio.append(ratio("57_27Tm","64_30ab",sampleNo))
    NormarativeRatio.append(ratio("60_28ab","64_30ab",sampleNo))
    NormarativeRatio.append(ratio("61_SC28 TA","58_RC26TA+SC27 TA",sampleNo))
    NormarativeRatio.append(ratio("62_29ab","64_30ab",sampleNo))
    NormarativeRatio.append(ratio("63_30O","64_30ab",sampleNo))
    NormarativeRatio.append(ratio("65_RC28 TA","58_RC26TA+SC27 TA",sampleNo))
    NormarativeRatio.append(ratio("66_31abS","64_30ab",sampleNo))
    NormarativeRatio.append(ratio("67_30G","64_30ab",sampleNo)) #checked

    InformativeRatio=[]
    InformativeRatio.append(ratio("68_De", "1_1-M-Adam", sampleNo, Normative=False))
    InformativeRatio.append(ratio("1_1-M-Adam", "71_2-M-Adam", sampleNo, Normative=False))
    InformativeRatio.append(ratio("69_1,3,5-TM-Adam", "75_tr-1,4-DM-Adam", sampleNo, Normative=False))
    InformativeRatio.append(ratio("69_1,3,5-TM-Adam", "76_1,3,6-TM-Adam", sampleNo, Normative=False))
    InformativeRatio.append(ratio("70_C1-de_s", "77_C2-de_s", sampleNo, Normative=False))
    InformativeRatio.append(ratio("72_Tetralin", "4_2-M-Tetralin", sampleNo, Normative=False))
    InformativeRatio.append(ratio("79_1,2,5,7-TeM-Adam ", "8_2-E-Adam", sampleNo, Normative=False))
    InformativeRatio.append(ratio("79_1,2,5,7-TeM-Adam ", "24_BS10", sampleNo, Normative=False))
    InformativeRatio.append(ratio("81_m-C6-Tol", "24_BS10", sampleNo, Normative=False))
    InformativeRatio.append(ratio("81_m-C6-Tol", "83_ o-C6-Tol", sampleNo, Normative=False))
    InformativeRatio.append(ratio("12_C7_Benz", "28_C10_Benz", sampleNo, Normative=False))
    InformativeRatio.append(ratio("87_BS3", "18_BS5", sampleNo, Normative=False))
    InformativeRatio.append(ratio("86_1,6-DM-N", "85_1,3+1,7-DM-N", sampleNo, Normative=False))
    InformativeRatio.append(ratio("89_ANY", "92_1,2 -DM-N", sampleNo, Normative=False))
    InformativeRatio.append(ratio("95_ Diam", "97_4-M-Diam", sampleNo, Normative=False))
    InformativeRatio.append(ratio("96_FAME 12:0", "39_FAME 16:0", sampleNo, Normative=False))
    InformativeRatio.append(ratio("98_1,3,7-TM-N", "99_1,3,6-TM-N", sampleNo, Normative=False)) #checked
    InformativeRatio.append(ratio("21_BS8", "24_BS10", sampleNo, Normative=False))
    InformativeRatio.append(ratio("102_8H-A", "104_8H-Phe", sampleNo, Normative=False))
    InformativeRatio.append(ratio("103_1-M-F", "104_8H-Phe", sampleNo, Normative=False))
    InformativeRatio.append(ratio("105_FAME 14:0", "39_FAME 16:0", sampleNo, Normative=False))
    InformativeRatio.append(ratio("112_FAME 16:1", "39_FAME 16:0", sampleNo, Normative=False))
    InformativeRatio.append(ratio("114_1-E-Phe", "115_1,7 DM-Phe", sampleNo, Normative=False))
    InformativeRatio.append(ratio("116_C3-dbt_s", "121_C3-phe_s", sampleNo, Normative=False))
    InformativeRatio.append(ratio("117_FAME 18:2", "43_FAME 18:0", sampleNo, Normative=False))
    InformativeRatio.append(ratio("118_FAME 18:1 + 18:3", "43_FAME 18:0", sampleNo, Normative=False))
    InformativeRatio.append(ratio("120_C21Tr", "51_C23Tr", sampleNo, Normative=False))
    InformativeRatio.append(ratio("51_C23Tr", "131_Phy-Tol", sampleNo, Normative=False))
    InformativeRatio.append(ratio("125_FAME 20:0", "43_FAME 18:0", sampleNo, Normative=False))
    InformativeRatio.append(ratio("128_C20TA", "130_C21 TA", sampleNo, Normative=False))
    InformativeRatio.append(ratio("130_C21 TA", "58_RC26TA+SC27 TA", sampleNo, Normative=False))
    InformativeRatio.append(ratio("135_C28 (22S)", "64_30ab", sampleNo, Normative=False))
    InformativeRatio.append(ratio("137_BePy", "138_BaPy ", sampleNo, Normative=False))
    InformativeRatio.append(ratio("141_29aaS", "143_29aaR", sampleNo, Normative=False)) #checked
    infor = pd.DataFrame(InformativeRatio, columns=["Compounds","ratio"])
    norm = pd.DataFrame(NormarativeRatio, columns=["Compounds","ratio"])
    fin = pd.concat([norm,infor])
    return [fin,infor,norm]

#run the functions on 2 different samples.
A=createRatio(1)[0]
B=createRatio(2)[0]
A = A.assign(ratio2=B.loc[:,'ratio'])
A.columns.values[1] = "A"
A.columns.values[2] = "B"

#calculate other values
def mean(row):
    return (row['A']+row['B'])/2
def absDiff(row):
    return abs(row['A']-row['B'])
def relDiff(row):
    if row['mean']>0:
        return (row['absoluteDifference']/row['mean'])*100
    else:
        return 0.0001
def flagging(row):
    if row['relativeDifference%']>14:
        return 1
    else:
        return 0
A['mean'] = A.apply(mean,axis=1)
A['absoluteDifference'] = A.apply(absDiff,axis=1)
A['relativeDifference%'] = A.apply(relDiff,axis=1)
A['14%flag'] = A.apply(flagging,axis=1)

#save csv file
A.to_csv('output.csv')