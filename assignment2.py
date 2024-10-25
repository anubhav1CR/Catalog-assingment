import random
import json
from functools import reduce

def convert_to_decimal(base, value):

    return int(value, int(base))

def generate_polynomial(secret, degree):

    coefficients = [random.randint(1, 100) for _ in range(degree)]
    coefficients.append(secret)  
    return coefficients

def evaluate_polynomial(coefficients, x):

    return sum(coef * (x ** idx) for idx, coef in enumerate(coefficients))

def generate_shares(secret, num_shares, threshold):

    coefficients = generate_polynomial(secret, threshold - 1)
    shares = []
    for x in range(1, num_shares + 1):
        y = evaluate_polynomial(coefficients, x)
        shares.append((x, y))  
    return shares

def lagrange_interpolation(shares, x):
    
    def lagrange_basis(j):
        basis = 1
        for m in range(len(shares)):
            if m != j:
                basis *= (x - shares[m][0]) / (shares[j][0] - shares[m][0])
        return basis

    
    secret = sum(shares[j][1] * lagrange_basis(j) for j in range(len(shares)))
    return int(secret)

def calculate_constant_term(roots):
    
    c = 1  
    for root in roots:
        c *= root  
    return c

def read_json_file(file_path):
    
    with open(file_path, 'r') as file:
        data = json.load(file)  
    return data

def main():
    
    secret = 12345  
    num_shares = 5   
    threshold = 3    

    
    shares = generate_shares(secret, num_shares, threshold)
    print("Generated Shares:")
    for x, y in shares:
        print(f"Share {x}: {y}")

    selected_shares = shares[:threshold]  

    
    reconstructed_secret = lagrange_interpolation(selected_shares, 0)
    print(f"\nReconstructed Secret from shares {selected_shares}: {reconstructed_secret}")

    input_data = read_json_file("testcase1.json")
    
    n = input_data["keys"]["n"]
    roots = []
    for i in range(1, n + 1):
        key = str(i)
        if key in input_data:  # Ensure key exists
            base = input_data[key]["base"]
            value = input_data[key]["value"]
            decimal_value = convert_to_decimal(base, value)
            roots.append(decimal_value)

    
    secret_C = calculate_constant_term(roots)
    print(f"\nThe constant term (c) of the polynomial from roots is: {secret_C}")

if __name__ == "__main__":
    main()
