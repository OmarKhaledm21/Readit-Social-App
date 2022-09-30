from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View

from .models import UserCommunity, Community
from django.db.models import Sum
# Create your views here.


class JoinCommunityView(View):
    def get_communities(self, request):
        user_communities_relation = UserCommunity.objects.filter(user_id=request.user.id).values_list('community_id')
        user_communities_ids = [item[0] for item in user_communities_relation]
        
        other_communities = list(Community.objects.exclude(id__in=user_communities_ids))
        
        other_communities = self.get_community_total_members(other_communities)
     
        return other_communities

    def get_community_total_members(self, communities):
        for i in range(len(communities)):
            community_id = communities[i].id
            members_total = UserCommunity.objects.filter(community_id=community_id).count()
            communities[i].members_total = members_total
        return communities

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('signin'))

        communities = self.get_communities(request)
        context = {
            "logged_in": request.user.is_authenticated,
            "communities": communities
        }

        return render(request, "community/all_communities.html", context)

    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('signin'))

        community_id = request.POST['id']
        community_obj = Community.objects.get(pk=community_id)
        UserCommunity.objects.create(
            user=request.user, community=community_obj)

        return redirect('join-community')


class MyCommunitiesView(View):
    def get_communities(self, request):
        user_communities_relation = list(UserCommunity.objects.filter(user_id=request.user.id))
        my_communities = [item.community for item in user_communities_relation]
        user_communities = self.get_community_total_members(my_communities)
        return user_communities

    def get_community_total_members(self, communities):
        for i in range(len(communities)):
            community_id = communities[i].id
            members_total = UserCommunity.objects.filter(community_id=community_id).count()
            communities[i].members_total = members_total
        return communities

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('signin'))

        communities = self.get_communities(request)
        context = {
            "logged_in": request.user.is_authenticated,
            "communities": communities
        }

        return render(request, "community/user_communities.html", context)

    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('signin'))

        community_id = request.POST['id']
        community_obj = Community.objects.get(pk=community_id)
        UserCommunity.objects.get(
            user=request.user, community=community_obj).delete()

        return redirect('remove-community')

class CreateCommunityView(View):
    def get(self,request):
        return render(request,'community/create_community.html',{
            "logged_in": request.user.is_authenticated,
            "error":False
        })

    def post(self,request):
        name = request.POST['name']
        desc = request.POST['description']
        image = request.FILES['image']
        try:
            com = Community.objects.create(community_name=name,description=desc,image=image)
            UserCommunity.objects.create(user_id=request.user.id,community_id=com.id)
        except:
            return render(request,'community/create_community.html',{
                "logged_in": request.user.is_authenticated,
                "error":True,
                "error_text":"Community Already Exists!"
            })
        return redirect('remove-community')
        