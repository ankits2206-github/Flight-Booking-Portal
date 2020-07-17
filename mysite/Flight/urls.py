from django.urls import path
from . import views

# . means importing from current dirctory

urlpatterns =[
    path("",views.index,name="index"),
    path("<int:flight_id>",views.flight,name="flight"),
    path("<int:flight_id>/book",views.book,name="book"),
    path("airport",views.airport,name="airport"),
    path("bookairport",views.bookairport,name="bookairport"),
    path("addflight",views.addflight,name="addflight"),
    path("passenger",views.passenger,name="passenger"),
    path("bookpassenger",views.bookpassenger,name="bookpassenger"),
    path("<int:flight_id>/normregister",views.normregister,name="normregister"),
    path("mybookings",views.mybookings,name="mybookings"),
    path("History",views.History,name="History"),
    path("delete",views.delete,name="delete")
]
