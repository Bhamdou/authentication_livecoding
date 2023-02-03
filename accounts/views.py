from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, View
from .forms import LoginForm
# Create your views here.
# - LoginView, - LogoutView

class LogoutView(View):
    def dispatch(self, request):
        self.request.session.flush()
        return HttpResponseRedirect(reverse('home'))

class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        username = form.data.get('username', None)
        password = form.data.get('password', None)

        # hard coded
        if (username == 'admin' and password == 'admin') or (username == 'lucas' and password == 'lucas'):
            # generate session id
            self.request.session.flush()
            self.request.session["user_id"] = username
            # redirect to a success URL
            return HttpResponseRedirect(self.success_url)
        else:
            # reload the form
            return super().form_valid(self.request)
