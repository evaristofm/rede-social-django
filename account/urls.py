from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .auth import (
    PasswordResetCompleteView, PasswordChangeDoneView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetView, PasswordChangeView
)

from . import views

app_name = 'account'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),  # TODO: Erro para redirecionar ao template password_change_done (reversy_lazy)
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
