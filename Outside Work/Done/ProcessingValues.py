import pandas as pd

sample1ratio=1 #important (set sample index for ratio) sample number -1
sample2ratio=2

sample1BS10=1 #important (set sample index for normalising into BS10) sample number -1
sample2BS10=2

sample1Phy=1 #important (set sample index for normalising into Phytane) sample number -1
sample2Phy=2

sample1Hopane=1 #important (set sample index for normalising into Hopane) sample number -1
sample2Hopane=3

#import excel spreadsheet
df = pd.read_excel(r"Copy of Oilcomp EN_200 MS xxxx_v110-Dr.Hii.xlsm", sheet_name="Database")
df = df.iloc[9:154,]
df.dropna()
df = df.loc[:, (df != 0).all(axis=0)]
print(df)
df.to_csv('file2.csv', header=True, index=False)
df.set_index("DATABASE",inplace=True)

#rename dataframe columns
columnIndex = 0
samplecount = 0
for i in range(3,len(df.columns),2):
    df.columns.values[i-1]=f"sample{samplecount}Ret"
    df.columns.values[i]=f"sample{samplecount}Value"
    samplecount+=1

print(df.loc["1_1-M-Adam"])
print(df)

#declare important functions (normalisation, ratio, etc)
def removeFN(string):
    string=string[string.find("_")+1:]
    return string

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

def NormaliseToBS10(compound, sample1=1, sample2=2):
    print("Normalising "+compound+" to BS10")
    if df.loc["24_BS10"][f"sample{sample1}Value"]>1:
        return [df.loc[compound][f"sample{sample1}Ret"], compound, df.loc[compound][f"sample{sample1}Value"], df.loc[compound][f"sample{sample2}Value"], df.loc[compound][f"sample{sample1}Value"]/df.loc["24_BS10"][f"sample{sample1}Value"]*df.loc["24_BS10"][f"sample{sample2}Value"]]
    else:
        return [df.loc[compound][f"sample{sample1}Ret"], compound, df.loc[compound][f"sample{sample1}Value"], df.loc[compound][f"sample{sample2}Value"], 0.001]
    
def NormaliseToPhytane(compound, sample1=1, sample2=2):
    print("Normalising "+compound+" to Phytane")
    if df.loc["33_Phy"][f"sample{sample1}Value"]>1:
        return [df.loc[compound][f"sample{sample1}Ret"], compound, df.loc[compound][f"sample{sample1}Value"], df.loc[compound][f"sample{sample2}Value"], df.loc[compound][f"sample{sample1}Value"]/df.loc["33_Phy"][f"sample{sample1}Value"]*df.loc["33_Phy"][f"sample{sample2}Value"]]
    else:
        return [df.loc[compound][f"sample{sample1}Ret"], compound, df.loc[compound][f"sample{sample1}Value"], df.loc[compound][f"sample{sample2}Value"], 0.001]

def NormaliseToHopane(compound, sample1=1, sample2=3):
    print("Normalising "+compound+" to Hopane")
    if df.loc["64_30ab"][f"sample{sample1}Value"]>1:
        return [df.loc[compound][f"sample{sample1}Ret"], compound, df.loc[compound][f"sample{sample1}Value"], df.loc[compound][f"sample{sample2}Value"], df.loc[compound][f"sample{sample1}Value"]/df.loc["64_30ab"][f"sample{sample1}Value"]*df.loc["64_30ab"][f"sample{sample2}Value"]]
    else:
        return [df.loc[compound][f"sample{sample1}Ret"], compound, df.loc[compound][f"sample{sample1}Value"], df.loc[compound][f"sample{sample2}Value"], 0.001]
    
#declare function to run all set ratios
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

#run finctions and create DataFrames for each set of output
A=createRatio(sample1ratio)[0]
B=createRatio(sample2ratio)[0]
A = A.assign(ratio2=B.loc[:,'ratio'])
A.columns.values[1] = "A"
A.columns.values[2] = "B"

NormalisedToBS10=[]
for rows in df.index:
    NormalisedToBS10.append(NormaliseToBS10(rows,sample1BS10,sample2BS10))
BS10DataFrame=pd.DataFrame(NormalisedToBS10,columns=[f"RetentionTime Sample {sample1BS10}", "Compounds", "A", "B", "NormalisedToBS10"])

