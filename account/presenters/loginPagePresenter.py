class LoginPagePresenter():
    @staticmethod
    def userAuthenticatedAndActivaded(request):
        return_data = []
        username = ''
        print('##############################')
        print(str(request.user))
        print('##############################')
        if str(request.user) != 'AnonymousUser':
            username = request.user.first_name
        if request.user.is_authenticated and request.user.is_active:
            if request.user.is_operator:
                return_data = ['homeOperator', username ]
            elif request.user.is_admin:
                return_data = ['adminhome', username ]
            else:
                return_data = ['home', username ]
        return return_data


    @staticmethod
    def requestIsPost(request, authenticate, login, messages):
        user = None
        return_data = []
        username = request.user.first_name
        if request.method == 'POST':
            form = LoginForm(request.POST)
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)

        if user is not None and user.is_active:
            login(request, user)
            if user.is_operator:
                return_data = ['homeOperator', username ]
            elif user.is_admin:
                return_data = ['adminHome', username ]
            else:
                return_data = ['home', username ]
        else:
            messagerError = messages.error(request, 'Nome de usuário e/ou senha incorreto')
            return_data.push(messagerError)
        return return_data
