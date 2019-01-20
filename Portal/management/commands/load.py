from django.core.management.base import BaseCommand
from django.db import transaction
from Portal.models import Post, Nominee, Voter
import hashlib

POSTS_CSV = 'data/posts.csv'
NOMINEES_CSV = 'data/nominees.csv'
HOUSE_CSV = 'data/house.csv'
VOTERLIST_CSV = 'data/voterlist.csv'

class Command(BaseCommand):

    def posts(self):
        posts = []
        with open(POSTS_CSV, 'r') as f:
            f.readline()
            line = f.readline()[:-1]
            while line:
                _, name, type = line.split(',')
                line = f.readline()[:-1]
                post = Post(
                    name=name,
                    type=type
                )
                posts.append(post)
        Post.objects.bulk_create(posts)

    def nominees(self):
        nominees = []
        with open(NOMINEES_CSV, 'r') as f:
            f.readline()
            line = f.readline()[:-1]
            while line:
                _, name, post, symbol, votes = line.split(',')
                line = f.readline()[:-1]
                post = Post.objects.get(name=post)
                nominee = Nominee(
                    name=name,
                    post=post,
                    symbol=symbol
                )
                nominees.append(nominee)
        with open(HOUSE_CSV, 'r') as f:
            f.readline()
            line = f.readline()[:-1]
            while line:
                _, name, post, house, symbol, votes = line.split(',')
                line = f.readline()[:-1]
                post = Post.objects.get(name=post)
                nominee = Nominee(
                    name=name,
                    post=post,
                    house=house,
                    symbol=symbol
                )
                nominees.append(nominee)
        Nominee.objects.bulk_create(nominees)

    def voters(self):
        inserted = 0
        users = []
        with open(VOTERLIST_CSV, 'r') as f:
            f.readline()
            line = f.readline()[:-1]
            while line:
                _, class_sec, username, name, house, stage, password = line.split(',')
                # print(class_sec, username, name, house, stage, password)
                password = hashlib.md5(password.encode('utf-8')).hexdigest()
                line = f.readline()[:-1]
                user = Voter(
                    username=username,
                    password=password,
                    name=name,
                    class_sec=class_sec,
                    house=house,
                    stage=stage,
                    is_active=True
                )
                users.append(user)
        Voter.objects.bulk_create(users)

    def handle(self, *args, **options):
        self.posts()
        self.nominees()
        self.voters()
