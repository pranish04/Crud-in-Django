from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Employee, Qualification

class EmployeeListView(View):
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, 'employee/homepage.html', {'employees': employees})

class EmployeeDetailView(View):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        return render(request, 'employee/detail.html', {'employee': employee})

class EmployeeCreateView(View):
    def get(self, request):
        qualifications = Qualification.objects.all()
        return render(request, 'employee/create.html', {'qualifications': qualifications})

    def post(self, request):
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        qualification_ids = request.POST.getlist('qualification')

        employee = Employee.objects.create(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            address=address,
            email=email,
            mobile=mobile
        )
        employee.qualifications.set(qualification_ids)

        return redirect('employee_list')

class EmployeeUpdateView(View):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        qualifications = Qualification.objects.all()
        selected_qualifications = employee.qualifications.values_list('id', flat=True)
        return render(request, 'employee/update.html', {'employee': employee, 'qualifications': qualifications, 'selected_qualifications': selected_qualifications})

    def post(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)

        employee.first_name = request.POST.get('first_name')
        employee.middle_name = request.POST.get('middle_name')
        employee.last_name = request.POST.get('last_name')
        employee.address = request.POST.get('address')
        employee.email = request.POST.get('email')
        employee.mobile = request.POST.get('mobile')
        qualification_ids = request.POST.getlist('qualification')

        employee.qualifications.set(qualification_ids)
        employee.save()

        return redirect('employee_detail', pk=pk)

class EmployeeDeleteView(View):
    def post(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return redirect('employee_list')