NormalisedToPhytane=[]
for rows in df.index:
    NormalisedToPhytane.append(NormaliseToPhytane(rows,sample1Phy,sample2Phy))
PhytaneDataFrame=pd.DataFrame(NormalisedToPhytane,columns=[f"RetentionTime Sample {sample1Phy}", "Compounds", "A", "B", "NormalisedToPhytane"])

NormalisedToHopane=[]
for rows in df.index:
    NormalisedToHopane.append(NormaliseToHopane(rows,sample1Hopane,sample2Hopane))
HopaneDataFrame=pd.DataFrame(NormalisedToHopane,columns=[f"RetentionTime Sample {sample1Hopane}", "Compounds", "A", "B", "NormalisedToHopane"])

#define and run function for computing new rows with different value
#ratio
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


#normalise to BS10
def AfterNorm2of3BS10(row):
    if row["B"]>1:
        return 100*row["NormalisedToBS10"]/row["B"]
    else:
        return 0.0001
    
BS10DataFrame["% 2/3 After Normalisation"]=BS10DataFrame.apply(AfterNorm2of3BS10, axis=1)
print(BS10DataFrame)

#normalise to Phytane
def AfterNorm2of3Phy(row):
    if row["B"]>1:
        return 100*row["NormalisedToPhytane"]/row["B"]
    else:
        return 0.0001
    
PhytaneDataFrame["% 2/3 After Normalisation"]=PhytaneDataFrame.apply(AfterNorm2of3Phy, axis=1)
print(PhytaneDataFrame)

#normalise to Hopane
def AfterNorm2of4Hopane(row):
    if row["B"]>1:
        return 100*row["NormalisedToHopane"]/row["B"]
    else:
        return 0.0001

HopaneDataFrame["% 2/3 After Normalisation"]=HopaneDataFrame.apply(AfterNorm2of4Hopane, axis=1)
print(HopaneDataFrame)

print(A)

#save down all dataframe as CSV
BS10DataFrame.to_csv('BS10DataFrame.csv')
PhytaneDataFrame.to_csv('PhytaneDataFrame.csv')
HopaneDataFrame.to_csv('HopaneDataFrame.csv')
A.to_csv('RatioDataFrame.csv')

import matplotlib.pyplot as plt
import numpy as np
import ValueStorage
import pandas as pd
import math

#load dataframe
df = pd.read_csv("BS10DataFrame.csv")
df.set_index("Unnamed: 0", inplace=True)
print(df.loc[df["Compounds"].str.contains("1_1-M-Adam")]) #get the compound and its values (test)
print(df)

#define function to find compound information based on compound name
def find_value(name: str):
    return [df.loc[df["Compounds"].str.contains(name,regex=False)].loc[:,"RetentionTime Sample 1"], df.loc[df["Compounds"].str.contains(name,regex=False)].loc[:,"% 2/3 After Normalisation"]]
find_value("59_29bbR+S") #why does 135_C28 (22S) work without a comma??? WTF pls help (solved, SOLUTION= regex=False, does not allow str.contains to return series)

#stable line values
lineLowRet = -2
lineHighRet=25
lineMinValue=0
lineMaxValue=100
dottedLowRet=6
dottedHighRet=25
dottedMinValue=5
dottedMaxValue=100
MaxTrendline=60

#setting up the graph
countPerElement = [1,4,11,17,19,23,34,43,45,49,63,71,77,88,92,98,124,130,136,145]
fig, ax = plt.subplots(figsize=(16,10))                                                                                  
count = 1
indexCount = 1

#declaring compound groups to plot
rt_nCx=[]
v_nCX=[]
rt_isoCx=[]
v_isoCx=[]
rt_brCx=[]
v_brCx=[]
rt_nCxCyhex=[]
v_nCxCyhex=[]
rt_de=[]
v_de=[]
rt_adam=[]
v_adam=[]
rt_BS=[]
v_BS=[]
rt_diam=[]
v_diam=[]
rt_tricyTerp=[]
v_tricyTerp=[]
rt_hopa=[]
v_hopa=[]
rt_ster=[]
v_ster=[]
rt_CxBenz=[]
v_CxBenz=[]
rt_cxTol=[]
v_cxTol=[]
rt_HyPAH=[]
v_HyPAH=[]
rt_PAH=[]
v_PAH=[]
rt_CxPAH=[]
v_CxPAH=[]
rt_SPAH=[]
v_SPAH=[]
rt_TAS=[]
v_TAS=[]
rt_FAME=[]
v_FAME=[]

