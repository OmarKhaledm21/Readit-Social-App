from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import get_user_model, login, logout

from django.views.generic import View

from .forms import SignupForm, SigninForm

# Create your views here.


class SignupView(View):
    def get(self, request):
        context = {
            "page_name": "Signup",
            "logged_in": request.user.is_authenticated,
            "form_url": "signup",
            "form": SignupForm(),
            "error": False,
            "form_errors": []
        }

        return render(request, "user/user_form.html", context)

    def post(self, request):
        form = SignupForm(request.POST)
        UserModel = get_user_model()

        username = request.POST['username']
        user_email = request.POST['email']

        context = {
            "page_name": "Signup",
            "logged_in": False,
            "form_url": "signin",
            "form": form,
            "error": False,
            "form_errors": []
        }

        if form.is_valid():
            password = request.POST['password']
            password2 = request.POST['retype_password']
            if (password != password2):
                context.form_errors.append("Passwords don't match")
                context.error = True
                return render(request, "user/user_form.html", context)
            # If data in form is valid we check if username or email is already used by another user
            username_check = UserModel.objects.filter(
                username=username).exists()
            email_check = UserModel.objects.filter(email=user_email).exists()

            if not username_check and not email_check:
                user_password = make_password(request.POST['password'])
                user_firstname = request.POST['first_name']
                user_lastname = request.POST['last_name']
                user_gender = request.POST['gender']
                phone = request.POST['phone']

                user = UserModel.objects.create(username=username, email=user_email, password=user_password,
                                                first_name=user_firstname, last_name=user_lastname, gender=user_gender, phone=phone)
                login(request, user)
                return redirect('user-profile', pk=request.user.id)

            else:
                form_error_status = True
                if username_check:
                    context.form_errors.append('Username already exists')
                if email_check:
                    context.form_errors.append('Email already exists')

                return render(request, "user/user_form.html", context)
        else:
            context.form_errors.extend(form.errors)
            context.form_error_status = True

            return render(request, "user/user_form.html", context)


class SigninView(View):
    def get(self, request):
        return render(request, "user/user_form.html", {
            "page_name":"Signin",
            "logged_in": False,
            "form_url": "signin",
            "form": SigninForm(),
            "error": False,
            "form_errors": []
        })

    def post(self, request):
        form = SigninForm(request.POST)

        form_errors = []
        form_error_status = False

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            UserModel = get_user_model()
            try:
                user = UserModel.objects.get(username=username)
                if user.check_password(password):
                    login(request, user)
                    return redirect('user-profile', pk=request.user.id)
            except UserModel.DoesNotExist:
                form_errors.append('Wrong username or password')
                form_error_status = True

                return render(request, "user/user_form.html", {
                    "page_name":"Signin",
                    "logged_in": False,
                    "form_url": "signin",
                    "form": form,
                    "error": form_error_status,
                    "form_errors": form_errors
                })


        else:
            form_errors.extend(form.errors)
            form_error_status = True

            return render(request, "user/user_form.html", {
                "page_name":"Signin",
                "logged_in": False,
                "form_url": "signin",
                "form": form,
                "error": form_error_status,
                "form_errors": form_errors
            })


def signout(request):
    logout(request)
    return redirect('signin')


class ProfileView(View):
    def get(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('signin')
        elif pk != request.user.id:
            return redirect('user-profile', pk=request.user.id)

        UserModel = get_user_model()
        user = UserModel.objects.get(pk=pk)

        form_error_status = False
        form_errors = []

        context = {
            "page_name":"Signup",
            "logged_in": True,
            "form_url": "user-profile",
            "error": form_error_status,
            "form_errors": form_errors,
            "user": user,
            "user_fullname": user.full_name()
        }

        return render(request, "user/profile.html", context)

    def post(self, request, pk):
        UserModel = get_user_model()
        user = UserModel.objects.get(pk=pk)
        try:
            image = request.FILES["image"]
            user.image = image
        except:
            print("NO IMAGE")

        form_error_status = False
        form_errors = []

        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password2 = request.POST['retype_password']

        if email != user.email:
            if UserModel.objects.filter(email=email).exists():
                form_error_status = True
                form_errors.append('Email already exists.')
            else:
                new_email = email
                user.email = new_email

        if password != password2:
            form_error_status = True
            form_errors.append("Passwords doesn't match.")

        if first_name == "" or last_name == "" or gender == "" or phone == "" or email == "":
            form_error_status = True
            form_errors.append("Can't leave empty fields.")

        if form_error_status == False:
            if len(password) > 5:
                new_password = make_password(password)
                user.password = new_password
            if user.first_name != first_name:
                user.first_name = first_name
            if user.last_name != last_name:
                user.last_name = last_name
            if user.gender != gender:
                user.gender = gender
            if user.phone != phone:
                user.phone = phone
            user.save()

        context = {
            "page_name":"Signup",
            "logged_in": True,
            "form_url": "user-profile",
            "error": form_error_status,
            "form_errors": form_errors,
            "user": user,
            "user_fullname": user.full_name()
        }

        return render(request, "user/profile.html", context)
