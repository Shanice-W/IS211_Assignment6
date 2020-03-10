#!/usr/bin/env python
# coding: utf-8

# In[9]:


def convertCelsiusToKelvin(temp=float):
    try:
        x = temp + 273.15
    except TypeError:
        raise TypeError('Input should be a float ')
    return x


# In[10]:


def convertCelsiusToFahrenheit(temp=float):
    try:
        x = temp * (9.0/5.0) + 32
    except TypeError:
        raise TypeError('Input should be a float')
    return x


# In[11]:


def convertFahrenheitToCelsius(temp=float):
    try:
        x = (temp - 32) * (5.0/9.0)
    except TypeError:
        raise TypeError('Input should be a float')
    return x


# In[12]:


def convertFahrenheitToKelvin(temp=float):
    try:
        x = (temp + 459.67) * (5.0/9.0)
    except TypeError:
        raise TypeError('Input should be a float')
    return x


# In[13]:


def convertKelvinToCelsius(temp=float):
    try:
        x = temp - 273.15
    except TypeError:
        raise TypeError('Input should be a float')
    return x


# In[14]:


def convertKelvintoFahrenheit(temp=float):
    try:
        x = temp * (9.0/5.0) - 459.76
    except TypeError:
        raise TypeError('Input should be a float')
    return x

