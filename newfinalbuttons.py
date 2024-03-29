
# mattland ---> ariland
# "Matthew rates confirmed"???

#file to save data
outfile = open("C:\Users\keira\OneDrive\Desktop\mpscripts\newfinalbuttons.py", "w")
#importing libraries
import wpf
from System.Windows import MessageBox
from System.Windows import Application, Window
import sys
sys.path.append(r"c:\Python27\Lib\site-packages")
sys.path.append(r"c:\Python27\Lib")
import clr
clr.AddReference("System.Windows.Forms")
import MissionPlanner
clr.AddReference("MAVLink")
from System.Windows.Forms import Application, Form, Button, MessageBox
from System.Drawing import Point
import MAVLink



#Assigns buttons (variable)
f = Form()
battery_1 = Button()
battery_2 = Button()
battery_3 = Button()
battery_4 = Button()
battery_5 = Button()
battery_6 = Button()
battery_7 = Button()
battery_8 = Button()
pickup_1 = Button()
pickup_2 = Button()
pickup_3 = Button()
dropoff_1 = Button()
dropoff_2 = Button()
dropoff_3 = Button()
pickup_1grnd = Button()
pickup_2grnd = Button()
pickup_3grnd = Button()
dropoff_1grnd = Button()
dropoff_2grnd = Button()
dropoff_3grnd = Button()
cwturns = Button()
ccwturns = Button()
ccwturns = Button()
ariland = Button()
regland = Button()
save1 = Button()

#Establishes location
battery_1.Location = Point(0, 0)
battery_2.Location = Point(0, 25)
battery_3.Location = Point(0, 50)
battery_4.Location = Point(0, 75)
battery_5.Location = Point(0, 100)
battery_6.Location = Point(0, 125)
battery_7.Location = Point(0, 150)
battery_8.Location = Point(0, 175)
pickup_1.Location = Point(75, 0)
pickup_2.Location = Point(150, 0)
pickup_3.Location = Point(225, 0)
dropoff_1.Location = Point(75, 25)
dropoff_2.Location = Point(150, 25)
dropoff_3.Location = Point(225, 25)
pickup_1grnd.Location = Point(75, 50)
pickup_2grnd.Location = Point(150, 50)
pickup_3grnd.Location = Point(225, 50)
dropoff_1grnd.Location = Point(75, 75)
dropoff_2grnd.Location = Point(150, 75)
dropoff_3grnd.Location = Point(225, 75)
cwturns.Location = Point(300, 0)
ccwturns.Location = Point(300, 25)
ariland.Location = Point(300, 75)
regland.Location = Point(300, 50)
save1.Location = Point(75, 100)

#Actual string (what the button actually looks like)
battery_1.Text = "Bat 1"
battery_2.Text = "Bat 2"
battery_3.Text = "Bat 3"
battery_4.Text = "Bat 4"
battery_5.Text = "Bat 5"
battery_6.Text = "Bat 6"
battery_7.Text = "Bat 7"
battery_8.Text = "Bat 8"
pickup_1.Text = " WB Pickup"
pickup_2.Text = "MK Pickup"
pickup_3.Text = "MM Pickup"
dropoff_1.Text = "WB Dropoff"
dropoff_2.Text = "MK Dropoff"
dropoff_3.Text = "MM Dropoff"
pickup_1grnd.Text = "GPWB"
pickup_2grnd.Text = "GPMK"
pickup_3grnd.Text = "GPMM"
dropoff_1grnd.Text = "GDWB"
dropoff_2grnd.Text = "GDMK"
dropoff_3grnd.Text = "GDMM"
cwturns.Text = "CW"
ccwturns.Text = "CCW"
save1.Text = "Save"
regland.Text = "Regular"
ariland.Text = "Arinze"

#save data and close the file
def save(sender, args):
                outfile.close()
                print("Saved")
 #change turning rate of clockwise
