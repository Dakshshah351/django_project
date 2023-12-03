from django.contrib import messages
from urllib import request
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import pending_projects as pending_project
import os
import csv
from .models import reviewModel
from django.core.files.storage import default_storage
from django.utils import timezone
from datetime import datetime, timedelta
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth import login as auth_login
from .forms.loginForm import loginform
from .models import UserModel
from .models import PasswordToken as passwordToken
from .models import RequirementModel 
from .models import reviewModel 

import random
from django.conf import settings
from os import path
from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from .forms.addRunningProjects import pending_projects
from .forms.register import CustomUserCreationForms
from .forms.register import UpdateProfile
from .forms.register import Update
from .forms.review_form import review_form

from .forms.reset_password_Form import reset_password_Form as reset_pass_form  
from .forms.change_pass_Form import change_pass_Form  
from .forms.RequirementGatheringForm import RequirementGatheringform  
from datetime import datetime

from django.contrib.auth import authenticate, login

# Create your views here.
def students(request):
    return render(request,"index.html")
def student(request):
    if request.user.roll==1:
        context={}
        userid=request.user.id
        context["notifications"] = reviewModel.objects.filter(dev_id=userid)
        return render(request,"home.html",context)
    elif request.user.roll==2:
        return render(request,"leader.html")
    else:
        return render(request,"admin.html")
def leader(request):
    return render(request,"leader.html")
def admin(request):
    return render(request,"admin.html")
