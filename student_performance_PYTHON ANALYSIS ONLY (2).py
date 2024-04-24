import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#DATA CLEANING

#reading data file
def student_perform_data():    
    df=pd.read_csv('student_performance_data.csv')
    pd.options.display.max_rows=500
      
#filling null values with 0
    df.fillna(0,inplace=True)
# using mean to replace null value =0
    m=np.mean(df['Study_Hours'])
    print(m)

    m2=np.mean(df['GPA'])
    print(m2)

    m3=np.mean(df['Attendance'])
    print(m3)

#using for loop to replace null values
    m=df['Study_Hours'].mean()
    for x in df.index:
       if df.loc[x,'Study_Hours']==0:
        df.loc[x,'Study_Hours']=m

    m2=df['GPA'].mean()  
    for y in df.index:
       if df.loc[y,'GPA']==0:
          df.loc[y,'GPA']=m2

    m3=df['Attendance'].mean()
    for z in df.index:
       if df.loc[z,'Attendance']==0:
          df.loc[z,'Attendance']=m3
    
    print(df)


#EXPLORATORY DATA ANALYSIS

#CORRELATION
    correl_study_hrs_GPA=np.corrcoef(df['Study_Hours'],df['GPA'])[0,1]
    #print(correl_study_hrs_GPA)

    correl_STDid_Age=np.corrcoef(df['Student_ID'],df['Age'])[0,1]
    #print(correl_STDid_Age)

    correl_attend_peer=np.corrcoef(df['Attendance'], df['Peer_Interaction_Score'])[0,1]
    #print(correl_attend_peer)

    correl_social_media_library=np.corrcoef(df['Social_Media_Hours'],df['Library_Usage'])[0,1]
    #print(correl_social_media_library)
    correl_peer_GPA=np.corrcoef(df['Peer_Interaction_Score'],df['GPA'])[0,1]
    print(correl_peer_GPA)


#visualisation distribution
#GPA    
    plt.hist(df['GPA'])
    plt.hist(df['Study_Hours'])
    plt.hist(df['Attendance'])

#relationship bln study hrs & gpa
    plt.bar(df['Study_Hours'],df['GPA'])
    #plt.show()


#standard deviation
    stand_devi=np.std(df['Study_Hours'])
    print(stand_devi)

    stand_dev2=np.std(df['Social_Media_Hours'])
    print(stand_dev2)

    stand_dev3=np.std(df['Library_Usage'])
    print(stand_dev3)

#variance
    var_study_hrs=np.var(df['Study_Hours'])
    print(var_study_hrs)

    var_social_media=np.var(df['Social_Media_Hours'])
    print(var_social_media)

    var_library=np.var(df['Library_Usage'])
    print(var_library)


#percentile
    perc_25=np.percentile(df['GPA'],25)
    perc_50=np.percentile(df['GPA'],50)
    perc_75=np.percentile(df['GPA'],75)


    print(perc_25)
    print(perc_50)
    print(perc_75)



student_perform_data()