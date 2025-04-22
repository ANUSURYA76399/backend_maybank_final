from validation import *

# Test data
test_cases = {
    "card_number": ("4532123456789012", "123456"),
    "zip_code": ("50000", "123"),
    "currency": ("MYR", "ABC"),
    "email": ("john.doe@example.com", "invalid.email@"),
    "phone_number": ("9876543210", "123456"),
    "expiry_date": ("12/25", "13/22"),
    "username": ("johndoe123", "jo"),
    "password": ("Test@1234", "weak"),
    "date": ("2024-04-21", "2024-13-45")
}

def run_validation_tests():
    print("Validation Test Results:")
    print("-" * 50)
    
    for field, (valid, invalid) in test_cases.items():
        print(f"\n{field.replace('_', ' ').title()}:")
        
        # Get the corresponding validation function
        validator = globals()[f"validate_{field}"]
        
        # Test valid input
        result = validator(valid)
        print(f"Valid input ({valid}): {'✓' if result else '✗'}")
        
        # Test invalid input
        result = validator(invalid)
        print(f"Invalid input ({invalid}): {'✗' if not result else '!'}")

if __name__ == "__main__":
    run_validation_tests()