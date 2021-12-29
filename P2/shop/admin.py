from django.contrib import admin

# Register your models here.
from shop.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category_name', 'description']
    search_fields = ['category_name', 'description']
    list_filter = ['category_name']

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'first_name', 'last_name', 'mobile_number', 'is_active']
    search_fields = ['first_name', 'last_name', 'mobile_number']
    list_filter = ['country', 'is_active']

    class Meta:
        model = User


admin.site.register(User, UserAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_id', 'company_name']
    search_fields = ['company_name']

    class Meta:
        model = Company


admin.site.register(Company, CompanyAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'full_name', 'company_name']
    list_filter = ['company']

    def full_name(self, obj):
        result = User.objects.get(user_id=obj.user.user_id)
        return result.__str__()

    def company_name(self, obj):
        result = Company.objects.get(company_id=obj.company.company_id)
        return result.company_name

    class Meta:
        model = Customer


admin.site.register(Customer, CustomerAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'full_name', 'title', 'hire_date']

    def full_name(self, obj):
        result = User.objects.get(user_id=obj.user.user_id)
        return result.__str__()

    class Meta:
        model = Employee


admin.site.register(Employee, EmployeeAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_name', 'category_name', 'unit_price']
    list_filter = ['category']

    def category_name(self, obj):
        result = Category.objects.get(category_id=obj.category.category_id)
        return result.category_name

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'customer_name', 'employee_name', 'order_time']
    list_filter = ['customer']

    def customer_name(self, obj):
        result = Customer.objects.get(customer_id=obj.customer.customer_id)
        return result.user.__str__()

    def employee_name(self, obj):
        result = Employee.objects.get(employee_id=obj.employee.employee_id)
        return result.user.__str__()

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['pk', 'order', 'product', 'unit_price', 'quantity']

    def order(self, obj):
        result = Order.objects.get(order_id=obj.order.order_id)
        return result.__str__()

    def product(self, obj):
        result = Product.objects.get(product_id=obj.product.product_id)
        return result.__str__

    class Meta:
        model = OrderDetail


admin.site.register(OrderDetail, OrderDetailAdmin)