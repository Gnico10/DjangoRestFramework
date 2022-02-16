from django.urls import path
from rest_framework.routers import DefaultRouter

from api.apiviews import ProductoList, ProductoDetalle, ProductoViewSet
from api.apiviews import CategoriaSave, SubCategoriaSave
from api.apiviews import CategoriaList, SubCategoriaList
from api.apiviews import CategoriaDetalle, SubCategoriaAdd

router = DefaultRouter()
router.register('v2/productos', ProductoViewSet)

urlpatterns = [
    path('v1/productos/', ProductoList.as_view(), name = 'producto_list'),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(), name = 'producto_detalle'),

    path('v1/categoriassave/', CategoriaSave.as_view(), name = 'categoria_save'),
    path('v1/subcategoriassave/', SubCategoriaSave.as_view(), name = 'subcategoria_save'),

    path('v1/categorias/', CategoriaList.as_view(), name = 'categoria_list'),
    # path('v1/subcategorias/', SubCategoriaList.as_view(), name = 'subcategoria_list'),

    path('v1/categorias/<int:pk>', CategoriaDetalle.as_view(), name = 'categoria_detalle'), 
    path('v1/categorias/<int:pk>/subcategorias/', SubCategoriaList.as_view(), name = 'subcategoria_list'),

    path('v1/categorias/<int:cat_pk>/addsubcategoria/', SubCategoriaAdd.as_view(), name = 'addsubcategoria_list'),
]

urlpatterns += router.urls