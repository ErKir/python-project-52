from django.shortcuts import render
from django.views import View


class Users(View):
    def get(self, request):
        return render(request, 'users/users.html', {})