#assigning values to compounds
for i in ValueStorage.PW_PlotValues:
    datax, datay = find_value(i)
    if indexCount>= 1 and indexCount <= 4: #0
        rt_nCx.append(datax)
        v_nCX.append(datay)
    if indexCount>4 and indexCount<=11: #1
        rt_isoCx.append(datax)
        v_isoCx.append(datay)
    if indexCount>11 and indexCount<=17: #2
        rt_brCx.append(datax)
        v_brCx.append(datay)
    if indexCount>17 and indexCount<=19:#3
        rt_nCxCyhex.append(datax)
        v_nCxCyhex.append(datay)
    if indexCount>19 and indexCount<=23: #4
        rt_de.append(datax)
        v_de.append(datay)
    if indexCount>23 and indexCount<=34: #5
        rt_adam.append(datax)
        v_adam.append(datay)
    if indexCount>34 and indexCount<=43: #6
        rt_BS.append(datax)
        v_BS.append(datay)
    if indexCount>43 and indexCount<=45: #7
        rt_diam.append(datax)
        v_diam.append(datay)
    if indexCount>45 and indexCount<=49: #8
        rt_tricyTerp=[]
        v_tricyTerp=[]
    if indexCount>49 and indexCount<=63: #9
        rt_hopa.append(datax)
        v_hopa.append(datay)
    if indexCount>63 and indexCount<=71: #10
        rt_ster.append(datax)
        v_ster.append(datay)
    if indexCount>71 and indexCount<=77: #11
        rt_CxBenz.append(datax)
        v_CxBenz.append(datay)
    if indexCount>77 and indexCount<=88: #12
        rt_cxTol.append(datax)
        v_cxTol.append(datay)
    if indexCount>88 and indexCount<=92: #13
        rt_HyPAH.append(datax)
        v_HyPAH.append(datay)
    if indexCount>92 and indexCount<=98: #14
        rt_PAH.append(datax)
        v_PAH.append(datay)
    if indexCount>98 and indexCount<=124: #15
        rt_CxPAH.append(datax)
        v_CxPAH.append(datay)
    if indexCount>124 and indexCount<=130: #16
        rt_SPAH.append(datax)
        v_SPAH.append(datay)
    if indexCount>130 and indexCount<=136: #17
        rt_TAS.append(datax)
        v_TAS.append(datay)
    if indexCount>136 and indexCount<=146: #18
        rt_FAME.append(datax)
        v_FAME.append(datay)
        #print(i) #show compounds
    indexCount += 1

#plotting compounds, rearrange the lines as you see fit to alter the order of the compounds on the legend
ax.plot(rt_nCx, v_nCX , marker='s',markerfacecolor='none', ls='none',color = "green",label = "n-Cx") #n-Cx
ax.plot(rt_isoCx, v_isoCx, marker='s', ls='none',color = "Grey",label = "ico-Cx",markeredgewidth=1, markeredgecolor="black") #iso-Cx
ax.plot(rt_brCx, v_brCx , marker='^', ls='none',color = "Green",label = "br-Cx") #br-Cx
ax.plot(rt_nCxCyhex, v_nCxCyhex, marker='+', ls='none',color = "green",label = "n-Cx-cyhex",ms=6) #nCxCyhex
ax.plot(rt_de, v_de, marker='.',markerfacecolor='none', ls='none',color = "Black",label = "de",ms=12) #de
ax.plot(rt_adam, v_adam, marker='.', ls='none',color = "black",label = "adam",ms=12) #adam
ax.plot(rt_BS, v_BS, marker='D',markerfacecolor='none', ls='none',color = "black",label = "BS") #BS
ax.plot(rt_diam, v_diam, marker='_', ls='none',color = "Black",label = "diam",markeredgewidth=1.5, markeredgecolor="black",ms=10) #diam
ax.plot(rt_tricyTerp, v_tricyTerp, marker='x', ls='none',color = "black",label = "Tricy-terp") #tricyTerp
ax.plot(rt_tricyTerp, v_tricyTerp, marker='|', ls='none',color = "black") #tricyTerp
ax.plot(rt_hopa, v_hopa, marker='D', ls='none',color = "Black",label = "hop") #hop
ax.plot(rt_ster, v_ster, marker='^', ls='none',color = "Black",label = "ster") #ster
ax.plot(rt_CxBenz, v_CxBenz, marker='x', ls='none',color = "green",label = "Cx-benz") #Cx-Benz
ax.plot(rt_cxTol, v_cxTol, marker='x', ls='none',color = "red",label = "Cx-tol") #Cx-tol
ax.plot(rt_cxTol, v_cxTol, marker='|', ls='none',color = "red") #Cx-tol
ax.plot(rt_HyPAH, v_HyPAH, marker='.', ls='none',color = "Red",label = "Hy-PAH",ms=12) #Hy-PAH
ax.plot(rt_PAH, v_PAH, marker='.',markerfacecolor='none', ls='none',color = "Red",label = "PAH",ms=12) #PAH
ax.plot(rt_CxPAH, v_CxPAH, marker='^', ls='none',color = "Red",label = "Cx-PAH") #Cx-PAH
ax.plot(rt_SPAH, v_SPAH, marker='+', ls='none',color = "Brown",label = "S-PAH", ms=8) #S-PAH
ax.plot(rt_TAS, v_TAS, marker='D', ls='none',color = "Red",label = "TAS", ms=4) #TAS
ax.plot(rt_FAME, v_FAME, marker='s', ls='none',color = "green",label = "FAME",ms=6) #FAME

