from django.shortcuts import render, redirect

# Create your views here.

from .forms import DocumentForm
from django.contrib import messages
from .models import Document
from django.contrib.auth.decorators import login_required

@login_required
def document_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = form.save(commit=False)
            newdoc.user = request.user
            newdoc.save()
            messages.success(request, 'Successful upload')  # Add success message
            return redirect('document_upload')
    else:
        form = DocumentForm()

    documents = Document.objects.filter(user=request.user)  # Get user's documents
    return render(request, 'upload.html', {'form': form, 'documents': documents})


from .forms import SignUpForm
from django.contrib.auth import login, authenticate

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('document_upload')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
