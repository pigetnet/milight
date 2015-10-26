#!/usr/bin/python
import milight
import sys

ip = sys.argv[1]
id = int(sys.argv[2])
state = sys.argv[3]

print ip
print id
print state

controller = milight.MiLight({'host': ip, 'port': 8899})
light = milight.LightBulb(['rgbw'])

if state == "on":
    controller.send(light.on(id))
    print "Turning on"+str(id)

if state == "off":
    controller.send(light.off(id))
    print "Turning off"+str(id)

if state == "dim":
    controller.send(light.brightness(50,id))
    print "Turning dim"+str(id)

if state == "bright":
    controller.send(light.brightness(100,id))
    print "Turning bright"+str(id)
