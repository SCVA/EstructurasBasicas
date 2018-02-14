from cola import Cola

a=Cola()
pacientes= ["Juan Domínguez","Lucía Restrepo","Lola Pérez","Camilo Torres","Felipe Gutiérrez"]

[a.encolar(x) for x in pacientes]
print(a.items)

a.desencolar()
print(a.items)

a.encolar("María Vargas")
print(a.items)
