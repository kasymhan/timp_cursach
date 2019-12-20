from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Site, name='site'),
    path(r'an/<pk>',Anouc.as_view(),name='anouc'),
    path('registr/', Registration.as_view(), name='registration'),
    path('auth/', Auth.as_view(), name='auth1'),
    path('logout/', logout.as_view(), name='logout'),
    path('an/', Announcemen.as_view(), name='create_announcement'),
    path('redirect_an/', An.as_view(), name='redirect_an'),
    path('redirect_ac/', Ac.as_view(), name='redirect_ac'),
    path('profile/', Profile.as_view(), name='profile'),
    path('delete/', Delete_Announcement.as_view(), name='delete_annoucement'),
    path('search/', Search.as_view(), name='search')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
