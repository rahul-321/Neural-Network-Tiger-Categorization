import math

def genderThreshold(net):
        theta= - 4.5              
        if net>theta:
                return 1        #male
        else: 
                return -1

def getGender(g):
	if g == 1: return 'male'
	return 'female'

def ageThreshold(net):
        theta=50
        if net>theta:
                return 1        # adult
        else: 
                return -1
def getAge(a):
	if a == 1: return 'old'
	return 'young'

def speedThreshold(net):
        theta= -668
        if net<theta:
                return 1       # fast
        else: 
                return -1
def getSpeed(s):
	if s == 1: return 'fast'
	return 'slow'

def heightThreshold(net):
	if net < -678: return 1
	if net < -342: return 0
	return -1
		
def getHeight(h):
	if h == 1: return 'tall'
	if h == 0: return 'medium'
	return 'short'

def computeNet(inputs, weights):
        net = 0
        for i in range(len(inputs)):
                net = net + inputs[i]*weights[i]
        #print "NET:"
        #print net
        return net

def computeFNetBinary(net):
        f_net = 0
        if(net>0):
                f_net = 1
        if(net<0):
                f_net = -1
        return f_net

def computeFNetCont(net):
        f_net = 0
        f_net = (2/(1+math.exp(-net)))-1
        return f_net


def perceptron(desired, actual):
        return (desired-actual)

def widrow(desired, actual):
        return (desired-actual)

def adjustWeights(inputs, weights, last, binary, desired, rule):
        c = 1
        if(last):
                #print "COMPLETE"
                return  weights[:]
        current_input = inputs[0]
        inputs = inputs[1:]
        current_desired = desired[0]
        desired = desired[1:]
        if len(inputs) == 0:
                last = True
        net = computeNet(current_input, weights)
        if(binary):
                f_net = computeFNetBinary(net)
        else:
                f_net = computeFNetCont(net)
        #if rule == "hebb":
        #        r = hebb(f_net)
        if rule == "perceptron":
                r = perceptron(current_desired, f_net)
        #elif rule == "widrow":
        #        r = widrow(current_desired, net)
        del_weights = []
        for i in range(len(current_input)):
                x = (c*r)*current_input[i]
                del_weights.append(x)
                weights[i] = weights[i] + x
        #print("NEW WEIGHTS:")
        #print(weights)
        return adjustWeights(inputs, weights, last, binary, desired, rule)


initialWeightGender = [1]	#difference between length and breadth
initialWeightAge = [1]		#only length
initialWeightSpeed = [1,1]		#step and stride
initialWeightHeight = [1,1,1]	#output of gender and age and stride


inputs = [[7,5,20,10],[17,17,30,15],[15,15,20,9],[14,12,18,8],[8,8,20,9]]

desiredGender = [-1,1,1,-1,1]
desiredAge=[-1,1,1,1,-1]
desiredSpeed=[-1,1,-1,-1,-1]
desiredHeight=[-1,1,0,0,-1]	#0 indicates a medium


inputGender = []
for i in inputs:
	temp = [(i[0] - i[1])]
	inputGender.append(temp)
print('inputGender ', inputGender)

inputAge = []
for i in inputs:
	temp = [i[0]]
	inputAge.append(temp)
print('inputAge ', inputAge)
	
print("USING PERCEPTRON RULE:")

weieghtsPGender=adjustWeights(inputGender, initialWeightGender, False, True, desiredGender, "perceptron")

print(weieghtsPGender)

print('gender is', getGender(genderThreshold(computeNet([1.49], weieghtsPGender))))

weieghtsPAge=adjustWeights(inputAge, initialWeightAge, False, True, desiredAge, "perceptron")
print(weieghtsPAge)

print('It is', getAge(ageThreshold(computeNet([10], weieghtsPAge))))

#prepare input for speed
inputSpeed = []
for i in inputs:
	inputSpeed.append(i[2:])
print('inputSpeed ', inputSpeed)

weieghtsPSpeed=adjustWeights(inputSpeed, initialWeightSpeed, False, True, desiredSpeed, "perceptron")
print(weieghtsPSpeed)
print('it was moving', getSpeed(speedThreshold(computeNet([28, 13], weieghtsPSpeed))))


#prepare input for height:
inputHeight = []
for i in range(len(inputs)):
	gender = genderThreshold(computeNet(inputGender[i], weieghtsPGender))
	age = ageThreshold(computeNet(inputAge[i], weieghtsPAge))
	temp = [gender, age, inputs[i][2]]
	inputHeight.append(temp)
print('inputHeight ', inputHeight)

weieghtsPHeight=adjustWeights(inputHeight, initialWeightHeight, False, True, desiredHeight, "perceptron")      
print(weieghtsPHeight)
print("It's height is", getHeight(heightThreshold(computeNet([-1, 1, 28], weieghtsPHeight))))
