"""tipply URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from app.views import IndexView,SignUpView,LoginView,LogoutView,EmployeeListingCreateView,ApplicantListView, EmployeeListView, EmployeeWorkSkillCreateView, EmployeeCreateView, user_create_view,poi_list,pwk_list, BookView, BusinessMapView
from tipplyapi.views import EmployeeListingListAPIView, EmployeeListingDetailAPIView
from rest_framework.authtoken import views as authviews
from app import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^api-token-auth/', authviews.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^signup/$', SignUpView.as_view(), name='sign_up_view'),
    url(r'^login/$', login, name="login_view"),
    url(r'^logout/$', logout, name="logout_view"),
    url(r'^places$', views.poi_list),
    url(r'^people$', views.pwk_list),
    url(r'^book$',BookView.as_view(), name="book_view"),
    url(r'^findus$',BusinessMapView.as_view(), name="business_map_view"),
    url(r'^employee_create/$',EmployeeCreateView.as_view(), name='employee_create_view'),
    url(r'^employee_listing_create/$',EmployeeListingCreateView.as_view(), name='employee_listing_create_view'),
    url(r'^applicant_list/$',ApplicantListView.as_view(), name='applicant_list_view'),
    url(r'^employee_workskill_create/$',EmployeeWorkSkillCreateView.as_view(), name='employee_workskill_create_view'),
    url(r'^employee_list/$',EmployeeListView.as_view(), name='employee_list_view'),
    url(r'^api/employee_listings/$', EmployeeListingListAPIView.as_view(), name="employee_listing_list_api_view"),
    url(r'^api/employee_listings/(?P<pk>\d+)/$', EmployeeListingDetailAPIView.as_view(), name="employee_listing_detail_api_view")


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
