#Desmos Grap of data for reference
#https://www.desmos.com/calculator/geuuzegkqu
coordinates = [[0,100],[2,110],[4,200],[6,280],[8,400],[10,590]]
degree = 2 #define the degree of the polynomial
coeffecients = [] #initialize an empty list of coeffecients
for x in range(degree+1): #make all the coeffecients 1, add 1 to the power to account for vertical shift
    coeffecients.append(1) #make it one
for epoch in range(50000): #adjust the values 50000 times
    lr = 0.0001 #learning rate basically dialates how much you need to change each coeffecient by, lets say your error is 100 and you are adjusting the constant 100 might be too much so you need to scale your changes down
    for coordinate in coordinates: # cycle through coordinates
        x = coordinate[0] #define the x coordinate
        y = coordinate[1] #define the y coordinate
        power = len(coeffecients)-1 #find the degree of the polynomial (i know it's defined on line 2, but I'm too lazy to change)
        guess = 0 #make the current predicted value 0
        for index in range(len(coeffecients)): #cycle through the coeffecients in order to make the guess
            guess += coeffecients[index]*(x**power) #basically calculating each term of the polynomial here. coeffecient*(x)^power. when the constant is reached the power is 0 so the term is just the coeffecient
            power -= 1 #subtract 1 from the power as terms decrease in degree from left to right
        error = y-guess #find error, the actual value minus the prediction (same thing in PID loop)
        power = len(coeffecients)-1 #find the degree of the polynomial (i know it's defined on line 2, but I'm too lazy to change)
        for index in range(len(coeffecients)-1):  #cycle through the coeffecients besides the last one which the constant term
            coeffecients[index] = coeffecients[index]+(x**power)*(error*lr) #okay so calc stuff
            # This example below is for linear regression (y=mx+b), the same can be applied for quadratic as well
            # The general form for the change of a coeffecient is:
            # coeffecient + deltaCoeffecient
            # So we know we need to change this given coeffecient by a certain value called deltaCoeffecient
            # deltaCoeffecient must have the following 3 qualities
            # - Proportional to the error, so we must multiply by the error. This is done so if the error is negative, the value of the coeffecient moves down
            # - Scaled down by learning rate (refer to line 7)
            # - Must account for how much this the given coeffecient effects the function
            # The effect a coeffectient has on a function can be calculated via the paritial derivative
            # It makes sense that the paritial derivative of y = mx+b, if I change m by some amount the output is dialated by x, and always will be
            # For the equation mx+b, you find the derivative with respect to m. This will give you x. (Refer to power rule)
            # So we have three things that dictate how much the this given coeffecient changes by
            # - learning rate
            # - Error
            # - The paritial derivative (AKA if I change this value, how much does the whole function change by)
            # With ALLL of this mind, we can come up with:
            # m = m+(x*error*learning_rate)
            power -= 1 #subtract power by one because of paritial derivative pattern.
            # If have have ax^2 + bx + c, the paritial derivative of the ax^2 with respect to a is x^2, thus in the first run of loop the power is 2
            # 2nd time around the paritial derivative of the b with respect to b is x, thus in the second run of the loop the power is 1
            # The constant is ommited in the calculation as it is constant and the paritial derivative of any constant is 0, using the constant here would result in the constant staying the same throughout training as deltaCoeffecient has a factor 0 resulting in no change.
        coeffecients[-1] = coeffecients[-1]+(error*lr) #Adjust the constant by using error*lr. Still uses the 3 qualities since the coeffecient doesn't effect the function in a way that it is dependent on the input 
print coeffecients #print and DAB when you see the results 
