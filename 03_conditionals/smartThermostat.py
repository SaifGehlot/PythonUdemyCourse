#deviceStatus = False
#temperature = 12
#if deviceStatus | (temperature > 35) :
#    print("High Temperature Alert!")    
#else:
#    print("Temperature is Normal")

device_status = ""
temperature = 38

if device_status == "Active" :
    if (temperature > 35) :
        print("High Temperature Alert!")
    else:
        print("Temperature in Normal")    
else:
    print("Device is offline")
