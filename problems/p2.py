#################################################

#Problem 2: Write an algorithm to find a substring in a string – do not use prebuilt python functions and regular expressions.

######################################################

def find_substring(s, subs):
    """
    Find substring in string given string s and substing sub. 
    
    Returns: starting index of substring in longer string. 
    """

    j = len(subs) # len of sub string 

    for ind in range(len(s)+1-j):
        S = s[ind:j+ind] 
        if S == subs:
            print(f"Substring '{S}' found at index {ind}")
            return ind
            

    

    
            
    
  
            
        
            



        
    


if __name__ == "__main__":

    example = "Greedy algorithms do not always yield optimal solutions, but for many problems they do. We shall first examine, in Section 16.1, a simple but nontrivial problem, the activity-selection problem, for which a greedy algorithm efficiently computes an optimal solution. We shall arrive at the greedy algorithm by first consider- ing a dynamic-programming approach and then showing that we can always make greedy choices to arrive at an optimal solution. Section 16.2 reviews the basic elements of the greedy approach, giving a direct approach for proving greedy al- gorithms correct. Section 16.3 presents an important application of greedy tech- niques: designing data-compression (Huffman) codes. In Section 16.4, we inves- tigate some of the theory underlying combinatorial structures called “matroids,” for which a greedy algorithm always produces an optimal solution. Finally, Sec- tion 16.5 applies matroids to solve a problem of scheduling unit-time tasks with deadlines and penalties."


    I = find_substring(example,"dynamic")






