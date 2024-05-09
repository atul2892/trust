from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('biography/',views.biography),
    path('journey/',views.journey),
    path('achievements/',views.achievements),
    path('speeches/',views.speeches),
    path('speeches-details/<int:id>',views.speechesDetails),
    path('videos/',views.videos),
    path('media-coverage/',views.mediaCoverage),
    path('media-coverage-details/<int:id>',views.mediaCoverageDetails),
    path('news/',views.news),
    path('news-details/<int:id>',views.newsDetails),
    path('gallery/',views.gallery),
    path('videos-gallery/',views.videosGallery),
    path('videos-gallery-details/<int:id>',views.videosGalleryDetails),
    path('daily-updates/',views.dailyUpdates),
    path('daily-updates-details/<int:id>',views.dailyUpdatesDetails),
    path('contact/',views.contact),
    path('business-query/',views.businessQuery),
    path('newsletter-subscription/',views.newsletterSubscription),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
