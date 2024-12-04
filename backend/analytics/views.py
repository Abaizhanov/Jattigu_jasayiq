from django.shortcuts import render
from django.db.models import Count
from user.models import User
from blog.models import BlogPost, Comment
import matplotlib.pyplot as plt
import io
import urllib, base64

def analytics_view(request):
    # Total number of blog posts and comments
    total_posts = BlogPost.objects.count()
    total_comments = Comment.objects.count()

    # User demographics (age and gender)
    age_groups = User.objects.values('age').annotate(count=Count('age'))
    gender_distribution = User.objects.values('gender').annotate(count=Count('gender')).order_by('gender')

    # Fitness goal distribution
    fitness_goal_distribution = User.objects.values('fitness_goal').annotate(count=Count('fitness_goal'))

    # Posts and comments per user (activity analysis)
    user_activity = User.objects.annotate(
        num_comments=Count('comment')  # Count the number of comments each user has made
    )

    # Example: Create a chart for gender distribution
    genders = ['Male', 'Female', 'Other']
    gender_counts = [0, 0, 0]  # Default to zero for each gender

    # Fill in the counts for each gender
    for i, gender in enumerate(genders):
        gender_count = gender_distribution.filter(gender=gender).first()
        if gender_count:
            gender_counts[i] = gender_count['count']

    # Create the bar chart
    plt.figure(figsize=(6, 4))
    plt.bar(genders, gender_counts, color=['blue', 'pink', 'gray'])
    plt.title('Gender Distribution of Users')
    plt.xlabel('Gender')
    plt.ylabel('Number of Users')

    # Save the plot to a string and pass it to the template
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    context = {
        'total_posts': total_posts,
        'total_comments': total_comments,
        'age_groups': age_groups,
        'gender_distribution': gender_distribution,
        'fitness_goal_distribution': fitness_goal_distribution,
        'user_activity': user_activity,
        'gender_chart': img_str,  # Pass the image string for the chart
    }
    return render(request, 'analytics/overview.html', context)
