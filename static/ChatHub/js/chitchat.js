function viewMessage(idNo){
	window.location.href="http://localhost:8000/msg/"+idNo+"/";
}

function newMessage(idNo){
	event.cancelBubble = true;
	if(event.stopPropagation) event.stopPropagation();
	
	window.location.href="http://localhost:8000/index/"+idNo+"/";
}