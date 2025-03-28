def app(temp): # function which has value "temp"
    if temp < 78: # if temperature is less than 78
        print ("უჰ დავიწვით კაცო დაუწიე!") # print this text <--
    elif temp > 1000:  # else if temperature is more than 1000
        print ("ვიგუდები დაუწიე!") # print this text <--
    elif temp < -100:  # else if temperature is less than -100
        print ("ვაიმე ანტარქტიდაზე ვცხოვრობთ!")  # print this text <--
    else:
        print ("უი რა კაი სიგრეილეა!")  # print this text <--

# examples
print (app(12))
print (app(71))
print (app(82))
print (app(11))
print (app(112))
print (app(512552))
print (app(-134))
print (app(152))
print (app(914))
print (app(517))
print (app(9318))
print (app(74))
print (app(32))
print (app(61))
print (app(112))