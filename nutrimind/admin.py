from django.contrib import admin
from .models import UserProfile, Recommendation, PsychologicalCondition

# Register PsychologicalCondition so it can be managed fromadmin side
admin.site.register(PsychologicalCondition)

# Customize the UserProfile admin interface
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'age', 'weight') 
    search_fields = ('user__username', 'name')       
    
@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('get_psychological_condition', 'meal_plan', 'yoga_exercises')
    search_fields = ('psychological_condition__name',)

    def get_psychological_condition(self, obj):
        return obj.psychological_condition.name
    get_psychological_condition.short_description = 'Psychological Condition'
