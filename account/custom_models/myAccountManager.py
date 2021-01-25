from django.contrib.auth.models import BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Usuário deve possuir um email")
        if not first_name:
            raise ValueError("Usuário deve possuir um nome")
        if not last_name:
            raise ValueError("Usuário deve possuir um sobrenome")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )        

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(
            email=self.normalize_email(email),
            password=set_password(self.password),
            first_name=first_name,
            last_name=last_name,
        )  

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
