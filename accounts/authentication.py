from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()  # Dynamically get the user model

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print(f"Authenticating user: {username}")  # Debug print
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            print("User does not exist")  # Debug print
            return None
        if user.check_password(password):
            print("Password matched")  # Debug print
            return user
        else:
            print("Password did not match")  # Debug print
            return None
