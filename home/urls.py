from django.urls import path,reverse_lazy
from home import views
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from home.forms import ChangePassword

urlpatterns = [
    path('',views.user_login,name='login'),
    path('',views.index,name='index'),
    path('test-area/',views.test_area,name='test-area'),
    path('profile/',PasswordChangeView.as_view(template_name='change-password.html',success_url=reverse_lazy('password changed'),form_class=ChangePassword),name='profile'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('about_us/',views.about_us,name='about_us'), 
    path('contact_us/',views.contact_us,name='contact_us'), 
    path('feedback/',views.feedback,name='feedback'),
    path('remove_feedback/<int:fid>/',views.remove_feedback,name='remove_feedback'),
    path('enquiry/',views.enquiry,name='enquiry'),
    path('view_enquiry/<int:eid>/',views.view_enquiry,name='view-enquiry'),
    path('remove_enquiry/<int:eid>/',views.remove_enquiry,name='remove_enquiry'),
    path('quick_links/',views.quick_links,name='quick_links'),
    path('manage_menu/',views.manage_menu,name='manage_menu'),
    path('remove_abt_img/<int:aid>/',views.remove_abt_img,name='remove_abt_img'),
    path('profile/done/',PasswordChangeDoneView.as_view(template_name='change-password.html')),
    path('logout/',views.signout,name='logout'),
    path('theme/',views.change_color,name='change-theme'),
    path('export-feedbacks/',views.export_feedbacks,name='export-feedbacks'),
    path('export-enquiries/',views.export_enquiries,name='export-enquiries'),
]