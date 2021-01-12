import numpy as np
import torch
from ising import Ising

def dataset1(len_of_timeseries,number_of_timeseries,noise_frequency=0,mu=0,sigma=1):
    
    time_series=torch.empty((number_of_timeseries,len_of_timeseries)).normal_(mean=0,std=1)
    for i in range(1,len_of_timeseries):
        for j in range(number_of_timeseries):
                add_gaussian_noise=False
                if np.random.random()>(1-noise_frequency):
                    add_gaussian_noise=True
                time_series[j,i]=time_series[j,0] + add_gaussian_noise*np.random.normal(mu,sigma)
    return time_series


def dataset2(len_of_timeseries,number_of_timeseries,coef_lag_list,noise_frequency=0,mu=0,sigma=1):
    
    if type(coef_lag_list)==int:
        coef_lag_list=[(1,coef_lag_list)]
    
    if type(coef_lag_list)==tuple:
        coef_lag_list=[coef_lag_list]
        
    if type(coef_lag_list)==list and type(coef_lag_list[0])==tuple:
        coef_lag_list=[coef_lag_list]*number_of_timeseries
        
    time_series=torch.empty((number_of_timeseries,len_of_timeseries)).normal_(mean=0,std=1)
    for j in range(number_of_timeseries):
        timeseries_coef_lag_list=coef_lag_list[j]
        max_lag=timeseries_coef_lag_list[0][0]
        for coef,lag in timeseries_coef_lag_list:
            if lag>max_lag:
                max_lag=lag
            
        for i in range(max_lag,len_of_timeseries):
            add_gaussian_noise=False
            sum_of_coefs=0
            if np.random.random()>(1-noise_frequency):
                add_gaussian_noise=True
            time_series[j,i]=0
            for coef,lag in timeseries_coef_lag_list:
                time_series[j,i]=time_series[j,i] + coef*time_series[j,i-lag]
                sum_of_coefs=sum_of_coefs+np.abs(coef)
            time_series[j,i]=(time_series[j,i] + add_gaussian_noise*np.random.normal(mu,sigma))/(sum_of_coefs)
    return time_series



def dataset3(len_of_timeseries,number_of_timeseries,coef_lag_list,noise_frequency=0,mu=0,sigma=1):
    
    if type(coef_lag_list)==int:
        coef_lag_list=[(1,coef_lag_list)]
    
    if type(coef_lag_list)==tuple:
        coef_lag_list=[coef_lag_list]
        
    if type(coef_lag_list)==list and type(coef_lag_list[0])==tuple:
        coef_lag_list=[coef_lag_list]*number_of_timeseries
        
    time_series=torch.empty((number_of_timeseries,len_of_timeseries)).normal_(mean=0,std=1)
    for j in range(number_of_timeseries):
        timeseries_coef_lag_list=coef_lag_list[j]
        max_lag=timeseries_coef_lag_list[0][0]
        for coef,lag in timeseries_coef_lag_list:
            if lag>max_lag:
                max_lag=lag
            
        for i in range(max_lag,len_of_timeseries):
            add_gaussian_noise=False
            sum_of_coefs=0
            if np.random.random()>(1-noise_frequency):
                add_gaussian_noise=True
            time_series[j,i]=0
            for coef,lag in timeseries_coef_lag_list:
                time_series[j,i]=time_series[j,i] + coef*time_series[j,i-lag]
                sum_of_coefs=sum_of_coefs+coef
            time_series[j,i]=torch.tanh((time_series[j,i] + add_gaussian_noise*np.random.normal(mu,sigma))/(sum_of_coefs))
    return time_series


def dataset4(len_of_timeseries,coef_lag_list,noise_frequency=0,mu=0,sigma=1):
    
    number_of_timeseries=2
    
    if type(coef_lag_list)==int:
        coef_lag_list=[(1,coef_lag_list)]
    
    if type(coef_lag_list)==tuple:
        coef_lag_list=[coef_lag_list]
        
    if type(coef_lag_list)==list and type(coef_lag_list[0])==tuple:
        coef_lag_list=[coef_lag_list]*number_of_timeseries
    
    time_series=torch.empty((number_of_timeseries,len_of_timeseries)).normal_(mean=0,std=1)
    max_lag=coef_lag_list[0][0][0]
    for j in range(number_of_timeseries):
            timeseries_coef_lag_list=coef_lag_list[j]
            for coef,lag in timeseries_coef_lag_list:
                if lag>max_lag:
                    max_lag=lag
                    
    for i in range(max_lag,len_of_timeseries):
        for j in range(number_of_timeseries):
                timeseries_coef_lag_list=coef_lag_list[j]
                add_gaussian_noise=False
                sum_of_coefs=0
                if np.random.random()>(1-noise_frequency):
                    add_gaussian_noise=True
                time_series[1-j,i]=0
                for coef,lag in timeseries_coef_lag_list:
                    time_series[1-j,i]=time_series[1-j,i] + coef*time_series[j,i-lag]
                    sum_of_coefs=sum_of_coefs+coef
                time_series[1-j,i]=(time_series[1-j,i] + add_gaussian_noise*np.random.normal(mu,sigma))/(sum_of_coefs)
    return time_series



