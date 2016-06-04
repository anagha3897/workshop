urlpatterns = ('',

               url(r'^$', UserRegistrationView.as_view(), name='register_user'))
