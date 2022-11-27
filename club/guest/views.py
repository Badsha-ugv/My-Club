from django.shortcuts import render,redirect
from user_account.models import CustomUser
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,login,logout 
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

#from this app model 
from .models import Project,People,Award,Image,Comment,Award,ProjectImage

from dev_club.models import DevFund,DevEvent #from dev_club import DevFund
from pro_club.models import Fund,Due,Event #from pro_club import  Fund 


def home(request):
    return render(request,'guest/home.html')


def guest_logout(request):
    logout(request) 
    return redirect('home')


def project(request):
    project_list = Project.objects.all().order_by('-publish_date')
    dict = {
        'projects': project_list,
    }
    return render(request,'guest/project.html',dict)

def people(request):
    people = People.objects.all() 
    dict = {
        'people': people,
    }
    return render(request,'guest/people.html',dict)

def award(request):
    award_list = Award.objects.all()
    dict = {
        'awards': award_list,
    }
    return render(request,'guest/award.html',dict)

def award_view(request,id):
    award = Award.objects.get(id=id)
    dict = {
        'awards': award,
    }
    return render(request,'guest/award_view.html',dict)  

def gallery(request):
    image = Image.objects.all()
    return render(request,'guest/gallery.html',{'images':image})


def profile(request,id):
    p_member_list = CustomUser.objects.filter(club_name= 'PROGRAMMING')
    d_member_list = CustomUser.objects.filter(club_name= 'DEVELOPMENT')
    p_event = Event.objects.filter(event_status='UPCOMMING')
    d_event = Event.objects.filter(event_status='UPCOMMING')


    user = CustomUser.objects.get(id=id)
   
    stu_id = user.student_id
  
    

    # my_due = Due.objects.get(member = user) 
    my_due,created = Due.objects.get_or_create(member = user)
    

    print('my due',my_due.ammount) 

    dev_club_fund = DevFund.objects.all()[0]

    pro_club_fund = Fund.objects.all()[0] 

    project = Project.objects.filter(user=user)
    

    dict = {
        'user':user,
        'dev_fund':dev_club_fund,
        'pro_fund':pro_club_fund,
        'project':project,
        'my_due':my_due,
        'p_member_list': p_member_list,
        'd_member_list':d_member_list,
        'p_event':p_event,
        'd_event':d_event,
    }
    if user.id != request.user.id:
        return HttpResponse('You Have no Access! Please go back :|')
    else:
        return render(request,'guest/profile.html',dict)


def create_project(request):
    user = request.user
    if request.method == 'POST':
        p_name = request.POST.get('p_name')
        p_desc = request.POST.get('p_desc')
        p_image = request.FILES.get('p_image')
        more_image = request.FILES.getlist('more_image')


        project = Project (
            user = user,
            project_name=p_name,
            project_description = p_desc,
            image = p_image,
        )
        project.save() 
        for image in more_image:
            ProjectImage.objects.create(project=project, image=image)

        return redirect('/')

    return render(request,'guest/create_project.html')


def project_view(request,id):
    project = Project.objects.get(id=id) 
    comment = Comment.objects.filter(project=project).order_by('-id')
    more_image = ProjectImage.objects.filter(project=project)

    if request.method == 'POST':
        cmt = request.POST.get('comment_text')
        comment_text = Comment(
            user = request.user,
            project = project,
            text = cmt,
        )
        comment_text.save() 
        return HttpResponseRedirect(request.path_info)
        
    dict = {
        'comment':comment,
        'project':project,
        'more_image':more_image,
    }
    return render(request,'guest/view_project.html',dict) 


def update_profile(request,id):
    user = CustomUser.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')   
        student_id = request.POST.get('stu_id')
        password = request.POST.get('password')
        image  = request.FILES.get('img') 


        
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.phone_number = phone
        user.student_id = student_id

        if image != None and image != '':
            user.profile_pic = image


        if password != None and password != '':
            user.set_password(password)
        user.save() 
        messages.success(request,'Profile Update Successfully')
        return redirect(request.path_info)
    # access control 
    if user.id != request.user.id:
        return HttpResponse('Go Back :|')
    dict = {
        'user': user,
    }
    return render(request,'guest/update_profile.html',dict)