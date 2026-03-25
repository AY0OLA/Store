from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from item.models import Items
from .models import Conversation
from .forms import ConversationMessageForm


@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Items, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Conversation.objects.filter(item=item, members=request.user)

    if conversations.exists():
        return redirect('conversation:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user, item.created_by)

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('conversation:detail', pk=conversation.id)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {
        'form': form
    })

    item = get_object_or_404(Items, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Conversation.objects.filter(item=item).filter(members=[request.user.id])

    if conversations:
        pass # redirect to conversation

    if request.method == 'POST':
        form =ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation= Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
    
    else:
        form = ConversationMessageForm()
    
    return render(request,'coversation/new.html',{
        'form': form
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members=request.user)

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })

@login_required
def detail(request, pk):
    conversations = Conversation.objects.filter(members=[request.user.id]).get(pk=pk)

    if request.method == 'POST'
        form = ConversationMessageForm(request.POST)

        if form.is_vaild:
            conversation_message = form.save(commit=False)
            conversation_message.conversation
            conversation_message.created_by = request.user

            conversation.save()

            return redirect('conversation/detail.html',pk=pk)

    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html',{
        'conversations': conversations ,
        'forms':form
    })
