from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from apps.account.models import Account, Work, AddToGroup, WorkResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from apps.account.forms import UserForm, AccountForm, AccountWork, AccountGroup, \
AccountAddToGroup, AccountWorkResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def create_account(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        account_form = AccountForm(request.POST)
        if user_form.is_valid() and account_form.is_valid():
            user = user_form.save()
            user.account.user = user
            user.account.rol = account_form.cleaned_data['rol']
            user.account.save()
            return redirect('account:login')
    else:
        user_form = UserForm()
        account_form = AccountForm()
    return render(request, 'account/registro.html', {
        'user_form': user_form,
        'account_form': account_form
    })


@login_required(login_url='/account/login/')
def account_index(request):
    ret = User.objects.filter(username=request.user.username).values_list('account__rol', flat=True)
    p = AddToGroup.objects.filter(user_add=request.user.username).values_list('name', flat=True)
    v = ''
    for r in ret:
        r

    if r == 'Profesor':

        user_id_list = WorkResponse.objects.filter(user_response=request.user.username).values_list('user', \
            flat=True)

        title_list = WorkResponse.objects.filter(user_response=request.user.username).values_list('title', \
            flat=True)

        group_list = WorkResponse.objects.filter(user_response=request.user.username).values_list('group', \
            flat=True)

        id_lista = WorkResponse.objects.filter(user_response=request.user.username).values_list('id', \
            flat=True)

        if user_id_list.exists():

            for user_id in user_id_list:
                user_id

            nombre_lista = User.objects.filter(id=user_id).values_list('username', flat=True)  

            for nombre in nombre_lista:
                nombre

            for title in title_list:
                title

            for group in group_list:
                group

            for id_tarea in id_lista:
                id_tarea

            return render(request, 'account/inicio.html', {'r':r, 'nombre':nombre, 'title':title, \
                'group':group, 'id_tarea':id_tarea})

        else:

            res = 0

            return render(request,  'account/inicio.html', {'r':r, 'res':res})

    else:

        for v in p:
            v

        titulo_lista = Work.objects.filter(group=v).values_list('title', flat=True)
        grupo_lista = Work.objects.filter(group=v).values_list('group', flat=True)
        id_usuario = Work.objects.filter(group=v).values_list('user', flat=True)
        id_tarea_lista = Work.objects.filter(group=v).values_list('id', flat=True)

        if id_usuario.exists():

            for user in id_usuario:
                user

            nombre_lista = User.objects.filter(id=user).values_list('username', flat=True)  

            for nombre in nombre_lista:
                nombre

            for titulo in titulo_lista:
                titulo

            for grupo in grupo_lista:
                grupo

            for id_tarea in id_tarea_lista:
                id_tarea

            return render(request, 'account/inicio.html', {'r': r, 'nombre':nombre, 'titulo':titulo, 'grupo':grupo, 'id_tarea':id_tarea})

        else:

            res = 0

            return render(request, 'account/inicio.html', {'res':res})

def account_close(request):
    logout(request)
    return redirect('account:login')

@login_required(login_url='/account/login/')
def account_tarea(request):
	u = User.objects.filter(username='Raul').values_list('group__name')
	for p in u:
		p
	if request.method == 'POST':
		form = AccountWork(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect('account:tarea')
	else:
		form = AccountWork()
	return render(request, 'account/tarea.html', {'form':form, 'p':p})

@login_required(login_url='/account/login/')
def account_grupo(request):
    if request.method == 'POST':
        form = AccountGroup(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('account:grupo')
    else:
    	form = AccountGroup()
    return render(request, 'account/grupo.html', {'form':form})

@login_required(login_url='/account/login/')
def account_add_to_group(request):
    u = User.objects.filter(username='Raul').values_list('group__name')
    for p in u:
        p
    if request.method == 'POST':
        form = AccountAddToGroup(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('account:add_to_grupo')
    else:
        form = AccountAddToGroup()
    return render(request, 'account/add_to_grupo.html', {'form':form, 'p':p})

@login_required(login_url='/account/login/')
def account_ver(request):
    res = User.objects.filter(username=request.user.username).values_list('account__rol', flat=True)

    for r in res:
        r

    id_tarea = request.POST.get('id')
    nombre = request.POST.get('nombre')

    if r == 'Profesor':

        tarea_res = WorkResponse.objects.filter(id=id_tarea).values_list('title', 'description', \
            'group', 'archive')

        return render(request, 'account/ver.html', {'r':r, 'nombre':nombre, 'tarea_res':tarea_res})

    else:
        tarea = Work.objects.filter(id=id_tarea).values_list('title', 'description', 'group', 'archive')
        if request.method == 'POST':
            form = AccountWorkResponse(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return redirect('account:ver')
        else:
            form = AccountWorkResponse()
        return render(request, 'account/ver.html', {'r':r, 'form':form, 'tarea':tarea, 'nombre':nombre})