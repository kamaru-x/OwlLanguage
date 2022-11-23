from django.urls import path
from gallery import views

urlpatterns = [
    path('create_album/',views.create_album,name='create_album'),
    path('view_album/<int:aid>/',views.view_ablum,name='view_album'),
    path('upload_image/',views.upload_image,name='upload_image'),
    path('manage_album/',views.manage_album,name='manage_album'),
    path('edit_album/<int:aid>/',views.edit_album,name='edit_album'),
    path('remove/<int:aid>/',views.remove,name='remove'),
    path('remove_image/<int:aid>/<int:iid>/',views.remove_image,name='remove_image'),
]