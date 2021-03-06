from django.http import HttpResponse, Http404, HttpResponseRedirect
from ChitChat.models import Message
from django.shortcuts import render
from ChitChat.forms import CreateForm, SearchForm
from django.db.models.base import ObjectDoesNotExist

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
		try:
			kids = Message.objects.filter(parent_id=msg.id)
		except ObjectDoesNotExist:
			kids = None
		try:
			parent = Message.objects.get(id=msg.parent_id)
		except ObjectDoesNotExist:
			parent = None
		return render(request,'singleMessage.html',{'message':msg,'children':kids,'parent':parent})
	except ObjectDoesNotExist:
		return HttpResponse("No Message Found")

def message_getall(request):
	try:
		all_msg = Message.objects.all()[:8]	#limit to 20
	except:
		all_msg = ({'user':'-','text':'N/A','id':'-1'},)
	return render(request,'allMessages.html',{'messages':all_msg})

def message_search(request,*args,**kwargs):
	if request.method == 'GET':
		try:
			search_msg = Message.objects.filter(text__icontains=args[0])
		except:
			search_msg = ({'user':'-','text':'N/A','id':'-1'},)
	elif request.method == 'POST':
		try:
			search_msg = Message.objects.filter(text__icontains=request.POST.get('search'))
		except:
			search_msg = ({'user':'-','text':'N/A','id':'-1'},)
	else:
		return Http404
	return render(request,'allMessages.html',{'messages':search_msg})
	
def message_post(request, *args, **kwargs):
	#Post a new Message (via POST)
	assert request.method == 'POST'
	form = CreateForm(request.POST)
	if form.is_valid:
		nm = request.POST.get("user")
		ms = request.POST.get("message")
		new_msg = Message(user=nm,text=ms)
		if (request.POST.get("parent")):
			try:
				new_msg.parent = Message.objects.get(id=int(request.POST.get("parent")))
				new_msg.save()
				return HttpResponseRedirect('/msg/'+str(new_msg.id)+'/')
			except ObjectDoesNotExist:
				return HttpResponse("Invalid Parent ID!")
		new_msg.save()
		return HttpResponseRedirect('/msg/')
	else:
		raise Http404

def new_message(request, *args, **kwargs):
	assert request.method == 'GET'
	form = CreateForm()
	if args:
		if int(args[0]) > -1:
			#Check that the message object exists for that ID and set the return form to that.
			try: 
				msg_test = Message.objects.get(id=int(args[0]))
				if msg_test:
					form = CreateForm(initial={'parent':args[0]})
			except Message.DoesNotExist:
				pass
		
	return render(request,'newMessage.html',{'form':form})
	
def search_message(request):
	assert request.method == 'GET'
	form = SearchForm()
	return render(request,'searchMessage.html',{'form':form})
	
def show_single(request, *args, **kwargs):
	assert request.method == 'GET'
	try:
		mess = Message.objects.get(id = int(args[0]))
	except Message.DoesNotExist:
		return Http404
	return render(request,'message.html',{'msg':mess},content_type='text/plain')