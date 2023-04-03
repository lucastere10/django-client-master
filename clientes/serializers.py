from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError("Insira um valor válido de cpf")
        if not nome_valido(data['nome']):
            raise serializers.ValidationError("Insira um valor válido de nome")
        if not rg_valido(data['rg']):
            raise serializers.ValidationError("Insira um valor válido de rg")
        if not celular_valido(data['celular']):
            raise serializers.ValidationError("Insira um valor válido de celular")
        return data