from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from portal.models import UserProfile,Student, Professor

class StudentSignupForm(UserCreationForm):
	# email = forms.EmailField(required=True)
	# program = forms.ChoiceField()
	# branch = forms.ChoiceField()
	# batch = forms.IntegerField()
	# tags = forms.CharField()

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	# def clean(self):
	# 	cleaned_data = super().clean()
	# 	email = cleaned_data.get('email')

	# 	if UserProfile.objects.filter(email=email).exists():
	# 		msg = 'A user with that email already exists.'
	# 		self.add_error('email', msg)

	# 	return self.cleaned_data

	def save(self, commit=True):
		user = super(StudentSignupForm, self).save(commit=False)
		# user.email = self.cleaned_data['email']
		if commit:
			user.save()
		# Student.objects.create()
		return user


class ProfessorSignupForm(UserCreationForm):
	# email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	# def clean(self):
	# 	cleaned_data = super().clean()
	# 	email = cleaned_data.get('email')

	# 	if UserProfile.objects.filter(email=email).exists():
	# 		msg = 'A user with that email already exists.'
	# 		self.add_error('email', msg)

	# 	return self.cleaned_data
		
	def save(self, commit=True):
		user = super(ProfessorSignupForm, self).save(commit=False)
		# user.email = self.cleaned_data['email']
		if commit:
			user.save()
			# Professor.objects.create()

		return user
	
# Create your forms here.

# class SignupForm(UserCreationForm):
# 	email = forms.EmailField(required=True)

# 	class Meta:
# 		model = User
# 		fields = ("username", "email", "password1", "password2")

# 	def save(self, commit=True):
# 		user = super(SignupForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user