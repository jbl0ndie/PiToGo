import pifacecad
import bus_check

display = bus_check.check_bus() # call the check_bus function
print(display) # to console, for debug

cad = pifacecad.PiFaceCAD() # instantiate the pifacecad object

cad.lcd.backlight_on() # fire up the backlight

cad.lcd.write(str(display)) # fingers crossed

#~ listener = pifacecad.SwitchEventListener(chip=cad)
#~ 
#~ for i in range(8):
    #~ listener.register(i, pifacecad.IODIR_FALLING_EDGE, update_pin_text)
#~ listener.activate()
