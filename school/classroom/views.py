from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, \
    DetailView, UpdateView, DeleteView

from classroom.models import Teacher
from classroom.forms import ContactForm

# Create your views here.


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # success URL?, NOT template.html
    success_url = reverse_lazy('classroom:thank_you')

    # what to do with form?
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class TeacherCreateView(CreateView):
    model = Teacher
    fields = "__all__"

    success_url = reverse_lazy('classroom:thank_you')


class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teacher_list'

    # queryset = Teacher.objects.all() # This is the default, can be overridden


class TeacherDetailView(DetailView):
    # Return only 1 model entry
    # Look for model_detail.html
    model = Teacher
    # PK --> {{teacher}}


class TeacherUpdateView(UpdateView):
    # Shares model_form.html with CreateView
    model = Teacher
    # fields = ['last_name']
    fields = "__all__"

    success_url = reverse_lazy('classroom:teacher_list')

class TeacherDeleteView(DeleteView):
    # form --> Confirm Delete Button
    # model_confirm_delete.html
    model = Teacher
    success_url = reverse_lazy('classroom:teacher_list')
