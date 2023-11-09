'''
Сокращения/Обозначения:
      gd_sto_083 - генератор дефектов (класс) по документу "СТО Газпром 2-2.4-083-2006", остальное - по аналогии
      calc_<дефект> - функция (метод класса) расчёта максимального размера дефекта
      Aa - Пора
      Ba - Включение
      Fc - Подрез


'''
import re

import numpy as np
import math
import random


class CalkDefects:
    '''
    Класс предназначен для расчёта допустимых дефектов
    '''

    #def __init__(self):
        #pass

    # определение критериев оценки согласно выбранному документу и типу контроля
    @staticmethod
    def define_criterions(doc, vt=False, rt=False, pt=False, mt=False, ut=False):
        '''
        Функция определяет критерии оценки согласно выбранному документу и типу контроля
        '''
        if doc == 'СТО Газпром 2-2.4-083-2006':
            if vt == True:
                return 'раздел 6, табл. 2, табл. 10 - 14'
            elif rt == True or pt == True or mt == True:
                return 'табл. 2'
            elif ut == True:
                return 'табл. 20, табл. 23'
            else:
                print(f'{doc} ошибка - define_criterions')
        elif doc == 'СТО Газпром 2-2.2-649-2012':
            if vt == True:
                return 'п. 5.4.1.2, табл. 5.19'
            elif rt == True:
                return 'п. 5.7.7 табл. 5.19, 5.20, 5.22'
            elif ut == True:
                return 'п. 5.7.8, табл. 5.21'
            elif pt == True or mt == True:
                return 'п. 5.7.16'
            else:
                 print(f'{doc} ошибка - define_criterions')
        elif doc == 'СТО Газпром 2-2.2-136-2007':
            if vt == True:
                return 'разд. 9, п. 9.3'
            elif pt == True or mt == True or ut == True or rt == True:
                return 'разд. 9, п. 9.4'
            else:
                print(f'{doc} ошибка - define_criterions')
        elif doc == 'СП 70.13330.2012':
            if vt == True:
                return 'п. 10.4.4, табл. 10.7'
            elif ut == True:
               return 'п. 10.4.9, 10.4.10, табл. 10.10'
            elif rt == True:
                return 'п. 10.4.8, 10.4.11, табл. 10.8, 10.9'
            elif mt == True or pt == True:
                return 'п. 10.4.13'
            else:
                print(f'{doc} ошибка - define_criterions')
        elif doc == 'ГОСТ 34347-2017':
            if vt == True:
                return 'п. 5.10.2'
            if rt == True:
                return 'п. 5.10.3'
            if ut == True:
                return 'нет критериев оценки УЗК'
            if pt == True or mt == True:
                # ссылка на документ с критериями
                return 'п. 7.8.3'
            else:
                print(f'{doc} ошибка - define_criterions')
        else:
            print('Документ не выбран')

    @staticmethod
    def calk_Aa(quality_level, thickness, doc, welding_method):
        '''
        Функция возвращает максимально допустимый размер пор
        '''
        # т.к. 'СТО Газпром 2-2.2-136-2007' ссылается на 'Газпром 2-2.4-083'
        if doc == 'СТО Газпром 2-2.4-083-2006' or doc == 'СТО Газпром 2-2.2-136-2007':
            if quality_level == "A":
                max_Aa=thickness * 0.1
                if max_Aa > 2:
                    max_Aa = 2
            elif quality_level == "B":
                max_Aa = thickness * 0.2
                if max_Aa > 2.5:
                    max_Aa = 2.5
            elif quality_level == "C":
                max_Aa = thickness * 0.2
                if max_Aa > 3:
                    max_Aa = 3
            else:
                max_Aa = 1.0
        elif doc == 'СТО Газпром 2-2.2-649-2012':
                if thickness < 3:
                    # если ручная дуговая
                    if welding_method == 'РД':
                        max_Aa=0.6
                    # если АДС и др. виды сварки
                    else:
                        max_Aa=0.5
                elif 3<=thickness<5:
                    if welding_method == 'РД':
                        max_Aa=0.8
                    else:
                        max_Aa=0.6
                elif 5<=thickness<8:
                    if welding_method == 'РД':
                        max_Aa=1.0
                    else:
                        max_Aa=0.8
                elif 8<=thickness<11:
                    if welding_method == 'РД':
                        max_Aa=1.2
                    else:
                        max_Aa=1.0
                elif 11<=thickness<14:
                    if welding_method == 'РД':
                        max_Aa=1.5
                    else:
                        max_Aa=1.2
                elif 14<=thickness<20:
                    if welding_method == 'РД':
                        max_Aa=2.0
                    else:
                        max_Aa=1.5
                elif 20<=thickness<25:
                    if welding_method == 'РД':
                        max_Aa=2.5
                    else:
                        max_Aa=2.0
                else:
                    max_Aa=1.0
        elif doc == 'СП 70.13330.2012':
            if 4<=thickness<=6:
                max_Aa = 0.8
            elif 6<thickness<8:
                max_Aa = 1.2
            elif 8<=thickness<10:
                max_Aa = 1.6
            elif 10<=thickness<12:
                max_Aa = 2.0
            elif 12<=thickness<14:
                max_Aa = 2.4
            elif 14<=thickness<16:
                max_Aa = 2.8
            elif 16<=thickness<18:
                max_Aa = 3.2
            elif 18<=thickness<20:
                max_Aa = 3.6
            else:
                max_Aa = 4.0
        elif doc == 'ГОСТ 34347-2017':
            if 2<=thickness<=3:
                max_Aa = 0.5
            elif 3<thickness<4:
                max_Aa = 0.6
            elif 4<=thickness<5:
                max_Aa = 0.7
            elif 5<=thickness<6:
                max_Aa = 0.8
            elif 6<=thickness<8:
                max_Aa = 1.0
            elif 8<=thickness<10:
                max_Aa = 1.2
            elif 10<=thickness<15:
                max_Aa = 1.5
            elif 15<=thickness<20:
                max_Aa = 2.0
            else:
                max_Aa = 2.5
        return float(max_Aa)

    @staticmethod
    def calc_Fc(doc):
        if doc != 'ГОСТ 34347-2017':
            lenght_Fa = random.randint(5, 20)
            return lenght_Fa

    def rt_sensitivity(self, thickness):
        '''
        Функция возвращает чувствительность контроля (по ГОСТ 7512),
        исходя из толщины сварного соединения
        '''
        S = thickness
        if S<=5:
            K = 0.1
        elif 5<S<=9:
            K = 0.2
        elif 9<S<=12:
            K = 0.3
        elif 12<S<=20:
            K = 0.4
        elif 20<S<=30:
            K = 0.5
        elif 30<S<=40:
            K = 0.6
        elif 40<S<=50:
            K = 0.75
        elif 50<S<=70:
            K = 1.0
        elif 70<S<=100:
            K = 1.25
        else:
            print('Ошибка rt_sensitivity')
        return K

    def rt_count_tapes(self, diameter, thickness):
        '''
        Функция определяет сxему просвечивания, исходя из диаметра свариваемых КСС,
        рассчитывает минимальное количество снимков согласно формулам (Приложнеие 4 ГОСТ 7512, табл. 1, 2),
        возвращает N снимков и фактическую чувствительность (K)
        '''
        D = diameter
        S = thickness
        join_length = float(D * math.pi)
        F = 5 # фокусное пятно Site X C3005
        d = D - 2*S
        m = d/D
        # на эллипс 5в (по ГОСТ 7512)
        if D <= 76:
            N_counts = 2
            K = 2*self.rt_sensitivity(thickness)
        # через 2 стенки 5г (по ГОСТ 7512)
        elif 76 < D <= 108:
            K = 2*self.rt_sensitivity(thickness)
            C = 2*F/K
            f = 0.5*(1.5*C*(1-m)-1)*D
            n = f/D
            p = math.sqrt(1 - 0.2 * ((2.6-(1/m))**2))
            # округляю в большую сторону
            N_counts = math.ceil(180/(math.degrees(math.asin(p*m)) + math.degrees(math.asin(p*m/(2*n+1)))))
        # через 1 стенку 5а (по ГОСТ 7512)
        elif D > 108:
            K = self.rt_sensitivity(thickness)
            C = 2*F/K
            f = 0.7*C*(1-m)*D
            n = f/D
            N_counts = math.ceil(180/(math.degrees(math.asin(0.7*m)) - math.degrees(math.asin(0.7*m/(2*n + 1)))))
        else:
            print('Неверный ввод - расчёт количества снимков')
        return N_counts, K

    def ut_select_converter(self, thickness):
        '''
        Функция возвращает угол и частоту пьезоэлектрического преобразователя (ПЭП)
        '''
        if 4 <= thickness < 8:
            piez_converter = 'П121-5.0-70'
        elif 8 <= thickness < 12:
            piez_converter = 'П121-5.0-65'
        elif 12 <= thickness:
            piez_converter = 'П121-2.5-65'
        else:
            piez_converter = 'None'
            print('Ошибка - выбор преобразователя')
        return piez_converter

    def ut_select_max_eq_area(self, doc, thickness, quality_level='A'):
        '''
        Функция возвращает значение максимально допустимой несплошности при УЗК
        '''
        max_eq_area = 0
        if 'Газпром' in doc:
            if 4 <= thickness < 6:
                if quality_level == 'А':
                    max_eq_area = 0.7
                else:
                    max_eq_area = 1.0
            elif 6 <= thickness < 8:
                if quality_level == 'А':
                    max_eq_area = 0.85
                else:
                    max_eq_area = 1.20
            elif 8 <= thickness < 12:
                if quality_level == 'А':
                    max_eq_area = 1.05
                else:
                    max_eq_area = 1.5
            elif 12 <= thickness < 15:
                if quality_level == 'А':
                    max_eq_area = 1.4
                else:
                    max_eq_area = 2.0
            elif 15 <= thickness < 20:
                if quality_level == 'А':
                    max_eq_area = 1.75
                else:
                    max_eq_area = 2.5
            elif 20 <= thickness < 26:
                if quality_level == 'A':
                    max_eq_area = 2.5
                else:
                    max_eq_area = 3.5
            elif thickness >= 26:
                if quality_level == 'A':
                    max_eq_area = 3.5
                else:
                    max_eq_area = 5.0
            else:
                print('По СТО Газпром 2-2.4-083-2006 при S<4 мм УК не проводится')
        elif doc == 'СП 70.13330.2012':
            if thickness < 6:
                print("По СП 70.13330.2012 при S<6 мм УК не проводится")
                max_eq_area = 0
            elif 6 <= thickness < 10:
                max_eq_area = 4
            elif 10 <= thickness < 20:
                max_eq_area = 6
            elif 20 <= thickness < 30:
                max_eq_area = 7
            else:
                max_eq_area = 7
        elif doc == 'ГОСТ 34347-2017':
            print("В ГОСТ 34347-2017 нет критериев оценки для УЗК, выберите другой документ")
            max_eq_area = 0
        else:
            print('Ошибка при выборе максимальной эквивалентной площади')
            max_eq_area = 0
        return max_eq_area



