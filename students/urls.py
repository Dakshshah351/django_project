from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import download_zip
from django.conf import settings
from .views import ProfileUpdate


urlpatterns=[
############ USER'S Screen ###############################################################
    path("",views.students,name='students'),
    path("home/",views.student,name='developer'),
    path("leader/",views.leader,name='leader'),
    path("admin/",views.admin,name='admin'),
                          

############END OF USER'S Screeen##################################################

############ AUTHENTICATION OF USER#################################################### 

    path('login/',views.login,name="login"),
    path('forget_password/',views.forgotpwdPage,name="forget_password"),
    path('reset_password/',views.reset_password,name="reset_password"),
    path('otp_varification/<email>',views.verify_otp,name="otp_varification"),
    path('new_password/<email>',views.new_password,name="new_password"),
    path('logout/',auth_views.LogoutView.as_view(template_name='index.html'),name='logout'),
    path('register/',views.SignUp.as_view(),name='register'),
    path('profile/',ProfileUpdate.as_view(),name="profile"),

############ AUTHENTICATION OF USER END####################################################
######################## Requirement Gathering CRUD #############################################
    path('RequirementGathering/',views.RequirementGathering,name="RequirementGathering"),
    path('viewGathering/',views.viewGathering,name="viewGathering"),
    path('viewGatheringbyleader/',views.viewGatheringbyleader,name="viewGatheringbyleader"),
    path('developerrecords/',views.developerrecords,name="developerrecords"),

    path('<id>/delete', views.deleteGathering ),
    path('<id>/update', views.updateGathering ),
######################## Requirement Gathering CRUD END #############################################

######################## PROJECTS CRUD #############################################
    path('runningProjects/',views.runningProjects,name="runningproject"),
    path('add_Projects/<project_title>',views.add_running_projects,name="add_Projects"),
    path('<id>/updateproject', views.update_project ),
    path('<id>/deleteproject', views.delete_project ),
    path('<project_title>/download-zip/', download_zip, name='download_zip'),
    path('review_project/<project_title>/', views.review_project, name='review_project'),
    path('accept_project/<project_title>/', views.accept_project, name='accept_project'),

######################## PROJECTS CRUD END#############################################
    path('bulkUpload/',views.bulk_upload,name='bulkUpload'),
    path("upload_csv/",views.upload_csv,name='upload_csv'),
    path("download_csv/",views.download_csv,name="download_csv"),

###################### LEADER ##########################################################
    path('assign_dev/<proid>',views.assign_dev,name='assign_dev'),
    path('assigned_dev/<proid>/<devid>',views.assigned_dev,name='assigned_dev'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
