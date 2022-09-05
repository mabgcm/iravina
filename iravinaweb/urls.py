from django.urls import path
from .views import home, invest, testimonials, news, bus, pro1, pro2, pro3, pro4, pro5, service, contact, partners, translation, tourism, market, media, visa, legal, gov, legalp, logp, edup, tourp

urlpatterns = [
    path('', home, name='home'),
    path('testimonials', testimonials, name='testimonials'),
    path('invest', invest, name='invest'),
    path('news', news, name='news'),
    path('bus', bus, name='bus'),
    path('pro1', pro1, name='pro1'),
    path('pro2', pro2, name='pro2'),
    path('pro3', pro3, name='pro3'),
    path('pro4', pro4, name='pro4'),
    path('pro5', pro5, name='pro5'),
    path('service', service, name='service'),
    path('contact', contact, name='contact'),
    path('partners', partners, name='partners'),
    path('translation', translation, name='translation'),
    path('tourism', tourism, name='tourism'),
    path('market', market, name='market'),
    path('media', media, name='media'),
    path('visa', visa, name='visa'),
    path('legal', legal, name='legal'),
    path('gov', gov, name='gov'),
    path('legalp', legalp, name='legalp'),
    path('logp', logp, name='logp'),
    path('edup', edup, name='edup'),
    path('tourp', tourp, name='tourp'),
]