from django.shortcuts import render,redirect
from django.http import HttpResponse    
from .models import  DevEvent,DevDue, DevFund,DevExpense, DevPayment
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.http import HttpResponseRedirect

from user_account.models import CustomUser
from guest.models import Image,Award
# Create your views here.


def user_type_cehck(CustomUser):
    return CustomUser.club_name == 'DEVELOPMENT' and CustomUser.user_type != 'MEMBERS'

@login_required(login_url='pc_login')
@user_passes_test(user_type_cehck, login_url='home')
def dev_dashboard(request):
    member = CustomUser.objects.filter(club_name='DEVELOPMENT')
    all_member = member.count()
    
    total_fund, created = DevFund.objects.get_or_create()

    if created:
        total_fund = total_fund[0]

    expense = DevExpense.objects.all()
    total_expense = 0
    for i in expense:
        total_expense = total_expense + i.expense_amount
    # print(total_expense)
    event_list = DevEvent.objects.filter(event_status='UPCOMMING').count()

    dict = {
        'member': member,
        'all_member': all_member,
        'total_fund': total_fund,
        'total_expense': total_expense,
        'event_list': event_list,

    }
    return render(request,'dev_club/dev_dashboard.html',dict)
    # return HttpResponse('Develomment Club Dashboard')




@login_required(login_url='pc_login')
@user_passes_test(user_type_cehck, login_url='home')
def dev_make_payment(request):

    member = CustomUser.objects.filter(club_name='DEVELOPMENT')

    if request.method == 'POST':
        stu_id = request.POST.get('student_id')
        pay = request.POST.get('pay_ammount')
        due = request.POST.get('due_ammount')
        date = request.POST.get('pay_date')

        pay_member = CustomUser.objects.get(student_id=stu_id)

         # due per member
        due_obj,created = DevDue.objects.get_or_create(member=pay_member)
        
        due_obj.ammount += int(due) 
        due_obj.date = date 
        due_obj.save()

        add_to_fund = DevFund.objects.all()[0]

        add_amount = int(add_to_fund.total) + int(pay)
        add_amount = str(add_amount)
        add_to_fund.total = add_amount
        add_to_fund.save()

        payment = DevPayment(
            member=pay_member,
            pay_amount=pay,
            due_amount=due,
            pay_date=date,

        )
        payment.save()
        messages.success(request, 'Payment Added Successfully')
        return redirect('dev_make_payment')

    dict = {
        'member': member,
    }
    return render(request, 'dev_club/payment_page.html', dict)


@login_required(login_url='pc_login')
@user_passes_test(user_type_cehck, login_url='home')
def dev_expense(request):
    fund = DevFund.objects.all()[0]
    if request.method == 'POST':
        expense_ammount = int(request.POST.get('ammount'))
        expense_date = request.POST.get('date')
        desc = request.POST.get('desc')
        total_fund = int(fund.total) - expense_ammount
        
        fund.total = str(total_fund)
        fund.save()

        expense = DevExpense(
            expense_amount=expense_ammount,
            date=expense_date,
            description=desc,
        )
        expense.save()
        messages.success(request, 'Expense Added Successfully')
        return redirect('dev_dashboard')

    return render(request, 'dev_club/expense.html')


@login_required(login_url='pc_login')
@user_passes_test(user_type_cehck, login_url='home')
def dev_event(request):
    if request.method == 'POST':
        event_name = request.POST.get('name')
        event_desc = request.POST.get('desc')
        starting = request.POST.get('start')
        ending = request.POST.get('end')

        # print(event_name, event_desc, starting, ending)
        event = DevEvent(
            name=event_name,
            description=event_desc,
            start_date=starting,
            end_date=ending,
        )
        event.save()
        messages.success(request, 'Event Added Successfully')
        return redirect('dev_show_event')
    return render(request, 'dev_club/event.html')


@login_required(login_url='pc_login')
@user_passes_test(user_type_cehck, login_url='home')
def dev_show_event(request):
    event_list = DevEvent.objects.all().order_by('-event_status')

    dict = {
        'event_list': event_list,
    }
    return render(request, 'dev_club/event_list.html', dict)


@login_required(login_url='pc_login')
@user_passes_test(user_type_cehck, login_url='home')
def dev_complete_event(request, id):
    event = DevEvent.objects.get(id=id)
    event.event_status = 'COMPLETE'
    event.save()
    messages.success(request, 'Event Completed Successfully')
    return redirect('dev_show_event')


@login_required(login_url='pc_login')
@user_passes_test(user_type_cehck, login_url='home')
def dev_delete_event(request, id):
    event = DevEvent.objects.get(id=id)
    event.delete()
    messages.success(request, 'Event Deleted Successfully')
    return redirect('dev_show_event')




# updated from pro_club
@login_required(login_url='pc_login')
@user_passes_test(user_type_cehck, login_url='home')
def due_list(request):
    
    
    # member = CustomUser.objects.all() 
    due = DevDue.objects.all()
    
    # due = Payment.objects.filter(payment
    dict = {
        
        'due_amount':due,
        
    }
    return render(request,'dev_club/due_list.html',dict)


@login_required(login_url='pc_login')
@user_passes_test(user_type_cehck, login_url='home')
def payment_history(request):
    payment_history = DevPayment.objects.all()
    return render(request,'dev_club/payment_history.html',{'payment_history':payment_history})

def add_gallery_image(request):
    if request.method == 'POST':
        image = request.FILES.getlist('image_file')

        for i in image:
            Image.objects.create(image=i)
        

    return render(request,'dev_club/add_gallery_image.html')


def add_award_event(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        front_img = request.FILES.get('img')
        other_img = request.FILES.getlist('others')
        desc = request.POST.get('desc')
        date = request.POST.get('date')

        award = Award(
            event_name=name,
            event_desc=desc,
            image=front_img,
            event_date=date,
        )
        # for i in other_img:
        #     award.add(other_img=i)

        award.save()
        return HttpResponseRedirect(request.path_info)

    return render(request, 'dev_club/add_award_event.html')


def create_user_account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        club_name = request.POST.get('club_name')
        student_id = request.POST.get('stu_id')
        

        user = CustomUser(
            username=username,
            club_name=club_name,
            student_id=student_id,

        )
        user.set_password(password)
        user.save()
        messages.success(request, 'User created successfully')
        return redirect('dev_dashboard')

    return render(request, 'dev_club/create_user_account.html')
