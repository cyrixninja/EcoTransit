import calcdistance as calc

#References :
# https://8billiontrees.com/carbon-offsets-credits/how-much-co2-does-a-car-emit-per-mile/#:~:text=CO2%20emissions%20can%20also,of%20CO2%20per%20km

def diesel_car(noofpassenger,origin,destination):
    distance = calc.main(origin,destination)
    emissiongms = (distance*171)/noofpassenger
    emissionkg = round((emissiongms/1000),2)
    if emissionkg > 1:
        return str(emissionkg) + " Kg of CO2 per Person "
    else:
        return str(emissiongms) + " G of CO2 per Person "

def petrol_car(noofpassenger,origin,destination):
    distance = calc.main(origin,destination)
    emissiongms = (distance*192)/noofpassenger
    emissionkg = round((emissiongms/1000),2) 
    if emissionkg > 1:
        return str(emissionkg) + " Kg of CO2 per Person "
    else:
        return str(emissiongms) + " G of CO2 per Person "
    
def motorcycle(noofpassenger,origin,destination):
    distance = calc.main(origin,destination)
    emissiongms = (distance*103)/noofpassenger
    emissionkg = round((emissiongms/1000),2)
    if emissionkg > 1:
        return str(emissionkg) + " Kg of CO2 per Person "
    else:
        return str(emissiongms) + " G of CO2 per Person "

def bus(noofpassenger,origin,destination):
    distance = calc.main(origin,destination)
    emissiongms = (distance*105)/noofpassenger 
    emissionkg = round((emissiongms/1000),2)
    if emissionkg > 1:
        return str(emissionkg) + " Kg of CO2 per Person "
    else:
        return str(emissiongms) + " G of CO2 per Person "