def clockwise(sender, args):
                Script.ChangeParam('CIRCLE_RATE',90)
 #change turning rate of ccw
def counterclockwise(sender, args):
                Script.ChangeParam('CIRCLE_RATE',-90)
 #log coordinates
def logger(sender, args):
                print("{} Coords: {:12.10f}, {:12.10f}".format(sender.Text, cs.lat, cs.lng))
                outfile.writelines("{} Coords: \t{:12.10f}, {:12.10f}\n".format(sender.Text, cs.lat, cs.lng))
 #landing params for arinze
def arilandfun(sender, args):
                Script.ChangeParam('LAND_ALT_LOW',600)
                Script.ChangeParam('LAND_SPEED',20)
                Script.ChangeParam('LAND_SPEED_HIGH',250)
                print("Arinze rates confirmed")
 #regular landing params
def reglandfun(sender, args):
                Script.ChangeParam('LAND_ALT_LOW',300)
                Script.ChangeParam('LAND_SPEED',75)
                Script.ChangeParam('LAND_SPEED_HIGH',300)
                print("Regular rates confirmed")
 #change battery params
def batt_change(sender, args):
                print("Testing!")
                batt_types = {'Bat 1':4120, 'Bat 2': 4100, 'Bat 3': 4010, 'Bat 4': 3970, 'Bat 5':3500, 'Bat 6': 3358, 'Bat 7': 3588, 'Bat 8': 3500}
                print("Changing {}, Max MA: {}".format(sender.Text, batt_types[sender.Text]))
                Script.ChangeParam('BATT_CAPACITY', batt_types[sender.Text])
                MAV.doCommand(MAVLink.MAV_CMD.BATTERY_RESET, 1, 100, 0, 0, 0, 0, 0)
cont = True
while cont:
        battery_1.Click += batt_change
        battery_3.Click += batt_change
        battery_2.Click += batt_change
        battery_4.Click += batt_change
        battery_5.Click += batt_change
        battery_6.Click += batt_change
        battery_7.Click += batt_change
        battery_8.Click += batt_change
        cwturns.Click += clockwise
        ccwturns.Click += counterclockwise
        pickup_1.Click += logger
        pickup_2.Click += logger
        pickup_3.Click += logger
        dropoff_1.Click += logger
        dropoff_2.Click += logger
        dropoff_3.Click += logger
        pickup_1grnd.Click += logger
        pickup_2grnd.Click += logger
        pickup_3grnd.Click += logger
        dropoff_1grnd.Click += logger
        dropoff_2grnd.Click += logger
        dropoff_3grnd.Click += logger
        mattland.Click += mattlandfun
        regland.Click += reglandfun
        save1.Click += save
        f.Controls.Add(battery_1)
        f.Controls.Add(battery_2)
        f.Controls.Add(battery_3)
        f.Controls.Add(battery_4)
        f.Controls.Add(battery_5)
        f.Controls.Add(battery_6)
        f.Controls.Add(battery_7)
        f.Controls.Add(battery_8)
        f.Controls.Add(pickup_1)
        f.Controls.Add(pickup_2)
        f.Controls.Add(pickup_3)
        f.Controls.Add(dropoff_1)
        f.Controls.Add(dropoff_2)
        f.Controls.Add(dropoff_3)
        f.Controls.Add(pickup_1grnd)
        f.Controls.Add(pickup_2grnd)
        f.Controls.Add(pickup_3grnd)
        f.Controls.Add(dropoff_1grnd)
        f.Controls.Add(dropoff_2grnd)
        f.Controls.Add(dropoff_3grnd)
        f.Controls.Add(cwturns)
        f.Controls.Add(ccwturns)
        f.Controls.Add(save1)
        f.Controls.Add(ariland)
        f.Controls.Add(regland)
        f.ShowDialog()
#Reg Height is 3m Land speed high is 300 cm/sec land speed is 75 
#Arinze Height is 5m Land Speed High and land speed is undecided
