"""
File: model.py
Author: Abid Jeem

In collaboration with Rihards and TAs

Models multiple cashiers.
"""

from cashier import Cashier
from customer import Customer
import random

class MarketModel(object):

    def __init__(self, lengthOfSimulation, averageTimePerCus,
                 probabilityOfNewArrival, numCashiers):
        self._probabilityOfNewArrival = probabilityOfNewArrival
        self._lengthOfSimulation = lengthOfSimulation
        self._averageTimePerCus = averageTimePerCus
        #self._cashiers = Cashier(1)
        self.cashiers_list = [Cashier(i) for i in range(1,numCashiers+1)]
        
   
    
    
    def runSimulation(self):
        """Run the clock for n ticks."""
        # Loop through each time tick in the simulation
        for currentTime in range(self._lengthOfSimulation):
            # Attempt to generate a new customer based on the probability of customer arrival
            customer = Customer.generateCustomer(
                self._probabilityOfNewArrival,
                currentTime,
                self._averageTimePerCus)

            # Check if a new customer is generated
            if customer is not None:
                # Determine the initial location of the customer randomly among available cashiers
                initialLocation = random.randint(0, len(self.cashiers_list) - 1)

                # Define left and right limits for selecting nearby cashiers, considering a range of 2 cashiers
                leftLimit = max(0, initialLocation - 2)
                rightLimit = min(len(self.cashiers_list) - 1, initialLocation + 2)

                # Initialize variables to track the shortest queue length and distance
                shortestQueueLength = 100000  # Set to a large initial value
                shortestQueueDistance = 10000  # Set to a large initial value
                shortestQueueCashier = None

                # Iterate through cashiers within the specified boundaries
                for cashier in self.cashiers_list[leftLimit:rightLimit + 1]:
                    # Get the current queue length and the distance from the customer's initial location
                    queueLength = cashier.customersInLine()
                    distance = abs(cashier._number - initialLocation)

                    # Check if the current cashier has a shorter queue or is closer
                    if queueLength < shortestQueueLength or (queueLength == shortestQueueLength and distance < shortestQueueDistance):
                        # Update the variables to keep track of the shortest queue
                        shortestQueueLength = queueLength
                        shortestQueueDistance = distance
                        shortestQueueCashier = cashier

                # If a suitable cashier is found, add the new customer to their queue
                if shortestQueueCashier:
                    shortestQueueCashier.addCustomer(customer)

            # Instruct all cashiers to provide another unit of service for customers in their queues
            for cashier in self.cashiers_list:
                cashier.serveCustomers(currentTime)
        


    def __str__(self):
        """Returns the string rep of the results of the simulation."""
        result = "CASHIER CUSTOMERS   AVERAGE     LEFT IN\n" + \
                 "        PROCESSED   WAIT TIME   LINE\n"
        for cashier in self.cashiers_list:
            result += str(cashier) + "\n"
        return result

