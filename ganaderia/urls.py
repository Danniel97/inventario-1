from django.conf.urls import url
from ganaderia.views import (
    index,
    AnimalCreate,AnimalList,AnimalDelete,AnimalUpdate,
    FichaMedicaDelete,FichaMedicaList,FichaMedicaUpdate,FichaMedicaViews,
    EspecieDelete,EspecieList,EspecieUpdate,EspecieViews,
    GeneroViews,GeneroDelete,GeneroList,GeneroUpdate,
    VacunaDelete,VacunaList,VacunaUpdate,VacunaViews,ProductoViews,ProductoList   
    
    )
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [  
   
    url(r'^$',index ),
    # AMINAL#############################################################################333
    url(r'^agregar_ani/',AnimalCreate.as_view(), name='agregar_ani' ),
    url(r'^listar_ani/',AnimalList.as_view(), name='listar_ani' ),
    url(r'^editar_ani(?P<pk>[\w-]+)/$',AnimalUpdate.as_view(), name='editar_ani' ),
    url(r'^eliminar_ani/(?P<pk>\d+)/$',AnimalDelete.as_view(), name='eliminar_ani' ),
    # FICHAMEDICA#############################################################################333
    url(r'^listar_fn/',FichaMedicaList.as_view() , name='listar_fn' ),
    url(r'^editar_fm/(?P<pk>\d+)/$',FichaMedicaUpdate.as_view() , name='editar_fm' ),
    url(r'^agregar_fm/',FichaMedicaViews.as_view(), name='agregar_fm' ),
    url(r'^eliminar_fm/(?P<pk>\d+)/$',AnimalDelete.as_view(), name='eliminar_fm' ),
  # ESPECIE#############################################################################333
    url(r'^listar_esp/',EspecieList.as_view() , name='listar_esp' ),
    url(r'^editar_esp/(?P<pk>\d+)/$',EspecieUpdate.as_view() , name='editar_esp' ),
    url(r'^agregar_esp/',EspecieViews.as_view(), name='agregar_esp' ),
    url(r'^eliminar_esp/(?P<pk>\d+)/$',EspecieDelete.as_view(), name='eliminar_esp' ),
  # GENERO#############################################################################333
    url(r'^listar_gen/',GeneroList.as_view() , name='listar_gen' ),
    url(r'^editar_gen/(?P<pk>\d+)/$',GeneroUpdate.as_view() , name='editar_gen' ),
    url(r'^agregar_gen/',GeneroViews.as_view(), name='agregar_gen' ),
    url(r'^eliminar_gen/(?P<pk>\d+)/$',GeneroList.as_view(), name='eliminar_gen' ),
#  VACUNA#############################################################################333
    url(r'^listar_vac/',VacunaList.as_view() , name='listar_vac' ),
    url(r'^editar_vac/(?P<pk>\d+)/$',VacunaUpdate.as_view() , name='editar_vac' ),
    url(r'^agregar_vac/',VacunaViews.as_view(), name='agregar_vac' ),
    url(r'^eliminar_vac/(?P<pk>\d+)/$',VacunaDelete.as_view(), name='eliminar_vac' ),
    
    # url(r'^pdf/',PDFprueba.as_view(), name='pdf' ),

    url(r'^agregar_pro/',ProductoViews.as_view(), name='agregar_pro' ),
    url(r'^listar_pro/',ProductoList.as_view() , name='listar_pro' ),
]

urlpatterns += staticfiles_urlpatterns()