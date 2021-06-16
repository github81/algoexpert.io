def moveElementToEnd(array, toMove):
    # Write your code here.
    
    lp = 0
    rp = len(array)-1
    while lp < rp:
    	if array[lp]==toMove:
    		if array[rp]==toMove:
    			rp-=1
    		else: 
    			array[lp], array[rp] = array[rp], array[lp]
    			lp+=1
    			rp-=1
    	else:
    		lp+=1
    		
    return array 
    	 
    	 