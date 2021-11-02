import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
def FIS(qual, ser, ti, d, s):
    quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
    service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
    time = ctrl.Antecedent(np.arange(7, 23, 1), 'time')
    day = ctrl.Antecedent(np.arange(2, 9, 1), 'day')
    size = ctrl.Antecedent(np.arange(1, 13, 1), 'size')

    tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

    quality.automf(3)
    quality['average'] = fuzz.trimf(quality.universe, [2, 5, 8])
    service.automf(3)
    service['average'] = fuzz.trimf(service.universe, [1, 5, 9])
    time['breakfast'] = fuzz.trimf(time.universe, [7, 7, 11])
    time['lunch'] = fuzz.trimf(time.universe, [10, 13, 16])
    time['dinner'] = fuzz.trimf(time.universe, [15, 18, 22])
    day['weekdays'] = fuzz.trapmf(day.universe, [1, 1, 5, 5])
    day['weekends'] = fuzz.trapmf(day.universe, [5, 6, 8, 8])
    size['small'] = fuzz.trimf(size.universe, [1, 1, 5])
    size['medium'] = fuzz.trimf(size.universe, [4, 7, 9])
    size['large'] = fuzz.trimf(size.universe, [8, 12, 12])
    tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
    tip['medium'] = fuzz.trimf(tip.universe, [5, 13, 20])
    tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

    r1 = ctrl.Rule(service['poor'] & quality['poor'], tip['low'])
    r2 = ctrl.Rule(service['poor'] & quality['average'] & time['breakfast'], tip['low'])
    r3 = ctrl.Rule(service['average'] & quality['average'] & time['breakfast'], tip['medium'])
    r4 = ctrl.Rule(service['poor'] | service['average'] & quality['average'] | quality['good']
    & time['lunch'] | time['dinner'], tip['medium'])
    r5 = ctrl.Rule(service['average'] & quality['average'] & time['breakfast'], tip['medium'])
    r6 = ctrl.Rule(service['good'] & quality['average'] | quality['good'] & time['lunch'] |
    time['dinner'], tip['high'])
    r7 = ctrl.Rule(service['poor'] & quality['average'] | quality['good'] & size['large'],
    tip['medium'])
    r8 = ctrl.Rule(service['good'] & quality['average'] | quality['good'] & size['medium']
    | size['large'], tip['high'])
    r9 = ctrl.Rule(service['poor'] & quality['poor'] & size['medium'] | size['large'], tip['low'])
    r10 = ctrl.Rule(service['poor'] & quality['average'] | quality['good'] & size['small']
    & day['weekdays'], tip['medium'])
    r11 = ctrl.Rule(service['average'] & quality['average'] | quality['good'] & size['small']
    & day['weekdays'], tip['high'])
    r12 = ctrl.Rule(service['average'] & quality['average'] | quality['good'] & size['small']
    & day['weekends'], tip['medium'])
    r13 = ctrl.Rule(service['average'] & quality['average'] | quality['good'] & size['medium']
    | size['large'] & day['weekends'], tip['medium'])
    r14 = ctrl.Rule(service['average'] & quality['average'] | quality['good'] & size['medium']
    | size['large'] & day['weekends'], tip['medium'])
    r15 = ctrl.Rule(service['good'] & quality['average'] | quality['good'] & size['medium']
    | size['large'] & day['weekends'], tip['high'])

    tipping_ctrl = ctrl.ControlSystem([r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15])
    tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

    tipping.input['quality'] = qual
    tipping.input['service'] = ser
    tipping.input['time'] = ti
    tipping.input['size'] = s
    tipping.input['day'] = d

    tipping.compute()
    return tipping, tip

