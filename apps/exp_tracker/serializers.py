from rest_framework import serializers
from .models import Category, Expense

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class ExpenseSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )
    
    class Meta:
        model = Expense
        fields = [
            "id",
            "category",
            "category_name",
            "amount",
            "description",
            "is_recurring",
            "expense_date",
            "created_at"
        ]
        read_only_fields = ["created_at"]
    
    def validate(self, data):
        if data.get("is_recurring") and not data.get("description"):
            raise serializers.ValidationError(
                "Recurring expenses must have a description."
            )
        return data