class Solution:

    # Function to find the maximum obtainable value by cutting the rod
    def cutRod(self, price, n):

        # Create a list to store the maximum obtainable value for each length of rod
        val = [0]*(n+1)

        # Iterate through each length of rod
        for i in range(1,n+1):

            # Initialize the maximum value to -1 for each length of rod
            max_val = -1

            # Iterate through each possible cut in the rod
            for j in range(i):

                # Calculate the maximum obtainable value by considering different cuts
                max_val = max(max_val, price[j] + val[i - j - 1])
                print(max_val)

            # Store the maximum obtainable value for the current length of rod
            val[i] = max_val

        # Return the maximum obtainable value for the given length of rod
        return val[n]

price = [1, 5, 8, 9, 10, 17, 17, 20]
N = 8

solution = Solution()
output = solution.cutRod(price, N)
print(output)
