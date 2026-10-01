from typing import TypedDict

class User(TypedDict):
    id: int
    name: str
    email: str

user1: User = {
    "id": 1,
    "name": "Hailey",
    "email": "hailey@example.com"
}

print(user1)  # Hailey