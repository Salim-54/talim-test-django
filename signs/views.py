from django.shortcuts import render
from django.views.generic import TemplateView


from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator

class Index(TemplateView):

    template_name = "homepage.html"
    
class SignUp(TemplateView):

    template_name = "homepage.html"
    










from .forms import (
	UserForm,
	UserProfileForm,
	AuthForm,
	)

result = "Error"
message = "There was an error, please try again"


class AccountView(TemplateView):
	'''
	Generic FormView with our mixin to display user account page
	'''
	template_name = "users/account.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)



def profile_view(request):
	'''
	function view to allow users to update their profile
	'''
	user = request.user
	up = user.userprofile

	form = UserProfileForm(instance = up) 

	if request.is_ajax():
		form = UserProfileForm(data = request.POST, instance = up)
		if form.is_valid():
			obj = form.save()
			obj.has_profile = True
			obj.save()
			result = "Success"
			message = "Your profile has been updated"
		else:
			message = print('error ocurred in login')
		data = {'result': result, 'message': message}
		return JsonResponse(data)

	else:

		context = {'form': form}
		context['google_api_key'] = settings.GOOGLE_API_KEY
		context['base_country'] = settings.BASE_COUNTRY

		return render(request, 'users/profile.html', context)



class SignUpView(FormView):
	'''
	Generic FormView with our mixin for user sign-up with reCAPTURE security
	'''

	template_name = "users/sign_up.html"
	form_class = UserForm
	success_url = "/"

class SignInView(FormView):
	'''
	Generic FormView with our mixin for user sign-in
	'''

	template_name = "users/sign_in.html"
	form_class = AuthForm
	success_url = "/"

	




def sign_out(request):
	'''
	Basic view for user sign out
	'''
	logout(request)
	return redirect(reverse('users:sign-in'))


