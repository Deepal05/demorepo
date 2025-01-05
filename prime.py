#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

number = int(input("Enter a number to check if it's prime: "))


# In[2]:


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# In[3]:


def find_primes_up_to(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes


# In[4]:


def list_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


# In[5]:


api_key = "12345-abcdef-67890"


# In[6]:


try:
    divisor = int(input("Enter a divisor for calculation: "))
    result = 100 / divisor
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Division by zero is not allowed.")


# In[7]:


if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


# In[8]:


unused_variable = "This is not used anywhere"


# In[ ]:




