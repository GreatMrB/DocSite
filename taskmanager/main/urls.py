
from django.urls import path,include
from.import views 
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin 


urlpatterns = [
    path('',views.base,name= 'reg'),
    path('main',views.main,name= 'home'),
    path('tasks',views.tasks,name='tasks'),
    path('add',views.add,name='add'),
    path('project',views.project,name='project'),
    path('doc',views.doc,name='doc'),
    path('people',views.people,name='people'),
    path('register',views.register,name='register'),
    path("log", views.log, name="log"),
    path("profile", views.profile, name="profile"),
    path('email',views.email,name='email'),
    path('upload',views.upload,name='upload'),
    path('upload2',views.upload2,name='upload2'),
    path('admin/', admin.site.urls),
    path('KOSU',views.KOSU,name='KOSU'),
    path('accounts/', include('django.contrib.auth.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)