import secrets
import string

def generate_secret_key(length=50):
    """Generate a secure random secret key"""
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*(-_=+)'
    secret_key = ''.join(secrets.choice(alphabet) for _ in range(length))
    return secret_key

if __name__ == "__main__":
    secret_key = generate_secret_key()
    print("Generated Django Secret Key:")
    print(f"SECRET_KEY={secret_key}")
    print("\nCopy this to your .env file")