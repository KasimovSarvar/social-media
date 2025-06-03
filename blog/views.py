from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from blog.models import Post, UserLikePost, Comment, UserFollow, Profile, Notification


def acc_view(request):
    return render(request, 'account-setting.html')

@login_required(login_url='/signin/')
def home_view(request):
    followers = UserFollow.objects.filter(follower=request.user).values_list('following', flat=True)
    users_list = User.objects.all().exclude(id=request.user.id).exclude(id__in=followers)[:4]
    posts = Post.objects.filter(author_id__in=followers).order_by('-created_at') or Post.objects.filter(
        author=request.user).order_by('-created_at')

    all_notifications = Notification.objects.filter(receiver=request.user).order_by('-timestamp')[:5]
    comment_notifications = Notification.objects.filter(receiver=request.user, type=2).order_by('-timestamp')[:5]

    d = {
        'all_notifications': all_notifications,
        'comment_notifications': comment_notifications,
        'posts': posts,
        'followers': followers,
        'users_list': users_list
    }


    return render(request, 'index.html', d)


@login_required(login_url='/signin/')
def setting_view(request):
    return render(request, 'setting.html')


def signin_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(username=username)
        if not user:
            return render(request, 'signin.html', {'error': 'Username is incorrect'})

        auth = authenticate(request, username=username, password=password)

        if auth:
            login(request, auth)
            return redirect('/')
        return render(request, 'signin.html', {'error': 'Password is incorrect'})

    return render(request, 'signin.html')


def logout_view(request):
    logout(request)
    return redirect('/signin/')


def signup_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = User.objects.create(username=username, password=make_password(password))
        user.save()
        profile=Profile.objects.create(user=user)
        profile.save()
        return redirect('/signin/')
    return render(request, 'signup.html')


def like_view(request):
    post_id = request.GET.get('post_id')
    author = request.user
    post_author = User.objects.get(post__id=post_id)

    exists = UserLikePost.objects.filter(author=author, post_id=post_id).first()
    if exists:
        exists.delete()

        Notification.objects.filter(
            receiver=post_author,
            sender=author,
            type=1,
            message=f"{author.username} liked your post.",
        ).delete()

        return redirect(f"/#{post_id}")

    obj = UserLikePost.objects.create(author=author, post_id=post_id)
    obj.save()

    Notification.objects.create(
        receiver=post_author,
        sender=author,
        type=1,
        message=f"{author.username} liked your post.",
    )

    return redirect(f"/#{post_id}")

@login_required
def follow_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        author = request.user
        # noti
        sms_user = User.objects.get(id=user_id)

        existing_follow = UserFollow.objects.filter(follower=author, following=sms_user).first()
        if existing_follow:
            existing_follow.delete()

            Notification.objects.filter(
                receiver=sms_user,
                sender=author,
                type=3,
                message=f"{author.username} followed you.",
            ).delete()

        else:
            UserFollow.objects.create(follower=author, following=sms_user)

            Notification.objects.create(
                receiver=sms_user,
                sender=author,
                type=3,
                message=f"{author.username} followed you.",
            )

        return redirect('/')


def create_post_view(request):
    if request.method == 'POST':
        author = request.user
        image = request.FILES['img']
        print(image, '*' * 10)
        post = Post.objects.create(author=author, image=image)
        post.save()
    return redirect('/')


def create_prof_view(request):
    author_username = request.GET.get('post_author_username')
    if author_username:
        follow = UserFollow.objects.filter(follower_id=request.user.id, following_id=author_username).exists()
    else:
        author_username = request.user.id
        follow = None
    posts = Post.objects.filter(author_id=author_username)
    if request.method == 'POST':
        picture = request.FILES['img']
        prof = Profile.objects.filter(user_id=request.user.id).first()
        prof.picture = picture
        prof.save()
        return redirect('/profile/')
    followers = UserFollow.objects.filter(following_id=author_username).count()
    following = UserFollow.objects.filter(follower_id=author_username).count()
    user = Profile.objects.filter(user_id=author_username).first()

    d = {
        'post_len': len(posts),
        'posts': posts,
        'followers': followers,
        'following': following,
        'prof_user': user.user.username,
        'user': user,
        "follow": follow,
    }
    return render(request, 'profile.html', d)


def comment_view(request, pk):
        if request.method == 'POST':
            data = request.POST

            obj = Comment.objects.create(author=request.user, post_id=pk, message=data.get('message'))
            obj.save()

            post_author = obj.post.author
            Notification.objects.create(
                receiver=post_author,
                sender=request.user,
                type=2,
                message=obj.message,
            )

        return redirect(f"/#post-{pk}")


def delete_post_view(request, pk):
    post = Post.objects.filter(author=request.user, id=pk).first()
    if post and request.method == 'POST':
        post.delete()
        return redirect("/")
    return redirect("/")


def search_view(request):
    if request.method == 'POST':
        search_query = request.POST.get('query')
        if not search_query:
            return render(request, 'search.html')
        filter_ = Q(username__icontains=search_query)
        users = User.objects.filter(filter_)
        d = {
            'users': users,
        }
        return render(request, 'search.html', d)
    return render(request, 'search.html')



def settings_view(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('gmail')
        bio = data.get('bio')
        obj = Profile.objects.create(first_name=first_name, last_name=last_name, email=email, bio=bio)
        obj.save()

        return redirect('/setting')


    return render(request, 'setting.html')
