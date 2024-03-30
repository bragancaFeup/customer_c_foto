# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:12:26 2024

@author: braga
"""

# #%%
# from classes.class_horario import Class_horario
# from classes.horarioForm import HorarioForm

  
# # # Creates a Class_horario
# # HorarioForm.read('../data/' 'horario.db')
# # teste = HorarioForm('None','2021/05/16 11:20:30','t1','p1','uc1','s1','obs')
# # #code,diahora,cod_turma,cod_prof,cod_uc,cod_sala,obs
# # HorarioForm.insert(getattr(teste, HorarioForm.att[0]))
# # print(HorarioForm.current())
# # print(teste)

# Class_horario.read('./data/' 'horario.db')

# print(Class_horario.lst)

# for k in Class_horario.lst:
#     evento = Class_horario.obj[k]
#     print (evento)
    
# HorarioForm.reset()
# ho = HorarioForm("None", Class_horario, "2024-03-04", 8, 11)

# mat = ho.semanaTree

# #%%
# from classes.horario2Form import Horario2Form
# from classes.class_horario import Class_horario
# xx=Horario2Form("None", Class_horario, "2024-03-04", 8, 11)

# date = xx.str2datetimeDiaHora("2024/12/13 10:11:12")
# print (date,type(date))

# import datetime as datetime

# x = datetime.datetime(date.year, date.month, date.day,date.hour)
# print (x,type(x))

# print(x.hour,type (x.hour))

# #%%
# Class_horario.read('./data/' 'horario.db')
#%%
from classes.class_horario import Class_horario
from classes.horario2Form import Horario2Form

Class_horario.read('./data/' 'horario.db')

def gerah(sbl,diacalen):
    sbl.reset()
    print(diacalen)
    sbl("None", Class_horario, diacalen, 9, 12)
    objh = sbl.obj[sbl.lst[0]]
    return objh


from datetime import datetime
from classes.class_horario import Class_horario
from classes.horario2Form import Horario2Form

cname = "Horario2Form"
diacalen="2024-03-14 10:00:00"

#print (sbl.lst)
# print(sbl.obj[sbl.lst[0]].semanaTree)

#objh = sbl.obj[sbl.lst[0]]
# index = 0
# for linha in objh.semanaTree:
#     if index >= objh.horaIni and index <= objh.horaFim:
#         print (linha)
#     index +=1

#print (objh.selectedDiaHora)

sbl = eval("Horario2Form")
objh = gerah(sbl,diacalen)

print("eventbydiahora")
#print(objh.eventsbydiahora("2024-03-04 10:00:00"))
for xx in objh.eventsdiahseleted:
    print(xx)

#print(objh.colunasdia)

#for c in range(7):
# c=1
# for l in range(24):
#     print(objh.semanaTree[l][c])

