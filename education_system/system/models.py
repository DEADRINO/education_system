from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_student = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def create_groups(self, min_users=None, max_users=None):
        users = self.author.user_set.all()

        num_users = len(users)
        num_groups = num_users // self.group_set.first().min_users
        remaining_users = num_users % self.group_set.first().min_users

        for _ in range(num_groups):
            group = Group.objects.create(product=self,
                                         max_users=self.group_set.first()
                                         .max_users)
            for _ in range(self.group_set.first().min_users):
                user = users.pop()
                group.members.add(user)

        if remaining_users:
            group = Group.objects.create(product=self,
                                         max_users=self.group_set.first()
                                         .max_users)
            for _ in range(remaining_users):
                user = users.pop()
                group.members.add(user)

    def add_user_to_group(self, user):
        groups = self.group_set.all().order_by('members__count')

        for group in groups:
            if group.members.count() < group.max_users:
                group.members.add(user)
                break
        else:
            group = Group.objects.create(product=self,
                                         max_users=self.group_size_max)
            group.members.add(user)


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    video_link = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    min_users = models.PositiveIntegerField(default=1)
    max_users = models.PositiveIntegerField()
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def add_member(self, user):
        if self.members.count() < self.max_users:
            self.members.add(user)
        else:
            raise ValueError("Group is full")

    def remove_member(self, user):
        self.members.remove(user)

    def get_members(self):
        return self.members.all()