from werkzeug.security import generate_password_hash
from models.user import User


username = "admin"

password = "admin123"

role = "Admin"


password_hash = generate_password_hash(password)

User.create(
    username,
    password_hash,
    role
)

print("Admin user created successfully!")