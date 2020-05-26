import numpy as np
import pandas as pd
import sys
sys.path.append('..')
from config import config

def read_calendar():
    """
        Function to read files and return as pandas csv

        Inputs:
        -------
        None

        Outputs:
        --------
        calendar: pandas dataframe containing calendar database
    """
    calendar = pd.read_csv(config.inputs_path['calendar'], sep = ',', engine = 'python')
    calendar['date'] = pd.to_datetime(calendar.date)
    return calendar

def read_sample_submission():
    """
        Function to read files and return as pandas csv

        Inputs:
        -------
        None

        Outputs:
        --------
        sample_submission: pandas dataframe containing sample_submission database
    """
    sample_submission = pd.read_csv(config.inputs_path['sample_submission'], sep = ',', engine = 'python')
    return sample_submission

def read_sell_prices():
    """
        Function to read files and return as pandas csv

        Inputs:
        -------
        None

        Outputs:
        --------
        sell_prices: pandas dataframe containing sell_prices database
    """
    sell_prices = pd.read_csv(config.inputs_path['sell_prices'], sep = ',', engine = 'python')
    return sell_prices

def read_sales_train_validation():
    """
        Function to read files and return as pandas csv

        Inputs:
        -------
        None

        Outputs:
        --------
        sales_train_validation: pandas dataframe containing sales_train_validation database
    """
    sales_train_validation = pd.read_csv(config.inputs_path['sales_train_validation'], sep = ',', engine = 'python')
    return sales_train_validation

def read_files():
    """
        Function to read files and return as pandas csv

        Inputs:
        -------
        None

        Outputs:
        --------
        calendar: pandas dataframe containing calendar database
        sell_prices: pandas dataframe containing sell_prices database
        sales_train_validation: pandas dataframe containing sales_train_validation database
        sample_submission: pandas dataframe containing sample_submission database
    """
    calendar = read_calendar()
    sell_prices = read_sell_prices()
    sales_train_validation = read_sales_train_validation()
    sample_submission = read_sample_submission()
    return calendar, sell_prices, sales_train_validation, sample_submission