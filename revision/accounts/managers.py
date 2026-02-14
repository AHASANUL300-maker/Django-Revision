from django.contrib.auth.base_user import BaseUserManager

class AwesomeUserManager(BaseUserManager):

    # Mention of Email, Password and setting the default value of passeord as None and rest are extra fields as **kwargs -> Key word arguments.
    def create_user(self, email, password=None, **extra_fileds):
        if not email:
            raise ValueError("Email is required.") # Raises a value error if the email is not present
        
        user = self.model(email = email, **extra_fileds)   # Creates the user
        user.set_password(password)  #Encrypts the password when saved
        user.save() # Saves the user model
        return user
    
    # Method to create superuser same as above
    def create_superuser(self, email, password=None, **extra_fields):
        # These fields are to be set as True for Super User
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Super must have is_staff = True")
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Super must have is_superuser = True")

        if extra_fields.get('is_active') is not True:
            raise ValueError("Super must have is_active = True")
        
        # Invoking the above method to create the user. It just extends this current method with above method code
        return self.create_user(email, password, **extra_fields)
