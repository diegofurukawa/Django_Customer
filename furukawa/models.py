from django.db import models


# ========= Cliente | Customer
class Customer(models.Model):
    idCustomer = models.IntegerField(primary_key=True, verbose_name="idCliente")

    cName = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Cliente"
    )
    cPhone = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Telefone"
    )
    cEmail = models.CharField(
        max_length=100, null=True, blank=False, verbose_name="E-mail"
    )
    cVendedor = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Vendedor"
    )
    cDescription = models.CharField(
        max_length=300, null=True, blank=True, verbose_name="Descrição"
    )
    dContractCreated = models.DateField(
        null=True, blank=False, verbose_name="Contrato desde"
    )
    nContractDuration = models.IntegerField(null=True, verbose_name="Tempo de Contrato")

    dCreated = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    dLastUpdate = models.DateTimeField(auto_now_add=True, null=True)


# ========= Contacto | Contact
class Contact(models.Model):
    idContact = models.IntegerField(primary_key=True)

    cName = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Nome Contato"
    )
    cPhone = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Telefone"
    )
    cEmail = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Email"
    )
    dCreated = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    dLastUpdate = models.DateTimeField(null=True)

    idCustomer = models.ForeignKey("Customer", on_delete=models.CASCADE)


# ========= Vendedor | SalesMan
class SalesMan(models.Model):
    idSalesMan = models.IntegerField(primary_key=True)
    cName = models.CharField(max_length=100, null=False, blank=False)
    cPhone = models.CharField(max_length=100, null=False, blank=False)
    cEmail = models.CharField(max_length=100, null=False, blank=False)
    dCreated = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    dLastUpdate = models.DateTimeField(null=True)


# ========= Produto | Product
class Product(models.Model):
    idProduct = models.IntegerField(primary_key=True)
    cProductName = models.CharField(max_length=100, null=False, blank=False)


# ========= Orçamento | Budget
class Budget(models.Model):
    idBudget = models.IntegerField(primary_key=True)
    idProduct = models.ForeignKey("Product", on_delete=models.SET)


# ========= Contrato | Contract
class Contract(models.Model):
    idContract = models.IntegerField(primary_key=True)
    cVendedor = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Vendedor"
    )
    cDescription = models.CharField(
        max_length=300, null=True, blank=True, verbose_name="Descrição"
    )
    dContractCreated = models.DateField(
        null=True, blank=False, verbose_name="Contrato desde"
    )
    nContractDuration = models.IntegerField(null=True, verbose_name="Tempo de Contrato")
    dLastUpdate = models.DateTimeField(null=True)
    idCustomer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    idSalesMan = models.ForeignKey("SalesMan", on_delete=models.CASCADE)
