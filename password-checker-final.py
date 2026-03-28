import string
import random

# ========================================
# PHASE 1: PASSWORD STRENGTH CHECKER
# ========================================

# List of common weak passwords
COMMON_PASSWORDS = [
    'password', '123456', '12345678', 'qwerty', 'abc123', 'monkey',
    'letmein', 'welcome', 'password123', 'admin', 'root', 'user',
    '123456789', '12345', '1234567', 'password1', 'qwerty123'
]

def display_welcome():
    """Display welcome message"""
    print("\n" + "="*60)
    print(" "*15 + "PASSWORD SECURITY TOOL")
    print("="*60)
    print("       Protect Your Digital Life with Strong Passwords!")
    print("="*60 + "\n")

def display_menu():
    """Display main menu options"""
    print("\n" + "-"*60)
    print("MAIN MENU:")
    print("-"*60)
    print("1. Check Password Strength")
    print("2. Generate Strong Password")
    print("3. View Security Tips")
    print("4. Exit")
    print("-"*60)

def check_length(password):
    """Check password length and return score and feedback"""
    length = len(password)
    
    if length >= 16:
        return 4, "✓ Excellent length!"
    elif length >= 12:
        return 3, "✓ Good length"
    elif length >= 8:
        return 2, "⚠ Acceptable length, but consider 12+ characters"
    else:
        return 0, "✗ Too short! Use at least 8 characters"

def check_character_variety(password):
    """Check for different character types"""
    score = 0
    feedback = []
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    if has_upper:
        score += 1
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("✗ Missing uppercase letters (A-Z)")
    
    if has_lower:
        score += 1
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("✗ Missing lowercase letters (a-z)")
    
    if has_digit:
        score += 1
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("✗ Missing numbers (0-9)")
    
    if has_special:
        score += 1
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("✗ Missing special characters (!@#$%^&*)")
    
    return score, feedback

def check_common_password(password):
    """Check if password is in common passwords list"""
    if password.lower() in COMMON_PASSWORDS:
        return -3, "✗ WARNING: This is a commonly used password!"
    return 0, "✓ Not a common password"

def check_sequential_chars(password):
    """Check for sequential or repetitive characters"""
    password_lower = password.lower()
    
    # Check for sequential letters (abc, bcd, xyz, etc.)
    for i in range(len(password_lower) - 2):
        if ord(password_lower[i+1]) == ord(password_lower[i]) + 1 and \
           ord(password_lower[i+2]) == ord(password_lower[i]) + 2:
            return -1, "⚠ Contains sequential characters (e.g., abc, 123)"
    
    # Check for repetitive characters (aaa, 111, etc.)
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return -1, "⚠ Contains repetitive characters (e.g., aaa, 111)"
    
    return 0, "✓ No obvious patterns detected"

def calculate_strength(score):
    """Calculate strength rating based on total score"""
    if score >= 9:
        return "VERY STRONG 🛡️", "green"
    elif score >= 7:
        return "STRONG 💪", "blue"
    elif score >= 5:
        return "MODERATE ⚡", "yellow"
    elif score >= 3:
        return "WEAK ⚠️", "orange"
    else:
        return "VERY WEAK ❌", "red"

def display_strength_bar(score, max_score=12):
    """Display visual strength bar"""
    filled = int((score / max_score) * 20)
    bar = "█" * filled + "░" * (20 - filled)
    percentage = int((score / max_score) * 100)
    return f"[{bar}] {percentage}%"

def check_password_strength(password):
    """Main function to check password strength"""
    print("\n" + "="*60)
    print(" "*20 + "ANALYSIS RESULTS")
    print("="*60 + "\n")
    
    total_score = 0
    all_feedback = []
    
    # Check length
    score, feedback = check_length(password)
    total_score += score
    all_feedback.append(feedback)
    
    # Check character variety
    score, feedback_list = check_character_variety(password)
    total_score += score
    all_feedback.extend(feedback_list)
    
    # Check for common passwords
    score, feedback = check_common_password(password)
    total_score += score
    all_feedback.append(feedback)
    
    # Check for sequential/repetitive characters
    score, feedback = check_sequential_chars(password)
    total_score += score
    all_feedback.append(feedback)
    
    # Calculate final strength
    strength, color = calculate_strength(total_score)
    
    # Display results
    print(f"Password Length: {len(password)} characters")
    print(f"Strength Score: {total_score}/12")
    print(f"Strength Bar: {display_strength_bar(total_score)}")
    print(f"\nOVERALL RATING: {strength}\n")
    
    print("-"*60)
    print("DETAILED FEEDBACK:")
    print("-"*60)
    for item in all_feedback:
        print(f"  {item}")
    
    print("\n" + "="*60)
    
    # Provide recommendations if password is weak
    if total_score < 7:
        print("\n💡 RECOMMENDATIONS TO IMPROVE:")
        print("-"*60)
        print("  • Use at least 12-16 characters")
        print("  • Mix uppercase and lowercase letters")
        print("  • Include numbers and special characters (!@#$%^&*)")
        print("  • Avoid common words and patterns")
        print("  • Don't use personal information (name, birthday)")
        print("-"*60)

def display_security_tips():
    """Display password security tips"""
    print("\n" + "="*60)
    print(" "*18 + "PASSWORD SECURITY TIPS")
    print("="*60 + "\n")
    
    tips = [
        "1. Use at least 12-16 characters for strong passwords",
        "2. Mix uppercase, lowercase, numbers, and special characters",
        "3. Avoid dictionary words and common phrases",
        "4. Don't use personal information (birthdays, names, etc.)",
        "5. Use unique passwords for each account",
        "6. Consider using a password manager",
        "7. Enable two-factor authentication when available",
        "8. Change passwords regularly (every 3-6 months)",
        "9. Never share your passwords with anyone",
        "10. Avoid writing passwords down in plain text"
    ]
    
    for tip in tips:
        print(f"  {tip}")
    
    print("\n" + "="*60)

def main():
    """Main program controller"""
    display_welcome()
    
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            print("\n" + "-"*60)
            password = input("Enter password to check: ")
            if password:
                check_password_strength(password)
            else:
                print("⚠ Password cannot be empty!")
        
        elif choice == '2':
            print("\n⚠ Password Generator coming in Phase 2!")
            print("   (Will be available after you test Phase 1)")
        
        elif choice == '3':
            display_security_tips()
        
        elif choice == '4':
            print("\n" + "="*60)
            print(" "*15 + "Thank you for using our tool!")
            print(" "*18 + "Stay secure! 🔒")
            print("="*60 + "\n")
            break
        
        else:
            print("\n❌ Invalid choice! Please enter 1-4.")

# Run the program
if __name__ == "__main__":
    main()
