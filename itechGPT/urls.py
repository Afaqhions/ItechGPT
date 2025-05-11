"""
URL configuration for itechGPT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Linking of veiws.py
from . import veiws

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', veiws.mainPage,name='main-page'),
    path('resource-page',veiws.resourcePage,name='resource-page'),
    path('products',veiws.productPage),
    path('about-us',veiws.aboutUsPage),
    path('login-user',veiws.loginPage, name='login'),
    path('join-us',veiws.signUpPage,name='sign-up-user'),
    path('forget-user',veiws.forgetPage),
    path('discover', veiws.discoverPage),
    path('ai-app',veiws.aiPage,name='ai-usr-app'),
    path('logout/', veiws.userLogout, name='logout-user'),
    path('pass-reset-page/<str:user>/', veiws.passResetPage, name='pass_reset_page')  # Ensure it captures 'user'
]
