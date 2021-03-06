from django.contrib import admin
from aishack.models import Tutorial, Track, TrackTutorials, Category, AishackUser, TutorialRead, UserTrack, TutorialSeries, TutorialSeriesOrder
from django.contrib.auth.models import User

class TrackTutorialsInline(admin.TabularInline):
    model = TrackTutorials
    extra = 1

class TutorialSeriesInline(admin.TabularInline):
    model = TutorialSeriesOrder

class TrackAdmin(admin.ModelAdmin):
    filter_horizontal = ('tutorials',)
    inlines = (TrackTutorialsInline,)

class TutorialSeriesAdmin(admin.ModelAdmin):
    inlines = (TutorialSeriesInline,)

admin.site.register(Tutorial)
admin.site.register(Track, TrackAdmin)
admin.site.register(TrackTutorials)
admin.site.register(TutorialRead)
admin.site.register(Category)
admin.site.register(UserTrack)
admin.site.register(TutorialSeries, TutorialSeriesAdmin)

# Custom attributes on the user
class AishackUserInline(admin.StackedInline):
    model = AishackUser
    can_delete = False

class UserAdmin(admin.ModelAdmin):
    inlines = (AishackUserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

