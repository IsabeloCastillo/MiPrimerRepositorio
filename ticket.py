class Producto():
    """Clase Producto
    Incluye el codigo, el nombre, el precio y el tipo
    
    args
    - codigo: Es un string que compone el codigo del producto
    - nombre: Es un string que define el nombre del producto
    - precio: Es un float, que define el precio del producto
    - tipo: Es un string que compone el tipo ded producto"""
    
    def __init__(self,codigo,nombre,precio,tipo):
        """Constructor de la clase Producto"""
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__tipo = tipo
        print("🆕Prodcuto creado🆕")
        self.emoji_nombre()
        self.calcular_total()
        
        
    #Getters
    @property
    def codigo(self):
        "Metodo getter del atributo codigo"
        #print("Estoy en el metodo getter de codigo")
        return self.__codigo
    
    @property
    def nombre(self):
        "Metodo getter del atributo nombre"
        #print("Estoy en el metodo getter de nombre")
        return self.__nombre
        
    @property    
    def precio(self):
        "Metodo getter del atributo precio"
        #print("Estoy en el metodo getter de precio")
        return self.__precio

    @property
    def tipo(self):
        "Metodo getter del atributo precio"
        #print("Estoy en el metodo getter de tipo")
        return self.__tipo
    
    # Setters
    @codigo.setter
    def codigo(self,nuevoCodigo):
        """Metodo setter del atributo codigo"""
        #print("Estoy en el setter de codigo")
        self.__codigo = nuevoCodigo
        
    @nombre.setter
    def nombre(self,nuevoNombre):
        """Metodo setter del atributo nombre"""
        #print("Estoy en el setter de nombre")
        self.__nombre = nuevoNombre
        
    @precio.setter
    def precio(self,nuevoPrecio):
        #print("Estoy en el setter de precio")
        self.__precio = nuevoPrecio
        
    @tipo.setter
    def tipo(self,nuevoTipo):
        #print("Estoy en el setter de tipo")
        self.__tipo = nuevoTipo
        
        
    def __str__(self):
        """Metodo __str__() de la clase producto. Indica codigo,nombre,precio y tipo del producto"""
        return "nCodigo>: {}\nNombre>: {}\nPrecio>: {} Euros 💶\nTipo>>>: {}".format(self.__codigo,
                                                                                                        self.__nombre,
                                                                                                        self.__precio,
                                                                                                        self.__tipo)
                                                                            
    
    # funcion para emojis                                                
    def emoji_nombre(self):
        if "z" in self.__codigo:
            self.__nombre = "👟" + self.__nombre
        if "c" in self.__codigo:
            self.__nombre = "👕" + self.__nombre
        if "g" in self.__codigo:
            self.__nombre = "🧢" + self.__nombre
        if "Basket" in self.__tipo:
            self.__tipo = self.__tipo + " 🏀"
        if "Running" in self.__tipo:
            self.__tipo = self.__tipo + " 🏃‍♀️"
        if "Futbol" in self.__tipo:
            self.__tipo = self.__tipo + " ⚽"
            
   
    # Método para calcular el importe total de varios productos        
    def calcular_total(self):
        self.__cantidad = int(input("Introduzca la cantidad: "))
        importe_total = self.__cantidad * self.__precio 
        print("Importe total = ", round(importe_total,2), "Euros","💶")
        return self.__cantidad
        

        
class Pedido():
    """Clase pedido 
        Incluye lista de productos y lista de cantidades
    
        args
        - productos: strings que componen una lista en este caso de pedidos
        - cantidades: integers que componen una lista de cantidades"""
    
    productos = [] #Esta lista contendrá objetos de la clase Producto
    cantidades = []#Esta lista contendrá objetos de la clase Producto
    
    def __init__(self,productos=[],cantidades=[]): 
        self.productos = productos
        self.cantidades = cantidades
        if(len(self.cantidades) == 0):
            print("Se ha creado un pedido vacio")
        else:    
            print("🆕Nuevo Pedido🆕😀 con productos añadidos\n")
        
    def mostrar_productos(self):
        for mp in self.productos:
            print(mp)  # Print toma por defecto str(p)    
            
    def mostrar_cantidades(self):
        for mc in self.cantidades:
            print(mc)  # Print toma por defecto str(p)   
            
    def total_pedido(self):
        total = 0.0
        for i in range(0,len(self.productos)):
            total += self.productos[i].precio * self.cantidades[i]
        print("El importe total de la compra es de:" , total , "Euros💶")
        return total
        
    
    
    def mostrar_pedido(self):
        space = "   " # Lleva 3 "espacios"      
        print("       ARTICULO" , "          PRECIO" , "       UNDS" )#Llevan 7,10,7 "espacios", respectivamentes
        print("       ¯¯¯¯¯¯¯¯" , "          ¯¯¯¯¯¯" , "       ¯¯¯¯" )#Llevan 7,10,7"_" respectivamentes
        for i in range(0,len(self.productos)):
            print(self.productos[i].nombre ,space,"",self.productos[i].precio ,space,space, (self.cantidades[i]))
        print("")
        (self.total_pedido())
        
      
    
    
c01 = Producto(codigo = "c001" , nombre = "Camiseta A.Iniesta" , precio = 69.95 , tipo = "Futbol")
print(c01,'\n')        

g01 = Producto(codigo = "g001" , nombre = "Gorra Micha.Jordan" , precio = 29.95 , tipo = "Basket")
print(g01, '\n')

z01 = Producto(codigo = "z001" , nombre = "Zapatillas Us.Bolt" , precio = 99.99 , tipo = "Running")
print(z01, '\n')

productos = [c01,g01,z01]
cantidades = [5,10,10]
pedido_hoy = Pedido(productos,cantidades)
pedido_hoy.mostrar_pedido()
print("Print de pruebas2"
