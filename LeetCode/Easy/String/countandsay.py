def countAndSay(self, n: int) -> str:
        
        # base case: if n is 1, return "1"
        if n == 1:
            return "1"
        
        # recursive case: get answer for (n-1) and then count and say the answer for (n-1)
        else:
            
            # get answer for (n-1)
            prev = self.countAndSay(n-1)

            # initialize empty string for count and say answer for (n-1)
            count_and_say = ""
            
            # initialize the counter to 1, since there is at least 1 digit
            counter_num = 1
            
            # loop through the numbers in the (n-1) answer
            for i in range(len(prev)-1):
                
                # get the current number
                current_num = prev[i]
                
                # get the next number
                next_num = prev[i+1]
                
                # if both are the same, update the counter for this specific number
                if current_num == next_num:
                    counter_num += 1
                
                # if a new number appears, update the count and say string
                else:
                    
                    # update the string with the number counted and the number itself
                    count_and_say += (str(counter_num)+str(current_num))
                    
                    # then reinitialize the new counter
                    counter_num = 1
                    
            count_and_say += (str(counter_num)+str(prev[len(prev)-1]))
            return count_and_say