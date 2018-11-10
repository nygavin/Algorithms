class Solution(object):
    def minNth(self, vals=[], ordinal=0):
    	print vals
    	min = [vals[0]]
    	position= 
    	val=0
    	for val in vals[1:]:
    		if val < vals[0]:
    			min.insert(0,val)
    			position+=1
    		else:
    			min.append(val)
    			
    	print min
    	print position
    	
    	if position == ordinal:
    		return vals[position]
    	elif position > ordinal:
    		return self.minNth(min[:position], ordinal)
    	return self.minNth(min[position+1:],ordinal-position-1)
	
a= Solution()

print(a.minNth([105,5,3,99,7,44,2,6], 3))# your code goes here
