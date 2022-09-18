
from django.contrib import admin
from django.urls import path
from authentication.views import login, signup, logout
from django.conf.urls import url, include
from urlhandler.views import dashboard, generate, home
from api.resources import NoteResource

note_resource = NoteResource()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path('logout/', logout, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('generate/', generate, name="generate"),
    path('<str:query>/', home, name="home"),
    url(r'^api/', include(note_resource.urls)),

]
