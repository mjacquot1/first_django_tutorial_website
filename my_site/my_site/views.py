from django.shortcuts import render

# Needed for a custom 404 page

def my_custom_page_not_found_view(request, exception):
    return render(request, '404.html', status=404)