
from django.views import generic


from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View
# from .forms import CheckoutForm, CouponForm, RefundForm, PaymentForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

# not using request
# class HomeView(ListView):
#     model = Customer
#     template_name = 'home.html'
#
#     # categories drop down : pass context
#     def get_context_data(self, *args, **kwargs):
#         cat_menu = Tag.objects.all()
#         context = super(HomeView, self).get_context_data(*args, **kwargs)
#         context["cat_menu"] = cat_menu
#         return context

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login') #after registration you will want to login.


class HomeView(ListView):
    model = Tutorial
    # paginate_by = 10
    template_name = "home.html"

class success(ListView):
    model = Tutorial
    template_name = "success.html"


#class CurriculumSummaryView(LoginRequiredMixin, View):

# @login_required
# class CurriculumSummaryView(LoginRequiredMixin, View):
#     def get(self, *args, **kwargs):
#         try:
#             order = Curriculum.objects.get(customer=self.request.user)
#             context = {
#                 'object': order
#             }
#             return render(self.request, 'curriculum_summary.html', context)
#         except ObjectDoesNotExist:
#             messages.warning(self.request, "You do not have an active curriculum")
#             return redirect("/")

class ItemDetailView(DetailView):
    model = Tutorial
    template_name = "product.html"


    # if cur exists -> choose cur
    # else create cur
    #simpler version. each customer only can have one curriculum.




# def add_to_cart(request, slug):
#     item = get_object_or_404(Tutorial, slug=slug)
#     curriculum_order_item, created = CurriculumItem.objects.get_or_create(tutorial=item, customer=request.customer.user) #needs to match with model
#     curriculum_order_qs = Curriculum.objects.filter(customer=request.customer.user)
#
#     if curriculum_order_qs.exists():
#         order_curriculum = curriculum_order_qs[0] #defualt cuurriculum , usually only one cart exists (but I willl have multiple curriculums later)
#         # check if the curriculum order_itme/curr_item is in the order/curriculum
#         if order_curriculum.items.filter(item__slug=item.slug).exists():  #tutorial exists in the curriculum
#             messages.info(request, "This tutorial item already exists in your curriculum.")
#             # return redirect("cart:curriculum-summary")
#             return redirect("success")
#         else:   #curriculum needs to be created
#             order_curriculum.items.add(curriculum_order_item)
#             messages.info(request, "This tutorial was added to your curriculum.")
#             return redirect("success")
#     else:
#         ordered_date = timezone.now()
#         order = Curriculum.objects.create(
#             customer=request.customer.user, date_created=ordered_date)
#         order.items.add(curriculum_order_item)
#         messages.info(request, "This tutorial item was added to your curriculum.")
#         return redirect("success")
#
#         # messages.info(request, "This item was added to your cart.")
#         # return redirect("cart:product")
#
#
#
# def remove_from_cart(request, slug):
#     item = get_object_or_404(Tutorial, slug=slug)
#     order_qs = Curriculum.objects.filter(customer=request.user) # request user for logged in user/https://stackoverflow.com/questions/60710808/wsgirequest-object-has-no-attribute-customuser
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order item is in the order
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item = CurriculumItem.objects.filter(
#                 tutorial=item,
#                 customer=request.customer.user,
#             )[0]
#             order.items.remove(order_item)
#             order_item.delete()
#             messages.info(request, "This item was removed from your cart.")
#             return redirect("success")
#         else:
#             messages.info(request, "This item was not in your cart")
#             return redirect("success")
#     else:
#         messages.info(request, "Your curriculum is empty")
#         return redirect("success")