def login(request):
    context={}
    form =loginform(request.POST or None)
    print(request)
    if form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]
        print(username)
        print(password)
        
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                
                auth_login(request,user)
                print("Done")
                if user.roll==1:
                    return redirect('developer') 
                elif user.roll==2:
                     return redirect('leader') 
                elif user.roll==3:
                     return redirect('admin')
            else:
                print("NOT CHECKED")

        except UserModel.DoesNotExist:
            print("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    context['form']= form

    return render(request,"login.html",context)
def home(request): 

    return render(request,"home.html",context)
#def forget_password(request):
def forgotpwdPage(request):

    print("dakasj")
    context={}
    form =reset_pass_form(request.POST or None)
    print(form)
    if form.is_valid():
        email = request.POST["email"]
    
    context['form']= form

    return render(request,"forgotpwd.html",context)

# return render(request, "forgotpwd.html")

def OTP_generate():
# token = ".join(random.choices(string.ascii_letters + string.digits, k=6)) # return token
    return str(random.randint(100000,999999))
def verify_otp(request , email): 
    if request.method == 'POST':
        otp = request.POST['otp']
        user = passwordToken.objects.filter(email=email).first()
        email= user.email
        if user.otp== otp:
            print("OTP matched")
            user.delete()
            form = change_pass_Form(request.POST or None)
            return render(request, 'resetpwd.html', {'email': email,'form':form})
        else:
            return HttpResponse("Entered OTP is not valid !! try again")
def reset_password(request):
    form =reset_pass_form(request.POST or None)
    print(form)
    if request.method == 'POST': 
        email =request.POST['email']
        print(email)

        user = UserModel.objects.filter(email=email).first()
        print(user)
        if user:
            otp =OTP_generate()
            user = UserModel.objects.get(email=email)
            token = passwordToken.objects.create( 
                email=user.email,
                otp=otp,
            )
            token.save()
            print(otp) #send the otp in email
            subject = "OTP for reset the password"
            message = f"Please verify and check the OTP for reset the password is {otp}" 
            from_email = "daksh05082004@gmail.com"
            recivers = [user.email]
            send_mail(subject, message, from_email, recivers) 
            # return HttpResponse(FOTP SENT >>>{otp}") 
            return render(request, 'otp.html', {'email': user.email})

        else:
            msg ="Provide valid email address"
            # return render(request, 'auth/forgotpwd.html', msg) 
            return HttpResponse("Email does not exists !!")

def new_password (request,email):
    if request.method == 'POST':
        password = request.POST['password']
        user = UserModel.objects.filter(email=email).first()
        pwd = make_password(password)
        chnge = UserModel.objects.filter(email=user.email).update(password=pwd)
    if chnge:
        passwordToken.objects.filter(email=email).delete()
        return redirect('login')
    else:
        return HttpResponse("Unable to reset password")    
class SignUp(CreateView):
    form_class = CustomUserCreationForms
    success_url = reverse_lazy('admin')
    template_name = 'register.html'

######################## USER CRUD START ############################################# 
def RequirementGathering(request):
    context={}
    form =RequirementGatheringform(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.INFO,'Successfully')
        return redirect('viewGathering')
    context['form']= form
    return render(request,"requirementgathering/add.html",context)
def viewGathering(request):
    context ={}
    context["viewGathering"] = RequirementModel.objects.all()

    return render(request,"requirementgathering/view.html", context)
def viewGatheringbyleader(request):
    context ={}
    context["viewGathering"] = RequirementModel.objects.all()
    context["viewGatheringbyleader"] = UserModel.objects.all()

    return render(request,"requirementgathering/viewbyleader.html", context)
def deleteGathering(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(RequirementModel,id = id)
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return redirect('viewGathering')
    return render(request, "requirementgathering/delete_view.html", context)

def updateGathering(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(RequirementModel, id = id)
    # pass the object as instance in form
    form = RequirementGatheringform (request.POST or None, instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('viewGathering')
    # add form dictionary to context
    context["form"] = form
    return render(request, "requirementgathering/update.html", context)
######################## USER CRUD END ############################################# 

######################## PROJECT CRUD START ############################################# 
def runningProjects(request):
    context ={}
    current_user = request.user
    print(current_user)
    print (current_user.id) 
    context["projects"] = RequirementModel.objects.filter(assigned_dev=current_user.id)
    data = RequirementModel.objects.filter(assigned_dev=current_user.id)
    context["cur_date"] = current_date = datetime.now() 
    print(context)
    
    return render(request,"pending_projects.html", context)
def add_running_projects(request,project_title):
    context={}
    form =pending_projects(request.POST or None, request.FILES or None)
    form_class = pending_projects
    if form.is_valid():
        
        path=str(request.user)
        if default_storage.exists(path):
            newfile = str(request.FILES['Upload_File'])
            print(newfile)
            print(form)
            newdata=form.save(commit=False)
            username = form.cleaned_data['project_title']
            newdata.project_title=project_title
            newdata.save()
            newpath=settings.MEDIA_ROOT+"\\"+path
            source = settings.MEDIA_ROOT+"\\"+"Upload_File"+"\\"+newfile
            print(source)
            # destination file path 
            dest = newpath+"\\"+newfile
            print(dest)
            os.rename(source, dest)
        else:
            newfile = str(request.FILES['Upload_File'])
            print(newfile)
            form.save()
            newpath=settings.MEDIA_ROOT+"\\"+path
            os.mkdir(newpath)
            source = settings.MEDIA_ROOT+"\\"+"Upload_File"+"\\"+newfile
            print(source)
            # destination file path 
            dest = newpath+"\\"+newfile
            print(dest)
            os.rename(source, dest)
        print("daku")
        obj = RequirementModel.objects.get(project_title=project_title)
        data=obj.project_title
        current_date = datetime.now()  # Get the current date and time
        obj.DEVdeadline=current_date
        obj.save()
        messages.add_message(request,messages.INFO,'Successfully')
        return redirect('runningproject')
    context['form']= form
    return render(request,"addProject.html",context)
def update_project(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(pending_project, id = id)
    # pass the object as instance in form
    form = pending_projects (request.POST or None,request.FILES or None,instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        query_sc = pending_project.objects.get(id=id)
        """ Deletes file from filesystem. """
        path = "/ALLPROJECT(1)/Python/first_project/first_demo1/media/"
        path1 = os.path.join(path,str(query_sc.Upload_File))
        os.remove(path1)
        form.save()
        return redirect('runningproject')
    # add form dictionary to context
    context["form"] = form
    return render(request, "updateProject.html", context)
def delete_project(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(pending_project,id = id)
    if request.method =="POST":
        query_sc = pending_project.objects.get(id=id)
        """ Deletes file from filesystem. """
        path = "/ALLPROJECT(1)/Python/first_project/first_demo1/media/"
        path1 = os.path.join(path,str(query_sc.Upload_File))
        os.remove(path1)
        obj.delete()
        return redirect('runningproject') 
    return render(request, "delete_project.html", context)
def download_zip(request,project_title):
    # Define the path to the ZIP file
    
    print(project_title)
    query_sc = pending_project.objects.filter(project_title=project_title).first()
    if query_sc is not None:
        print(project_title)
        data=RequirementModel.objects.get(project_title=project_title)
        print(data)
        userdata=UserModel.objects.get(id=data.assigned_dev)
        print(userdata)
        print(userdata.username)


        path = "/ALLPROJECT(1)/Python/first_project/first_demo1/media/"+userdata.username+"/"
        file_name=str(query_sc.Upload_File)
        x = file_name.split("/")
        x=x[1]
        print(path)
        #path1 = os.path.join(path,str(query_sc.Upload_File))
        #print(path1)
        zip_file_path = os.path.join(path,x)
        print(zip_file_path)
        if os.path.exists(zip_file_path):
            try:

                with open(zip_file_path, 'rb') as zip_file:

                    response = FileResponse(zip_file.read(), content_type='application/zip')
                    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(zip_file_path)}"'
                    return response
            except Exception as e:
                # Handle any exceptions that might occur when reading the file
                return HttpResponse('Error while reading the file', status=500)
        else:
            return HttpResponse('File not found', status=404)
    else:
         context = {}
         context["viewGathering"] = RequirementModel.objects.all()
         context["viewGatheringbyleader"] = UserModel.objects.all()
         context["errormsg"]="Not Submitted yet"
         # add form dictionary to context
    return render(request,"requirementgathering/viewbyleader.html", context)
def accept_project(request,project_title):
        context = {}
        print(project_title)
        query_sc = pending_project.objects.filter(project_title=project_title).first()
        if query_sc is not None:
            
            context["viewGathering"] = RequirementModel.objects.all()
            print(context)
            obj = RequirementModel.objects.get(project_title=project_title)
            b = reviewModel(description="Your Project "+project_title+" is Accepted", project_title=project_title,dev_id=obj.assigned_dev)
            b.save()
            user = UserModel.objects.get(id=obj.assigned_dev)
            data=obj.project_title
            email=user.email
            subject = "Your project is accepted"
            message = f"Hello {user.first_name} Your submited project is accpeted by leader" 
            from_email = "daksh05082004@gmail.com"
            recivers = [user.email]
            send_mail(subject, message, from_email, recivers) 
            # return HttpResponse(FOTP SENT >>>{otp}") 
            context["successmsg"]="Project Accepted"
            # add form dictionary to context
            return render(request,"requirementgathering/viewbyleader.html", context)
        else:
            print("ERRRRRRROR")
            context["errormsg"]="Project Not Submited yet"
            context["viewGathering"] = RequirementModel.objects.all()

            return render(request,"requirementgathering/viewbyleader.html", context)

def review_project(request,project_title):
    
    context = {}
    query_sc = pending_project.objects.filter(project_title=project_title).first()
    if query_sc is not None:
        obj = RequirementModel.objects.get(project_title=project_title)
        current_date = datetime.now()  # Get the current date and time
        days_to_add = 5
        future_date = current_date + timedelta(days=days_to_add)  # Add 5 days to the current date
        obj.DEVdeadline=future_date
        obj.save()
        
        context["viewGathering"] = RequirementModel.objects.all()
        user = UserModel.objects.get(id=obj.assigned_dev)
        data=obj.project_title

        form = review_form(request.POST or None)
        context['form']= form
        if request.method=='POST':
            form = review_form(request.POST or None)
            if form.is_valid():
                form.project_title="daksh"
                obj = RequirementModel.objects.get(project_title=project_title)
                new_data=form.save(commit=False)
                new_data.project_title=project_title
                new_data.dev_id=obj.assigned_dev
                context["successmsg"] = "Project Reviewed"
                new_data.save()
                email=user.email
                subject = "Your project is Return for Changes"
                message = f"Hello {user.first_name} Your submited project is Rejected by leader please check notification for the changes leader wants" 
                from_email = "daksh05082004@gmail.com"
                recivers = [user.email]
                send_mail(subject, message, from_email, recivers)
                return render(request,"requirementgathering/viewbyleader.html", context)
    else:
            print("ERRRRRRROR")
            context["errormsg"]="Project Not Submited yet"
            context["viewGathering"] = RequirementModel.objects.all()

            return render(request,"requirementgathering/viewbyleader.html", context)

            
            

    return render(request,"review_form.html", context)
####################### PROJECT CRUD END ########################################################################################
class ProfileUpdate(UpdateView):
    model = UserModel
    fields = ["first_name","last_name","email","userProfile"]
    template_name = 'profile.html'
    
    success_url = reverse_lazy('developer') # This is where the user will be 
                                       # redirected once the form
                                       # is successfully filled in

    def get_object(self, queryset=None):
        '''This method will load the object
           that will be used to load the form
           that will be edited'''
        return self.request.user
    
###################### BULK UPLOAD ###############################################
def bulk_upload(request):
    return render(request,"requirementgathering/bulkUpload.html")
def upload_csv(request):
    if("GET"==request.method):
        return HttpResponse("NOT valid Method")
    csv_file=request.FILES["csv_file"]
    if not csv_file.name.endswith('.csv'):
        return HttpResponse("File Not Valid")
    if csv_file.multiple_chunks():
        return HttpResponse("Uploaded File is to big")
    file_data = csv_file.read().decode("utf-8")
    print("file_data : "+ file_data)
    lines = file_data.split("\n")
    c=len(lines)
    for i in range(0,c-1):
        print(lines[i])

        fields = lines[i].split(",")
        data_dict = {}
        data_dict["Client_name"] = fields[0]
        data_dict["project_title"]= fields[1]
        
    # Assuming the date is in the first column (index 0)
        data_dict["start_date"]= fields[2]

        original_date = datetime.strptime(data_dict["start_date"], '%d-%m-%Y')
        updated_date_str = original_date.strftime('%Y-%m-%d')
        fields[2] = updated_date_str
        data_dict["start_date"]= fields[2]
        data_dict["end_date"]= fields[3]

        original_date = datetime.strptime(data_dict["end_date"], '%d-%m-%Y')
        updated_date_str = original_date.strftime('%Y-%m-%d')
        fields[3] = updated_date_str
        
        data_dict["end_date"]= fields[3]
        data_dict["Client_email"]= fields[4]
        data_dict["project_Description"]= fields[5]
        data_dict["project_Technology"]= fields[6]


        cform=RequirementGatheringform(data_dict)
        print(cform)
        if cform.is_valid():
            print("in if")
            cform.save()
        else:
            for field, errors in cform.errors.items():
                for error in errors:
                    print(error)
    return redirect("viewGathering")
def download_csv(request):
    response = HttpResponse()
    response['Content-Disposition']= 'attachment;filename=client_info.csv'
    writer=csv.writer(response)
    writer.writerow(['Client_name','project_title','start_date','end_date','Client_email','project_Description','project_Technology'])
    for data in RequirementModel.objects.all():
        writer.writerow([data.Client_name,data.project_title,data.start_date,data.end_date,data.Client_email,data.project_Description,data.project_Technology])
    return response
def assign_dev(request,proid):
    context ={}
    data = UserModel.objects.filter(roll=1)
    idset=proid
    return render(request,"assign_dev_view.html", {'ids': idset,'category':data})
def assigned_dev(request,devid,proid):
    context ={}
    print(devid)
    print(proid)
    context["category"] = UserModel.objects.filter(roll=1)
    # fetch the object related to passed id
    obj = RequirementModel.objects.get(id=devid)
    user_details = UserModel.objects.get(id=proid)
    user_details.Assigned_by = request.user.id
    user_details.save()
    data=obj.project_title
    current_date = datetime.now()  # Get the current date and time
    days_to_add = 5
    future_date = current_date + timedelta(days=days_to_add)  # Add 5 days to the current date
    email=user_details.email
    obj.DEVdeadline=future_date
    obj.assigned_dev = proid
    obj.save()
    user = UserModel.objects.get(email=email)
    subject = "You are Assigned"
    message = f"Hello {user.first_name} You are assigned in project of Mr.{obj.Client_name} you need to complete your task in next 5 days and submit it " 
    from_email = "daksh05082004@gmail.com"
    recivers = [user.email]
    send_mail(subject, message, from_email, recivers) 
    # return HttpResponse(FOTP SENT >>>{otp}") 
    context["successmsg"]="Developer Assigned"
    # add form dictionary to context
    return render(request,"assigned_dev_view.html", context)
def developerrecords(request):
    userid=request.user.id
    user_details = UserModel.objects.get(id=userid)
    context = {}
    tech = user_details.technology
    x = tech.split(",")
    lenx=len(x)
    print(x)
    context["lenx"] = x 
    # context["length"] = range(lenx) 
    
    context["developers"] = UserModel.objects.filter(roll=1,Assigned_by=request.user.id)
    for data in range(lenx):
        print()
        da = "dak"
        context[x[data]] = UserModel.objects.filter(roll=1,Assigned_by=request.user.id,technology=x[data])
        # context["all_xo"] = RequirementModel.objects.filter(project_Technology=x[data])
        print(context)
    return render(request,"developerrecords.html", context)




