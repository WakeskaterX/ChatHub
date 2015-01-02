from django.http import HttpResponse, Http404, HttpResponseRedirect
from ChitChat.models import Message
from django.shortcuts import render
from ChitChat.forms import CreateForm

#Routes Views based on GET, POST, PUT, or DELETE
#Views Specified must be set to the correct Action in KWARGS
def router(request, *args, **kwargs):
	get_view = kwargs.pop('GET',None)
	post_view = kwargs.pop('POST',None)
	put_view = kwargs.pop('PUT',None)
	delete_view = kwargs.pop('DELETE',None)
	if request.method == 'GET' and get_view is not None:
		return get_view(request, *args, **kwargs)
	elif request.method == 'POST' and post_view is not None:
		return post_view(request, *args, **kwargs)
	elif request.method == 'PUT' and put_view is not None:
		return put_view(request, *args, **kwargs)
	elif request.method == 'DELETE' and delete_view is not None:
		return delete_view(request, *args, **kwargs)
	raise Http404

def message_get(request, *args, **kwargs):
	try:
		msg = Message.objects.get(id=int(args[0]))	
		return render(request,'allMessages.html',{'messages':(msg,)})
	except:
		return HttpResponse("No Message Found")

def message_getall(request):
	try:
		all_msg = Message.objects.all()
	except:
		all_msg = ({'user':'-','text':'N/A','id':'-1'},)
	return render(request,'allMessages.html',{'messages':all_msg})

def message_post(request, *args, **kwargs):
	#Post a new Message (via POST)
	assert request.method == 'POST'
	form = CreateForm(request.POST)
	if form.is_valid:
		nm = request.POST.get("user")
		ms = request.POST.get("message")
		new_msg = Message(user=nm,text=ms)
		new_msg.save()
		return HttpResponseRedirect('/msg/')
	else:
		raise Http404

def new_message(request):
	assert request.method == 'GET'
	form = CreateForm()
	return render(request,'newMessage.html',{'form':form})
	