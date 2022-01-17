from django.contrib import admin
from django.urls import path, include
from project.urls import prj_cli_list_patterns
from client.urls import home_patterns
from .views import PersonalInfo, personal_info, signUpView, logInView, signoutView, successSignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_patterns)),
    path('client/', include('client.urls')),
    path('project/', include('project.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('', include(prj_cli_list_patterns)),
    path('', include('interactions.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('personal/', personal_info, name='personal_info'),
    # path('personal/', PersonalInfo.as_view(), name='personal'),
    path('accounts/signup/', signUpView, name='signup'),
    path('accounts/login/', logInView, name='login'),
    path('accounts/logout', signoutView, name='logout'),
    path('accounts/success_signup', successSignUpView, name='success_signup'),
]
