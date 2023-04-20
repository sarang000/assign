"""insurancemgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Insurance import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.showCssLoginPage),

    path('adminlogin/',views.AdminPage),
    path('adminLoginpage/',views.AdminPageDetails),

    path('adminorg/',views.AdminOrgReg),

    path('adminbranch/',views.AdminBranch),
    path('adminbranchorg/',views.AdminBranchOrg),

    path('adminorgmodifi/',views.AdminOrgModifi),
    path('adminModification/',views.AdminOrgModification),

    path('adminagent/',views.AdminAgent),
    path('adminagentdetails/',views.AdminAgentDetails),

    path('admindelete/',views.AdminDelete),

    path("companyofficals/",views.CompanyOffical),
    path("companyofficalsreg/",views.CompanyOfficalsRegistration),

    path("companyorgreg/",views.CompanyOrgRegistration),

    path("companypolicyreg/",views.CompanyPolicyRegistration),

    path("companypolicyviewdetails/",views.CompanyViewPolicyDetails),

    path("companyagentreg/",views.CompanyAgentRegistration),

    path("companyagentmodification/",views.CompanyAgentModification),

    path("companycustomereg/",views.CompanyCustomerRegistration),

    path("agentlogin/",views.AgentLogin),

    path("agentreg/",views.AgentDetailsPage),

    path("agentcustomerreg/",views.AgentCustomerDetailsPage),

    path("agentcustomerpolicy/",views.AgentCustomerPolicy),

    path("agentcustomermodification/",views.AgentCustomerModification),


    path("customerlogin/",views.CustomerLogin),

    path("customerloginDetails/",views.CustomerLoginDetails),

    path("viewcustomerpolicyDetails/",views.ViewCustomerPolicyDetails),

    path("viewallpolicydetails/",views.ViewAllPolicyDetails),

    path("deletecustomeraccount/",views.DeleteCustomerAccount),
]