def dataset5(len_of_timeseries,number_of_timeseries,coef_lag_list,noise_frequency=0,mu=0,sigma=1):
        
    if type(coef_lag_list)==int:
        coef_lag_list=[(1,coef_lag_list)]
    
    if type(coef_lag_list)==tuple:
        coef_lag_list=[coef_lag_list]
        
    if type(coef_lag_list)==list and type(coef_lag_list[0])==tuple:
        coef_lag_list=[coef_lag_list]*number_of_timeseries
    
    time_series=torch.empty((number_of_timeseries,len_of_timeseries)).normal_(mean=0,std=1)
    max_lag=coef_lag_list[0][0][0]
    for j in range(number_of_timeseries):
            timeseries_coef_lag_list=coef_lag_list[j]
            for coef,lag in timeseries_coef_lag_list:
                if lag>max_lag:
                    max_lag=lag
                                        
    for i in range(max_lag,len_of_timeseries):

        timeseries_coef_lag_list=coef_lag_list[0]
        add_gaussian_noise=False
        sum_of_coefs=0
        if np.random.random()>(1-noise_frequency):
            add_gaussian_noise=True
        time_series[0,i]=0
        for coef,lag in timeseries_coef_lag_list:
            time_series[0,i]=time_series[0,i] + coef*time_series[0,i-lag]
            sum_of_coefs=sum_of_coefs+coef
        time_series[0,i]=(time_series[0,i] + add_gaussian_noise*np.random.normal(mu,sigma))/(sum_of_coefs)
                           
        for j in range(1,number_of_timeseries):
            timeseries_coef_lag_list=coef_lag_list[j]
            add_gaussian_noise=False
            sum_of_coefs=0
            if np.random.random()>(1-noise_frequency):
                add_gaussian_noise=True
            time_series[j,i]=0
            for coef,lag in timeseries_coef_lag_list:
                time_series[j,i]=time_series[j,i] + coef*time_series[0,i-lag]
                sum_of_coefs=sum_of_coefs+coef
            time_series[j,i]=(time_series[j,i] + add_gaussian_noise*np.random.normal(mu,sigma))/(sum_of_coefs)
    return time_series


def dataset6(len_of_timeseries,number_of_timeseries,coef_lag_list,noise_frequency=0,mu=0,sigma=1):
        
    if type(coef_lag_list)==int:
        coef_lag_list=[(1,coef_lag_list)]
    
    if type(coef_lag_list)==tuple:
        coef_lag_list=[coef_lag_list]
        
    if type(coef_lag_list)==list and type(coef_lag_list[0])==tuple:
        coef_lag_list=[coef_lag_list]*number_of_timeseries
    
    time_series=torch.empty((number_of_timeseries,len_of_timeseries)).normal_(mean=0,std=1)
    max_lag=coef_lag_list[0][0][0]
    for j in range(number_of_timeseries):
            timeseries_coef_lag_list=coef_lag_list[j]
            for coef,lag in timeseries_coef_lag_list:
                if lag>max_lag:
                    max_lag=lag
                                        
    for i in range(max_lag,len_of_timeseries):

        timeseries_coef_lag_list=coef_lag_list[0]
        add_gaussian_noise=False
        sum_of_coefs=0
        if np.random.random()>(1-noise_frequency):
            add_gaussian_noise=True
        time_series[0,i]=0
        for coef,lag in timeseries_coef_lag_list:
            time_series[0,i]=time_series[0,i] + coef*time_series[0,i-lag]
            sum_of_coefs=sum_of_coefs+coef
        time_series[0,i]=torch.tanh((time_series[0,i] + add_gaussian_noise*np.random.normal(mu,sigma))/(sum_of_coefs))
                           
        for j in range(1,number_of_timeseries):
            timeseries_coef_lag_list=coef_lag_list[j]
            add_gaussian_noise=False
            sum_of_coefs=0
            if np.random.random()>(1-noise_frequency):
                add_gaussian_noise=True
            time_series[j,i]=0
            for coef,lag in timeseries_coef_lag_list:
                time_series[j,i]=time_series[j,i] + coef*time_series[0,i-lag]
                sum_of_coefs=sum_of_coefs+coef
            time_series[j,i]=torch.tanh((time_series[j,i] + add_gaussian_noise*np.random.normal(mu,sigma))/(sum_of_coefs))
    return time_series


