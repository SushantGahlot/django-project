from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse, Http404
from django.views.generic.base import View
from .models import Invoice
from .cache_helper import get_cache_frequency, set_cache_frequency


# This view checks if a company exists in the database
class VerifyCompany(View):
    def get(self, request, company_name):
        if not len(company_name.strip()) or not Invoice.objects.filter(company_name=company_name).exists():
            raise Http404
        return HttpResponse(status=200)


# This view is responsible for getting the frequency of how many times two companies
# have had business with each other
class GetCommercialRelationship(View):
    def get(self, request, first_company, second_company):
        if first_company == second_company:
            return HttpResponseBadRequest("Companies can not be same")

        first_company = first_company.strip()
        second_company = second_company.strip()

        if not len(first_company) or not len(second_company):
            return HttpResponseBadRequest("Please enter valid companies")

        # Get count from cache
        count = get_cache_frequency(first_company, second_company)

        # If count is not cached, get them from database
        if count is None:
            first_company_as_vendor = Invoice.objects.filter(
                company_name=second_company,
                vendor_name=first_company).count()
            second_company_as_vendor = Invoice.objects.filter(
                company_name=first_company,
                vendor_name=second_company).count()
            count = first_company_as_vendor + second_company_as_vendor
            # And set the cache
            set_cache_frequency(first_company, second_company, count)

        return JsonResponse({
            "frequency": count
        })
