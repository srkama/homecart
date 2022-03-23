from django.shortcuts import redirect, render
from django.contrib import messages
from product.models import Product
from review.models import Review

# Create your views here.
# page to get reviews
# upon sumbit we should redirect to product detail


def product_review(request, product_id):
    product=Product.objects.get(id=product_id)
    message=""
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        if rating:
            Review.objects.create(stars=rating, product=product, comment=comment)
            messages.success(request, 'Review updated successful!')
            return redirect("/")
        else:
            message="Rating is mandatory"
    return render(request, 'review.html', {'product':product, 'message': message})