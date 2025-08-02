def perform_operation(num1:float, num2:float, operation:str):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'."

# Example usage:
if __name__ == "__main__":
    print(perform_operation(10,5, 'add'))
    print(perform_operation(10,5, 'subtract'))
    print(perform_operation(10,5, 'multiply'))
    print(perform_operation(10,5, 'divide'))
    print(perform_operation(10,0, 'divide'))  # Testing division by zero
    print(perform_operation(10,5, 'modulus'))  # Testing invalid operation
