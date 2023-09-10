from django.contrib import admin
from django.urls.resolvers import URLPattern
from django.shortcuts import render
from django.urls import path
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from .models import Product, Category, CategoryProduct, Attribut, Gallery



# ------------------------------------------

# admin.site.index_title = 'Panel Administrativo'
# admin.site.site_header = 'Tienda Virtual NACIOTEX'
# admin.site.site_title = 'Dashboard'
# ------------------------------------------


class GalleryInline(admin.TabularInline):
    model = Gallery


class CategoryProductInline(admin.TabularInline):
    model = CategoryProduct


# class AttributProductInline(admin.TabularInline):
#     model = AttributProduct

# ---------------------------------------------


class AttributAdmin(admin.ModelAdmin):
    list_display = ("name",)
    # inlines = [AttributProductInline]


# class AttributProductAdmin(admin.ModelAdmin):
#     list_display = ('product', 'Attribut',  'detail')


# class ProductEntryDetailAdmin(admin.ModelAdmin):
#    list_display = ('product', 'qty', 'costo', 'iva', 'ProductEntry')


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('active', 'name_extend', 'ref', 'codigo',  'price1', 'flag', 'modified_date')
#     prepopulated_fields = {'slug': ('flag','name_extend')}
#     list_display_links = ('codigo', 'flag','name_extend')
#     search_fields = ('codigo', 'flag', 'ref', 'name_extend')
#     ordering = ('name_extend',)
#     inlines = [GalleryInline, CategoryProductInline]


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "active", 
        "codigo",
        "name_extend",               
        "ref",      
        "price1",
        "price2",
        "flag",
        "modified_date",
    )
    prepopulated_fields = {"slug": ("flag", "name_extend")}
    list_display_links = ("codigo", "flag", "name_extend")
    search_fields = ("codigo", "flag", "ref", "name_extend")
    ordering = ("name_extend",)
    inlines = [CategoryProductInline]

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path("upload-csv/", self.upload_csv),
        ]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES.get("csv_upload")

            if csv_file:
                try:
                    file_data = csv_file.read().decode("utf-8")
                    csv_data = file_data.split("\n")

                    for i, row in enumerate(csv_data):
                        if i == 0:
                            continue  # Skip the header row
                        else:
                            row = row.strip()  # Remove leading/trailing whitespaces
                            # row = row.replace(
                            #     ";", " "
                            # )  # Replace semicolons with spaces
                            row = row.split(';')

                            if len(row) >= 5:
                                try:
                                    # Intenta obtener el producto existente por codigo
                                    product = Product.objects.get(codigo=row[0])
                                except ObjectDoesNotExist:
                                    product = None

                                # Si el producto no existe, crea uno nuevo
                                if product is None:
                                    product = Product(
                                        codigo=row[0],
                                        name_extend=row[1],
                                        description=row[2],
                                        price1=row[3],
                                        price2=row[4],
                                        price_old=row[5],
                                        flag=row[6],
                                        ref=row[7],
                                        slug = row[8].replace(" ", "-"),
                                        active = row[9],
                                        soldout = row[10],
                                        offer = row[11],
                                        home = row[12],                                        
                                    )
                                    product.save()
                                    print(f"Se Creo correctamente")
                                else:
                                    # Si el producto existe, actualiza sus atributos
                                    product.name_extend=row[1],
                                    product.description=row[2],
                                    product.price1=row[3],
                                    product.price2=row[4],
                                    product.price_old=row[5],
                                    product.flag=row[6],
                                    product.ref=row[7],
                                    product.slug = row[8].replace(" ", "-"),
                                    product.active = row[9],
                                    product.soldout = row[10],
                                    product.offer = row[11],
                                    product.home = row[12],                                   
                                    product.save()
                                    print(f"Se Actualizó correctamente")
                except Exception as e:
                    # Manejar errores generales aquí, por ejemplo, registrarlos o mostrar un mensaje de error
                    print(f"Error al procesar el archivo CSV: {str(e)}")

        form = CsvImportForm()
        data = {"form": form}  
        return render(request, "admin/csv_product.html", data)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "slug", "modified_date", "created_date")
    readonly_fields = ("created_date",)
    search_fields = ("name",)

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path("upload-csv/", self.upload_csv),
        ]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES.get("csv_upload")

            if csv_file:
                try:
                    file_data = csv_file.read().decode("utf-8")
                    csv_data = file_data.split("\n")

                    for i, row in enumerate(csv_data):
                        if i == 0:
                            continue  # Skip the header row
                        else:
                            row = row.strip()  # Remove leading/trailing whitespaces
                            # row = row.replace(
                            #     ";", " "
                            # )  # Replace semicolons with spaces
                            row = row.split(';')

                            if len(row) >= 5:
                                try:
                                    # Intenta obtener la categoría existente por nombre
                                    category = Category.objects.get(codigo=row[0])
                                except ObjectDoesNotExist:
                                    category = None

                                # Si la categoría no existe, crea una nueva
                                if category is None:
                                    category = Category(
                                        codigo=row[0],
                                        name=row[1],
                                        slug=row[2].replace(" ", "-"),
                                        image_alterna=row[3],
                                    )
                                    category.save()
                                else:
                                    # Si la categoría existe, actualiza sus atributos
                                    category.name = row[1]
                                    category.slug = row[2].replace(" ", "-")
                                    category.image_alterna = row[3]
                                    category.save()
                except Exception as e:
                    # Manejar errores generales aquí, por ejemplo, registrarlos o mostrar un mensaje de error
                    print(f"Error al procesar el archivo CSV: {str(e)}")

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_category.html", data)


class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ("category", "product", "active", "created_date")
    readonly_fields = ("created_date",)
    list_display_links = ("category", "product")


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Attribut, AttributAdmin)
# admin.site.register(CategoryProduct, CategoryProductAdmin)
# admin.site.register(AttributProduct, AttributProductAdmin)
# admin.site.register(ProductEntryDetail, ProductEntryDetailAdmin)
