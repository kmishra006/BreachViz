# Create the password analyzer module
password_analyzer_code = '''import hashlib
import requests
import re
import string
import math
import time
from collections import Counter

class PasswordAnalyzer:
    def __init__(self):
        self.common_passwords = self._load_common_passwords()
        
    def _load_common_passwords(self):
        """Load common passwords list"""
        return [
            "password", "123456", "password123", "admin", "qwerty", 
            "letmein", "welcome", "monkey", "dragon", "master",
            "123456789", "12345678", "12345", "1234567890", "1234567",
            "password1", "123123", "abc123", "Password1", "qwerty123"
        ]
    
    def check_password_breach(self, password):
        """Check if password appears in HaveIBeenPwned database"""
        try:
            # Hash the password using SHA1
            sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
            
            # Use k-anonymity model - send first 5 characters
            prefix = sha1_hash[:5]
            suffix = sha1_hash[5:]
            
            # Query the API
            response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}", timeout=10)
            
            if response.status_code == 200:
                hashes = response.text.splitlines()
                for hash_line in hashes:
                    hash_suffix, count = hash_line.split(':')
                    if hash_suffix == suffix:
                        return {"breached": True, "count": int(count)}
                
                return {"breached": False, "count": 0}
            else:
                return {"breached": False, "count": 0, "error": "API unavailable"}
                
        except Exception as e:
            return {"breached": False, "count": 0, "error": str(e)}
    
    def calculate_password_strength(self, password):
        """Calculate password strength score"""
        score = 0
        feedback = []
        
        # Length scoring
        length = len(password)
        if length >= 12:
            score += 25
        elif length >= 8:
            score += 15
        elif length >= 6:
            score += 10
        else:
            feedback.append("Password is too short")
        
        # Character diversity
        has_lower = bool(re.search(r'[a-z]', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_digit = bool(re.search(r'\\d', password))
        has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
        
        char_types = sum([has_lower, has_upper, has_digit, has_special])
        score += char_types * 10
        
        # Entropy calculation
        entropy = self._calculate_entropy(password)
        if entropy >= 60:
            score += 25
        elif entropy >= 40:
            score += 15
        elif entropy >= 25:
            score += 10
        
        # Common password check
        if password.lower() in [p.lower() for p in self.common_passwords]:
            score = max(0, score - 50)
            feedback.append("Password is commonly used")
        
        # Pattern detection
        if self._has_sequential_pattern(password):
            score -= 15
            feedback.append("Contains sequential patterns")
        
        if self._has_repetitive_pattern(password):
            score -= 10
            feedback.append("Contains repetitive patterns")
        
        return {
            "score": min(100, max(0, score)),
            "feedback": feedback,
            "entropy": entropy
        }
    
    def analyze_password_comprehensive(self, password):
        """Comprehensive password analysis"""
        return {
            "length": len(password),
            "has_uppercase": bool(re.search(r'[A-Z]', password)),
            "has_lowercase": bool(re.search(r'[a-z]', password)),
            "has_numbers": bool(re.search(r'\\d', password)),
            "has_special": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
            "entropy": self._calculate_entropy(password),
            "character_sets": self._count_character_sets(password),
            "strength_score": self.calculate_password_strength(password)["score"],
            "is_common": password.lower() in [p.lower() for p in self.common_passwords],
            "has_sequential": self._has_sequential_pattern(password),
            "has_repetitive": self._has_repetitive_pattern(password)
        }
    
    def _calculate_entropy(self, password):
        """Calculate password entropy in bits"""
        if not password:
            return 0
        
        # Determine character space
        charset_size = 0
        if re.search(r'[a-z]', password):
            charset_size += 26
        if re.search(r'[A-Z]', password):
            charset_size += 26
        if re.search(r'\\d', password):
            charset_size += 10
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            charset_size += 32
        
        if charset_size == 0:
            return 0
        
        # Calculate entropy
        entropy = len(password) * math.log2(charset_size)
        return entropy
    
    def _count_character_sets(self, password):
        """Count different character sets used"""
        sets = 0
        if re.search(r'[a-z]', password):
            sets += 1
        if re.search(r'[A-Z]', password):
            sets += 1
        if re.search(r'\\d', password):
            sets += 1
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            sets += 1
        return sets
    
    def _has_sequential_pattern(self, password):
        """Check for sequential patterns like 123, abc"""
        # Check for ascending sequences
        for i in range(len(password) - 2):
            if (ord(password[i]) + 1 == ord(password[i + 1]) and 
                ord(password[i + 1]) + 1 == ord(password[i + 2])):
                return True
        return False
    
    def _has_repetitive_pattern(self, password):
        """Check for repetitive patterns"""
        # Check for repeated characters
        for i in range(len(password) - 2):
            if password[i] == password[i + 1] == password[i + 2]:
                return True
        return False
    
    def get_password_recommendations(self, analysis):
        """Get recommendations to improve password"""
        recommendations = []
        
        if analysis['length'] < 12:
            recommendations.append("🔹 Use at least 12 characters for better security")
        
        if not analysis['has_uppercase']:
            recommendations.append("🔹 Add uppercase letters (A-Z)")
        
        if not analysis['has_lowercase']:
            recommendations.append("🔹 Add lowercase letters (a-z)")
        
        if not analysis['has_numbers']:
            recommendations.append("🔹 Include numbers (0-9)")
        
        if not analysis['has_special']:
            recommendations.append("🔹 Use special characters (!@#$%^&*)")
        
        if analysis['is_common']:
            recommendations.append("🔸 Avoid common passwords")
        
        if analysis['has_sequential']:
            recommendations.append("🔸 Avoid sequential patterns (123, abc)")
        
        if analysis['has_repetitive']:
            recommendations.append("🔸 Avoid repetitive patterns (aaa, 111)")
        
        if analysis['entropy'] < 40:
            recommendations.append("🔹 Increase password complexity for higher entropy")
        
        return recommendations
    
    def estimate_crack_time(self, password):
        """Estimate time to crack password"""
        analysis = self.analyze_password_comprehensive(password)
        entropy = analysis['entropy']
        
        # Assuming 1 billion guesses per second
        guesses_per_second = 1_000_000_000
        
        # Calculate possible combinations
        possible_combinations = 2 ** entropy
        
        # Average time to crack (half of all possibilities)
        average_time_seconds = possible_combinations / (2 * guesses_per_second)
        
        # Convert to human readable format
        if average_time_seconds < 1:
            return "< 1 second"
        elif average_time_seconds < 60:
            return f"{average_time_seconds:.0f} seconds"
        elif average_time_seconds < 3600:
            return f"{average_time_seconds / 60:.0f} minutes"
        elif average_time_seconds < 86400:
            return f"{average_time_seconds / 3600:.0f} hours"
        elif average_time_seconds < 31536000:
            return f"{average_time_seconds / 86400:.0f} days"
        elif average_time_seconds < 31536000000:
            return f"{average_time_seconds / 31536000:.0f} years"
        else:
            return f"{average_time_seconds / 31536000:.2e} years"
'''

print("Password Analyzer Module Created!")
print("=" * 50)
print("Features implemented:")
print("• HaveIBeenPwned API integration")
print("• Password strength calculation")
print("• Entropy analysis")
print("• Pattern detection")
print("• Comprehensive recommendations")
print("• Crack time estimation")