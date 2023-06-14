from django.shortcuts import render


# Create your views here.
def example_view(request):
    # Under my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')

def variable_view(request):
    my_var = {
        'first_name':'rosalind',
        'last_name':'fraNKLin',
        'some_list':[1,2,3],
        'some_dictionary':{'inside_key':'inside_value'},
        'logged_in': True,
    } # Through the context var, my_vare will be passed through

    return render(request, 'my_app/variable.html', context=my_var)