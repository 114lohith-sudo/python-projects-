#tuple


#list are slow
#you use tuple

#tuple
#packing
address=(23,"something","something2","something3",11232311)
print(address)
#unpacking tuple
houseno,street,city,country,postalcode=address
print(houseno)
print(city)

#print only country
print(address[3])

#print city and country
print(address[2:4])

#this is a tuple --> charecter.pos(xpos,ypos)