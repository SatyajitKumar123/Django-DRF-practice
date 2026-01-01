from rest_framework import serializers

class ExpenseSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    amount = serializers.IntegerField()
    category = serializers.CharField(max_length=50)
    notes = serializers.CharField(
        max_length=200,
        required=False,
        allow_blank=True,
        write_only=True
    )
    summary = serializers.CharField(read_only=True)
    
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Amount must be greater than zero."
            )
        return value
    
    def validate(self, data):
        if data.get("category") == "Food" and not data.get("notes"):
            raise serializers.ValidationError({
                "notes": "Notes are required for food expenses."
            })
        return data
    
    def to_representation(self, instance):
        """
        Controls OUTPUT only
        """
        return {
            "title": instance["title"],
            "amount": instance["amount"],
            "category": instance["category"],
            "summary": f'{instance["title"]} - ₹{instance["amount"]}'
        }