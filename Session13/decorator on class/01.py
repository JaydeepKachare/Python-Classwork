from decorator import timer, debug 

class TimeWaster : 
    @debug
    def __init__(self,max_num):
        self.max_num = max_num

    @timer
    def waste_time(self,num_times) : 
        for i in range (num_times) : 
            sum = 0 

    
tw = TimeWaster(1000) 
tw.waste_time(1001)