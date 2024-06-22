from django.urls import path
from.import views
urlpatterns = [path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signupsuccess', views.signup_success, name='signup_success'),
    path('personal', views.personal, name='personal'),
    path('formsuccess', views.form_success, name='form_success'),
    path('form', views.form, name='form'),
    path('educational', views.educational, name='educational'),
    path('financial', views.financial, name='financial'),
    path('professional', views.professional, name='professional'),
    path('medical', views.medical, name='medical'),
    path('lout', views.lout, name='lout'),
    path('data', views.data, name='data'),
    path('deletesuccess', views.delete_success, name='delete_success'),
    path('editsuccess', views.edit_success, name='edit_success'),

    path('edit_personal/<int:id>/', views.edit_personal, name='edit_personal'),
    path('edit_educational/<int:id>/', views.edit_educational, name='edit_educational'),
    path('edit_financial/<int:id>/', views.edit_financial, name='edit_financial'),
    path('edit_professional/<int:id>/', views.edit_professional, name='edit_professional'),
    path('edit_medical/<int:id>/', views.edit_medical, name='edit_medical'),

    path('delete_personal/<int:id>/', views.delete_personal, name='delete_personal'),
    path('delete_educational/<int:id>/', views.delete_educational, name='delete_educational'),
    path('delete_financial/<int:id>/', views.delete_financial, name='delete_financial'),
    path('delete_professional/<int:id>/', views.delete_professional, name='delete_professional'),
    path('delete_medical/<int:id>/', views.delete_medical, name='delete_medical')
              ]

