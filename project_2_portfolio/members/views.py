from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from .models import Member, user_port
from .forms import YourForm
import os

# def members(request):
#   template = loader.get_template('user.html')
#   return HttpResponse(template.render())

def members(request):
    members_list = user_port.objects.all()
    return render(request, 'user.html', {'members': members_list})

def filter_user(request, optional_param=None):
    sanyosh_members = user_port.objects.filter(firstname=optional_param)
    for member in sanyosh_members:
        firstname = member.firstname 
        lastname = member.lastname 

        if firstname:
            if len(firstname) > 5:
                print(f"{firstname} meets the condition")
            else:
                print(f"{firstname} does not meet the condition")
        else:
            print("No firstname found for the member")

    return render(request, 'user.html', {'sanyosh_members': firstname, 'lastname': lastname,'array':sanyosh_members})

def index(request):
    return render(request, 'index.html', {'title': "Add User"})

# def view_member(request, pk=None):
#     return HttpResponse(pk)

def create_user(request):
    try:
        if request.method == 'POST' and request.FILES['image']:
            # Retrieve form data from request.POST
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            location = request.POST.get('location')
            contact = request.POST.get('contact')
            language = request.POST.get('language')
            skill = request.POST.get('skill')
            work_expirence = request.POST.get('work_expirence')
            education = request.POST.get('education')
            project = request.POST.get('project')
            link = request.POST.get('link')
            summary = request.POST.get('summary')
            image = request.FILES['image']
       

            # Save the form data to the database
            user_details = user_port(
                firstname=first_name,
                lastname=last_name,
                email=email,
                location=location,
                contact=contact,
                language=language,
                skill=skill,
                work_expirence	=work_expirence,
                education=education,
                project=project,
                link=link,
                summary=summary,
                image=image
            )
            user_details.save()

            # Redirect to a success page or display a success message
            return redirect('members')  # Replace 'success_page' with the actual URL name

    except Exception as e:
        # Catch any exceptions and print the error message
        print(f"An error occurred: {e}")

    return render(request, 'user.html')

def delete_member(request, pk=None):
    if pk is not None:
        member = get_object_or_404(user_port, pk=pk)
        member.delete()
        return HttpResponse(f'Member with pk={pk} has been deleted.')
    else:
        return HttpResponse('No member specified for deletion.')    
 