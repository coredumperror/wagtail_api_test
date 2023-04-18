from rest_framework.renderers import JSONRenderer
from wagtail.api.v2.pagination import WagtailPagination
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter

from .models import HomePage

# ======================================================
# Wagtail API v2 Endpoints
# ======================================================
class HomePageAPIViewSet(PagesAPIViewSet):
    name = 'homepage'
    model = HomePage
    renderer_classes = [JSONRenderer]
    # pagination_class = WagtailPagination
    # This forces the API to always output all the fields that we've exposed via the API, instead of requiring that the
    # caller ask for them manually.
    listing_default_fields = PagesAPIViewSet.listing_default_fields + [f.name for f in HomePage.api_fields]

    def get_queryset(self):
        """
        Unlike a normal PagesAPIViewSet, we only want to return HomePages.
        """
        return HomePage.objects.public().order_by('-latest_revision_created_at')

# Create the API router with 'homepage_api' as the URL namespace.
homepage_api_router = WagtailAPIRouter('homepage_api')
# Register the /api/v2/homepage_api... viewset.
homepage_api_router.register_endpoint('homepages', HomePageAPIViewSet)
