from django.shortcuts import render
from .models import AdminLoginPage
from .models import CompanyOfficals
from .models import Agent
from .models import Customer
# Create your views here.


def showCssLoginPage(request):
    return render(request,"index.html")


def AdminPage(request):
    return render(request, "admin/adminstraor.html")


def AdminPageDetails(request):
    username=request.POST.get("uname")
    password=request.POST.get("psw")
    if username=='admin' and password=='admin':
        ad=AdminLoginPage(username=username,password=password)
        ad.save()
        return render(request, "admin/adminReg.html")
    else:
        return render(request, "admin/adminstraor.html")


def AdminOrgReg(request):
    date=request.POST.get("date")
    organsation_name=request.POST.get("organisation name")
    branch_name=request.POST.get("branch")
    organsation_address=request.POST.get("address")
    branch_id=request.POST.get("branch id")
    branch_code=request.POST.get("branch code")
    password=request.POST.get("psw")
    password1=request.POST.get("psw-repeat")
    return render(request, "admin/adminOrganisationReg.html")


def AdminBranch(request):
    date=request.POST.get("date")
    branch_id=request.POST.get("branch id")
    branch_name=request.POST.get("branch name")
    branch_code=request.POST.get("branch code")
    branch_address=request.POST.get("branch address")
    branch_location=request.POST.get("branch location")
    password=request.POST.get("psw")
    repeat_password=request.POST.get("psw-repeat")
    return render(request, "admin/adminbranchRegistration.html")

def AdminBranchOrg(request):
    return render(request, "admin/adminbranchRegistration.html")

def AdminOrgModifi(request):
    date=request.POST.get("date")
    organisation_name =request.POST.get("name")
    branch=request.POST.get("branch")
    address=request.POST.get("address")
    branch_id=request.POST.get("branch id")
    branch_code=request.POST.get("branch code")
    password=request.POST.get("psw")
    repeat_password=request.POST.get("psw -repeat")
    return render(request, "admin/adminOrgModification.html")


def AdminOrgModification(request):
    return render(request, "admin/adminOrgModification.html")


def AdminAgent(request):
    return render(request, "admin/adminAgentDetails.html")

def AdminAgentDetails(request):
    agent_id =request.POST.get("agent id")
    agent_name =request.POST.get("name")
    father_name =request.POST.get("father name")
    age =request.POST.get("age")
    sex =request.POST.get("sex")
    occupation =request.POST.get("occupation")
    address =request.POST.get("address")
    password =request.POST.get("psw")
    repeat_password =request.POST.get("pws-repeat")
    return render(request, "admin/adminAgentDetails.html")


def AdminDelete(request):
    return render(request, "admin/delete.html")


def CompanyOffical(request):
    return render(request,"companyOfficals/companyofficals.html")

def CompanyOfficalsRegistration(request):
    username=request.POST.get("uname")
    password=request.POST.get("psw")
    id=request.POST.get("id")
    if username=='company' and password=='company':
        co=CompanyOfficals(username=username,password=password,id=id)
        co.save()
        return render(request, "companyOfficals/companyreg.html")
    else:
        return render(request, "companyOfficals/companyofficals.html")


def CompanyOrgRegistration(request):
    date = request.POST.get("date")
    organsation_name =request.POST.get("name")
    branch_id =request.POST.get("branch id")
    branch_name = request.POST.get("branch name")
    branch_code = request.POST.get("branch code")
    address = request.POST.get("address")
    password = request.POST.get("psw")
    repeat_password = request.POST.get("psw - repeat")
    return render(request, "companyOfficals/company_OrgRegistration.html")


def CompanyPolicyRegistration(request):
    date =request.POST.get("date")
    policy_name =request.POST.get("name")
    policy_Amount =request.POST.get("amount")
    interest =request.POST.get("interest")
    bonus_rate =request.POST.get("bonus rate")
    policy_team =request.POST.get("policy team")
    bonus_period =request.POST.get("bonus period")
    policy_expiry_date =request.POST.get("policy expiry date")
    password =request.POST.get("psw")
    repeat_password =request.POST.get("pws - repeat")
    return render(request, "companyOfficals/company_policyReg.html")


def CompanyViewPolicyDetails(request):
    return render(request, "companyOfficals/companyViewPolicyDetails.html")


def CompanyAgentRegistration(request):
    return render(request,"companyOfficals/companyAgent.html")


def CompanyAgentModification(request):
    return render(request,"companyOfficals/companyAgentModification.html")


def CompanyCustomerRegistration(request):
    return render(request,"companyOfficals/CompanycustomerRegistration.html")


def AgentLogin(request):
    username=request.POST.get("uname")
    password=request.POST.get("psw")
    id=request.POST.get("id")
    if username=='agent' and password=='agent':
        a=Agent(username=username,password=password)
        a.save()
        return render(request,"agent/agent.html")
    else:
        return render(request,"agent/agentLogin.html")


def AgentDetailsPage(request):
    return render(request,"agent/agent.html")


def AgentCustomerDetailsPage(request):
    return render(request,"agent/agentCustomerDetails.html")


def AgentCustomerPolicy(request):
    return render(request,"agent/agentcustomerpolicydetails.html")


def AgentCustomerModification(request):
    return render(request,"agent/agentcustomermodification.html")


def CustomerLogin(request):
    return render(request,"customer/customerLogin.html")


def CustomerLoginDetails(request):
    username=request.POST.get("uname")
    password=request.POST.get("psw")
    id=request.POST.get("Branch id")
    if username=='customer' and password=='customer':
        c=Customer(username=username,password=password,id=id)
        c.save()
        return render(request,"customer/customerreg.html")
    else:
        return render(request,"customer/customerLogin.html")


def ViewCustomerPolicyDetails(request):
    return render(request,"customer/viewcustomerpolicydetails.html")


def ViewAllPolicyDetails(request):
    return render(request,"customer/viewAllpolicyDetails.html")


def DeleteCustomerAccount(request):
    return render(request,"customer/deletecustomeraccount.html")


