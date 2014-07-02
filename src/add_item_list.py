#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 1, 2014

@author: anroco

How I can add items to a list created in python?

¿Como puedo agregar elementos a una lista creada en python?
'''

#create a list with string data
lista = ['b', 'c', 'e', 'f']
print (lista)

#add a new item to the end of the list
lista.append('g')
print (lista)

#add an item to a particular index
lista.insert(2, 'd')
print (lista)

#add an item to the top of the list
lista.insert(0, 'a')
print (lista)