def dataset7(len_of_timeseries,noise_frequency=0,mu=0,sigma=1):
    
    time_series=torch.empty((5,len_of_timeseries)).normal_(mean=0,std=1)

    for t in range (6,len_of_timeseries):
        if np.random.random()>(1-noise_frequency):
            add_gaussian_noise=True
        else:
            add_gaussian_noise=False
        time_series[0,t]=(time_series[0,t-1] + 3*time_series[0,t-5])/4 + add_gaussian_noise*np.random.normal(mu,sigma)
        time_series[1,t]=1-time_series[0,t-2] + add_gaussian_noise*np.random.normal(mu,sigma)
        time_series[2,t]=time_series[3,t-4] + time_series[1,t-1] + add_gaussian_noise*np.random.normal(mu,sigma)
        time_series[3,t]=1-(2*time_series[2,t-4] + 5*time_series[4,t-1])/7 + add_gaussian_noise*np.random.normal(mu,sigma)
        time_series[4,t]=(1.2*time_series[4,t-4] + time_series[1,t-1])/2.2 + add_gaussian_noise*np.random.normal(mu,sigma)
        
    return time_series


def dataset8(len_of_timeseries,switch_threshold,noise_frequency=0,mu=0,sigma=1):
    time_series=torch.empty((4,len_of_timeseries)).normal_(mean=0,std=1)

    for t in range (6,len_of_timeseries):
        if np.random.random()>(1-noise_frequency):
            add_gaussian_noise=True
        else:
            add_gaussian_noise=False
        if (time_series[0,t-5])>switch_threshold:
            time_series[0,t]=(time_series[0,t-1] + time_series[0,t-3])/2 + add_gaussian_noise*np.random.normal(mu,sigma)
            time_series[1,t]=time_series[0,t-5] + add_gaussian_noise*np.random.normal(mu,sigma)
            time_series[2,t]=time_series[0,t-4] + add_gaussian_noise*np.random.normal(mu,sigma)
            time_series[3,t]=0.5*time_series[3,t-4] + 0.5*time_series[3,t-1] + add_gaussian_noise*np.random.normal(mu,sigma)
        else:
            time_series[0,t]=(time_series[0,t-1] + time_series[0,t-3])/2 + add_gaussian_noise*np.random.normal(mu,sigma)
            time_series[1,t]=time_series[3,t-2] + add_gaussian_noise*np.random.normal(mu,sigma)
            time_series[2,t]=time_series[3,t-4] + add_gaussian_noise*np.random.normal(mu,sigma)
            time_series[3,t]=0.5*time_series[3,t-4] + 0.5*time_series[3,t-1] + add_gaussian_noise*np.random.normal(mu,sigma)        

    return time_series


def dataset9(t):
    rm = Ising()
    rm.simulate(t)
    
    time_series=np.array(rm.config)
    time_series=torch.tensor(time_series)
    time_series=time_series.flatten(start_dim=1)
    time_series=time_series.T
    
    return time_series



def dataset10(len_of_timeseries,r,noise_frequency=0,sigma=1):
        
    time_series=torch.empty((3,len_of_timeseries)).uniform_(0.0001,0.9999)
    for i in range(5,len_of_timeseries):
        add_gaussian_noise=False
        if np.random.random()>(1-noise_frequency):
            add_gaussian_noise=True
        time_series[0,i]=r*time_series[0,i-3]*(1-time_series[0,i-3])
        time_series[0,i]=(time_series[0,i] + add_gaussian_noise*np.random.normal(0,sigma))
        
        time_series[1,i]=r*time_series[1,i-5]*(1-time_series[1,i-5])
        time_series[1,i]=(time_series[1,i] + add_gaussian_noise*np.random.normal(0,sigma))
        
        time_series[2,i]=(time_series[0,i-3] + time_series[1,i-5])/2 
        time_series[2,i]=(time_series[2,i] + add_gaussian_noise*np.random.normal(0,sigma))
        
    return time_series