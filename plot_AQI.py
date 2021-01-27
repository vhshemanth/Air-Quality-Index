import pandas as pd
import matplotlib.pyplot as plt


def avg_data_2013():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2013.csv',chunksize=24):
        add_var=0
        avg_val=0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is str:
                if i != "NoData" and i !='---' and i !='InVld' and i !='PwrFail':
                    temp=float(i)
                    add_var+=temp

        avg=add_var/24
        temp_i+=1
        average.append(avg)
    return average

def avg_data_2014():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2014.csv',chunksize=24):
        add_var=0
        avg_val=0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is str:
                if i != "NoData" and i !='---' and i !='InVld' and i !='PwrFail':
                    temp=float(i)
                    add_var+=temp

        avg=add_var/24
        temp_i+=1
        average.append(avg)
    return average

def avg_data_2015():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2015.csv',chunksize=24):
        add_var=0
        avg_val=0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is str:
                if i != "NoData" and i !='---' and i !='InVld' and i !='PwrFail':
                    temp=float(i)
                    add_var+=temp

        avg=add_var/24
        temp_i+=1
        average.append(avg)
    return average

def avg_data_2016():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2016.csv',chunksize=24):
        add_var=0
        avg_val=0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is str:
                if i != "NoData" and i !='---' and i !='InVld' and i !='PwrFail':
                    temp=float(i)
                    add_var+=temp

        avg=add_var/24
        temp_i+=1
        average.append(avg)
    return average
def avg_data_2017():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2017.csv',chunksize=24):
        add_var=0
        avg_val=0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is str:
                if i != "NoData" and i !='---' and i !='InVld' and i !='PwrFail':
                    temp=float(i)
                    add_var+=temp

        avg=add_var/24
        temp_i+=1
        average.append(avg)
    return average

def avg_data_2018():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2018.csv',chunksize=24):
        add_var=0
        avg_val=0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is str:
                if i != "NoData" and i !='---' and i !='InVld' and i !='PwrFail':
                    temp=float(i)
                    add_var+=temp

        avg=add_var/24
        temp_i+=1
        average.append(avg)
    return average


if __name__=="__main__":
    lst_2013=avg_data_2013()
    lst_2014=avg_data_2014()
    lst_2015=avg_data_2015()
    lst_2016=avg_data_2016()
    lst_2017=avg_data_2017()
    lst_2018=avg_data_2018()
    plt.plot(lst_2013)
    plt.plot(lst_2014)
    plt.plot(lst_2015)
    plt.plot(lst_2016)
    plt.plot(lst_2017)
    plt.plot(lst_2018)
    plt.show()






