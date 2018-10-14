from django.conf.urls import url
from users import views
from django.contrib.auth import views as auth_views

from users.views import PasswordResetView, PasswordResetConfirmView, PasswordChangeView

urlpatterns = [
    # For account activation
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

    # google web login just for testing
    # url(r'^/websignin$', views.web_signin, name='websignin'),
    url(r'^google-token-verify/$', views.Google_Token.as_view(), name='google_token'),
    # To login a user
    url(r'^signin$', views.SignIn.as_view(), name='signin'),
    # To signup a user
    url(r'^google-signup/$', views.GoogleSignUp.as_view(), name='signup'),
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),
    # To update profile of the user
    url(r'^update$', views.ProfileUpdate.as_view(), name='profile_update'),

    # End points for password reset/Forgot password...

    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^(?P<user_id>.{32,})$', views.Detail.as_view(), name='detail'),

    url(r'^password/reset/$', PasswordResetView.as_view(),
        name='rest_password_reset'),

]