#set up constant line values
controlRT=[]
lineFactor=[]
lineYvalue=[]
dottedFactor=[]
dottedYvalue=[]
for i in range(5,MaxTrendline+6):
    controlRT.append(i)
    #line
    lineFactor.append(180*((i-lineLowRet)/(lineHighRet-lineLowRet)))
    if lineLowRet>i:
        lineYvalue.append(lineMinValue)
    else:
        if i>lineHighRet:
            lineYvalue.append(lineMaxValue)
        else:
            lineYvalue.append(lineMinValue+((lineMaxValue-lineMinValue)/2)+(math.sin(math.radians(180*((i-lineLowRet)/(lineHighRet-lineLowRet))-90))*((lineMaxValue-lineMinValue)/2)))
    #dotted line
    dottedFactor.append(180*((i-dottedLowRet)/(dottedHighRet-dottedLowRet)))
    if dottedLowRet>i:
        dottedYvalue.append(dottedMinValue)
    else:
        if i>dottedHighRet:
            dottedYvalue.append(dottedMaxValue)
        else:
            dottedYvalue.append(dottedMinValue+((dottedMaxValue-dottedMinValue)/2)+(math.sin(math.radians(180*((i-dottedLowRet)/(dottedHighRet-dottedLowRet))-90))*((dottedMaxValue-dottedMinValue)/2)))
print(lineYvalue)

#create dataframe for future use
TrendLineStableCompounds = pd.DataFrame()
TrendLineStableCompounds["ret time"]=controlRT
TrendLineStableCompounds["line factor"]=lineFactor
TrendLineStableCompounds["line y value"]=lineYvalue
TrendLineStableCompounds["dotted line factor"]=dottedFactor
TrendLineStableCompounds["dotted y value"]=dottedYvalue

#show dataframe
print(TrendLineStableCompounds)

#assign variables to values on dataframe to plot
x = TrendLineStableCompounds["ret time"]
y = TrendLineStableCompounds["line y value"]
y2 = TrendLineStableCompounds["dotted y value"]
#plot line
ax.plot(x,y,color = "black",linestyle = "-",label = "evap1",linewidth = 3)
ax.plot(x,y2,color = "black",linestyle = ":",label = "trend2",linewidth = 3)
ax.axhline(y = 85, color = '#964B00', linestyle = ':',label = "line 85", linewidth = 3) 
ax.axhline(y = 118, color = '#964B00', linestyle = ':', label = "line 118",linewidth = 3) 

#continue on setting up graph
plt.xticks(np.arange(5,65, step=10)) 
plt.yticks(np.arange(0,140,step=20))
ax.set_xlabel("retention time", loc='center')
ax.set_ylabel('%')
pos = ax.get_position()
ax.set_position([pos.x0, pos.y0, pos.width, pos.height * 0.85])

#set legend
ax.legend(
    loc='upper center', 
    bbox_to_anchor=(0.5,1.2),
    ncol = 6,
    title = "A - B: Normalised to BS10",
    fontsize = 9.4,
    )
plt.grid(axis = "y")

plt.savefig("finalBS10.png")