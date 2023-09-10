from django.contrib import admin
from django.urls.resolvers import URLPattern
from django.shortcuts import render
from django.urls import path
from django import forms
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
        "name_extend",
        "ref",
        "codigo",
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
        return render(request, "admin/csv_product.html")


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
            csv_file = request.FILES.get(
                "csv_upload"
            )  # Use get() to safely get the file

            if csv_file:
                file_data = csv_file.read().decode("utf-8")
                csv_data = file_data.split("\n")

                for i, row in enumerate(csv_data):
                    if i == 0:
                        continue  # Skip the header row
                    else:
                        row = row.strip()  # Remove leading/trailing whitespaces
                        row = row.replace(";", " ")  # Replace semicolons with spaces
                        row = row.split()

                        # Check if row has enough elements to avoid "list index out of range"
                        if len(row) >= 5:
                            category, created = Category.objects.update_or_create(
                                name=row[1],
                                defaults={
                                    "slug": row[2],
                                    "image_alterna": row[3],
                                    "image": row[4],
                                },
                            )

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
