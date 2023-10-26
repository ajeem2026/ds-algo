"""
Author: Abid Jeem
File: translator.py

This program is reponsible for converting infix expressions into postfix expressions
"""

from tokens import Token
from scanner import Scanner
from utils.linkedStack import LinkedStack

class Translator(object):
    """Translates infix expressions to postfix expressions."""

    def __init__(self, scanner):
        """Sets the initial state of the translator."""
        # Keeps track of the infix expression we've seen so far
        self._expressionSoFar = ""
        
        # Stack for operators
        self._operatorStack = LinkedStack()
        
        # Scanner to tokenize a string
        self._scanner = scanner


    def translate(self):
        """Returns a list of tokens that represent the postfix
        form of sourceStr.  Assumes that the infix expression
        in sourceStr is syntactically correct"""
        # Use a python list to store the postfix tokens
        postfix = list()
        
        
        # For each token in our scanner
        for currentToken in self._scanner:
            # Keep track of what has been seen so far
            self._expressionSoFar += str(currentToken) + " "
            
            # If the token is an int, add to end of postfix list
            if currentToken.getType() == Token.INT:
                postfix.append(currentToken)

            
            # If the token is an (, push it on the stack
            elif currentToken.getType()== Token.LPAR:
                self._operatorStack.push(currentToken)

            
            # If the token is an ), pop from the stack until we see a (
            #  and add to end of postfix list
            elif currentToken.getType() == Token.RPAR:
                while not self._operatorStack.isEmpty() and self._operatorStack.peek().getType() != Token.LPAR:
                    postfix.append(self._operatorStack.pop())
                if not self._operatorStack.isEmpty() and self._operatorStack.peek().getType() == Token.LPAR:
                    self._operatorStack.pop()  # Pop the left parenthesis
                        
            # Otherwise, the token is an operator.
            # While there are tokens on the stack that have higher precedence
            # than the current token, remove them from the stack and add to end of postfix
            else:
                while (not self._operatorStack.isEmpty() and self._operatorStack.peek().isOperator()and self._operatorStack.peek().getPrecedence() >= currentToken.getPrecedence()):
                    postfix.append(self._operatorStack.pop())
                # Finally, push the current token onto the stack
                self._operatorStack.push(currentToken)
        # At the end, pop the remaining tokens from the stack anrd add to the end of postfix     
        while not self._operatorStack.isEmpty():
            operator=self._operatorStack.pop()
            postfix.append(operator)      
            
        # return our postfix expression
        return postfix

    



   
    def __str__(self):
        """Returns a string containing the contents of the expression
        processed and the stack to this point."""
        result = "\n"
        
        if self._expressionSoFar == "":
            result += "Portion of expression processed: none\n"
        
        else: 
            result += "Portion of expression processed: " + \
                   self._expressionSoFar + "\n"
        
        if self._operatorStack.isEmpty():
            result += "The stack is empty"
        
        else:
            result += "Operators on the stack          : " + \
                      str(self._operatorStack)
        
        return result

    def translationStatus(self):
        return str(self)

    
def main():
    """Tester function for translators."""
    while True:
        sourceStr = input("Enter an infix expression, or enter to quit: ")
        if sourceStr == "":
            break
        else:
            try:
                translator = Translator(Scanner(sourceStr))
                postfix = translator.translate()
                print("Postfix:", end =" ")
                for token in postfix: print(token, end=" ")
                print()
            except Exception as e:
                print("Error: ", e, translator.translationStatus())

if __name__ == '__main__': 
    main()

