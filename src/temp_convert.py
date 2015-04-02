def F_to_K(temp):
	return ((temp-32)*(5/float(9))) + 273.15

def K_to_C(temp):
	return (temp)-273.5

def F_to_K(temp):
	temp_k = F_to_K(temp)
	result = K_to_C(temp)
	return(result)
