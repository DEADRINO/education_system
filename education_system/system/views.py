
from django.http import HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView
from .models import Product
from .forms import ProductForm


class CreatePostView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'system/product_form.html'
    permission_required = 'system.create_product'
    fields = ('name', 'content', 'author', 'start_date', 'price')

    def form_valid(self, form):
        if self.has_permission():
            return super().form_valid(form)
        else:
            return HttpResponse(status=403)
