if __name__ == '__main__':  # Check if script is run directly
    n = int(input())  # Read number of elements
    arr = list(map(int, input().split()))  # Read list of integers
    
    maxscore = max(arr)  # Find the maximum value
    filteredlist = [score for score in arr if score is not maxscore]  # List of values not the same object as maxscore (should use != for value)
    runnerscore = max(filteredlist)  # Find the runner-up (second highest) value
    print(runnerscore)  # Print the runner-up score