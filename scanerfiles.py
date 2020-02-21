#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import os.path
import sys
import cv2
import numpy as np
import re
from pprint import pprint
import time
from dataclasses import dataclass


@dataclass
class FaceCoord:
    x0:int = 1
    y0:int = 1
    x1:int = 1
    y1:int = 1
    w:int = 1
    h:int = 1


@dataclass
class GlassesCoord:
    x0:int = 1
    y0:int = 1
    x1:int = 1
    y1:int = 1
    w:int = 1
    h:int = 1

# /home/baron/coding/vkgroup2/club_154390899
# /home/baron/coding/vkgroup2/club_114537164
scaner_files = '/home/baron/coding/vkgroup2/club_154390899' # откуда берутся файлы
saving_dir = '/home/baron/cv_images'                       # куда сохранять
good_files = '' # для прошедших проверку
bad_files = '' # для не прошедших проверку
home_dir = os.getcwd()                                     # директория проекта

image_list = list()

def rename_files(file_list, path):
    for i, name in enumerate(file_list):
        file_list[i] = path+'/'+name


def files_selection(file_list):
    temp_list = list(file_list)
    file_list.clear()
    for name in temp_list:
        temp = name.strip().split('.')
        if temp[1] == 'jpg' or temp[1] == 'jpeg' or temp[1] == 'png':
            file_list.append(name)
    del temp_list


def showimage(image, name = 'photo', save_path = '.', save = False, show = True, key = 1000):
    if save:
        cv2.imwrite(save_path, imagee)
    if show:
        cv2.imshow(name, image)
        cv2.waitKey(key)
        cv2.destroyAllWindows()
    


def find_faces(file_list, good_files, bad_files):
    FACE = False
    EYE = False
    PROF = False
    SMILE  = False
    FACE_EYE = False
    FACE_SMILE = False
    KEY = None
    
    GRAY = None
    faces = None
    eyes = None
    smile = None
    
    face_coord = list()
    
    # получаю каскады
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
    profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    eyeglasses_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
    
    # перебор изображений из списка
    for original in file_list:
        print('='*40)
        print(original)
        face_coord.clear() # оччищаю список с координатами лиц
        # устанавливаю флаги в начальное состояние
        FACE = False
        EYE = False
        FACE_SMOLE = False
        
        if KEY == 'q':
            sys.exit()
        
        # загрузка фото
        image = cv2.imread(original)
        GRAY = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # получаю все лица
        faces = face_cascade.detectMultiScale( GRAY,
                                               scaleFactor  =  1.1,
                                               minNeighbors =  2,
                                               minSize      = (20, 20) )
        
        # получаю координаты лиц если они обнаружены
        # прорисовка квадратов обнаруженых лиц
        if len(faces) > 0:
            FACE = True # флаг обнаруженных лиц, лицо обнаружено
            for (x,y,w,h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (255, 100, 30), 2)
                face_coord.append(FaceCoord(x, y, x+w, y+h, w, h)) # сохраняю координаты для дальнейшего использования
        else:
            FACE = False
            print('Лиц на изображении не обнаружено')
            continue
        
        # обнаружение глаз и улыбок на лицах, если они есть
        if FACE == True:
            
            # глаза
            eyes = eye_cascade.detectMultiScale( GRAY,
                                                 scaleFactor  =  1.1,
                                                 minNeighbors =  2,
                                                 minSize      = (10, 10) )
            
            # улыбка
            smile = eye_cascade.detectMultiScale( GRAY,
                                                  scaleFactor  =  1.1,
                                                  minNeighbors =  1,
                                                  minSize      = (8, 8) )
            
            # получаю координаты глаз если они обнаружены
            if len(eyes) > 0:
                # получаю координаты глаз
                for (x,y,w,h) in eyes:
                    for data in face_coord:
                        # проверяю находятся ли координаты внутри координат лица
                        if x > data.x0 and (x+w) < data.x1 and y > data.y0 and (y+h) < data.y1:
                            EYE = True
                            cv2.rectangle(image, (x, y), (x+w, y+h), (10, 10, 255), 2)
                        else:
                            print('Глаза на лицах не удалось обнаружить')
            
            # получаю координаты улыбок если они обнаружены
            if len(smile) > 0:
                print('Всего улыбок: ', len(smile))
                # получаю координаты улыбок
                for (x,y,w,h) in smile:
                    for data in face_coord:
                        # проверяю находятся ли координаты внутри координат лица
                        if x > data.x0 and (x+w) < data.x1 and y > data.y0 and (y+h) < data.y1:
                            FACE_SMILE = True
                            cv2.rectangle(image, (x, y), (x+w, y+h), (10, 255, 10), 2)
                        else:
                            print('Улыбки на лицах не удалось обнаружить')
        
        
        if EYE or FACE_SMILE:
            KEY = showimage(image, key = 1000)
            FACE = False
        print('='*40)
        print()
    
    
    
    
    
    
    
    
    
    
    
    
    


if __name__ == '__main__':
    
    os.chdir(saving_dir)
    os.makedirs('good', exist_ok = True)
    os.makedirs('bad', exist_ok = True)
    os.chdir('good')
    good_files = os.getcwd()
    os.chdir('..')
    os.chdir('bad')
    bad_files = os.getcwd()
    os.chdir(scaner_files)
    image_list = os.listdir()
    os.chdir(home_dir)
    
    print('Home dir:', home_dir)
    print('Scaner dir:', scaner_files)
    print('Saving dir:', saving_dir)
    print('Good dir:', good_files)
    print('Bad dir:', bad_files)
    files_selection(image_list)
    rename_files(image_list, scaner_files)
    find_faces(image_list, 0, 0)
    
    
    
    
    
    
    
    










