from django.utils.deprecation import MiddlewareMixin
from loginAndRegister.models import userInfo, Admin
from menu_and_select.models import doctorInfos


class Middle(MiddlewareMixin):

    def process_request(self, request):
        def identify(form, **key):
            user = form.objects.filter(**key)
            # 身份符合
            if user.exists():
                return True

            # 身份不符合
            else:
                request.session.clear()
                return False

        if 'login' in request.path_info or 'register' in request.path_info or "pharmacy" in request.path_info:
            pass
        else:
            role = request.session.get('role')
            if request.session.get("login", None):
                if role == "admin":
                    if identify(Admin, username=request.session['username'], phoneNumber=request.session['phone']):
                        print("5")
                        pass
                    else:
                        print("6")
                        return
                if role == "doctor":
                    if identify(doctorInfos, doctor_name=request.session['username'],
                                phoneNumber=request.session['phone']):
                        print("3")
                        pass
                    else:
                        print("4")
                        return

                if role == "patient":
                    if identify(userInfo, username=request.session['username'], phoneNumber=request.session['phone']):
                        print("1")
                        pass
                    else:
                        print("2")
                        return
            else:
                print(request.session.items())
                print("8")
                return

    def process_response(self, request, response):
        return response
