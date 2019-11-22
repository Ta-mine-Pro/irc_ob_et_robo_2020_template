#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Direction, Color
import time

#モーター・センサー類の設定
Right = Motor(Port.B)
Left = Motor(Port.C, Direction.COUNTERCLOCKWISE) #Mモーター使用のため正の速度方向を逆に設定
CS = ColorSensor(Port.S1)
TS = TouchSensor(Port.S2)
US = UltrasonicSensor(Port.S3)
GS = GyroSensor(Port.S4)

#各種関数の定義
class My():
    
    #モーターの角度をAngle度にリセット
    def Reset(Angle):
        Right.reset_angle(Angle)
        Left.reset_angle(Angle)
    
    #モーターをそれぞれ速度Right_Speed、Left_Speedで回転
    def Run(Right_Speed, Left_Speed):
        Right.run(Right_Speed)
        Left.run(Left_Speed)
    
    #変数Reflectionの値を境目にライントレース
    def LineTrace(High_Power, Low_Power):
        if CS.reflection() > Reflection:
            My.Run(High_Power, Low_Power)
        else:
            My.Run(Low_Power, High_Power)

#プログラム
