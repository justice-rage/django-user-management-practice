""" Commented out code fails to output expected results.
Figure out why. """
# from django.conf.urls import url, include
# from users.views import dashboard

# urlpatterns = [
#     url(r"^accounts/", include("django.contrib.auth.urls")), # potential source of issue
#     url(r"^dashboard/", dashboard, name="users/dashboard"),
# ]

from django.conf.urls import include, url
from users.views import dashboard

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
]