# **APIViews:**

## **Introduction:**
In this step we are going to use generic views to implements our APIs, we are going to rely on the serializer since it displays the form of data that we are going to present on our views.

The different views allow us to implement different types of HTTP requests.

All the generic views that we are going to use in this tutorial are from `rest_framework.generics` and we are going to inherit from them to implemet them for our views.

### **- CreateAPIView**
Used for create-only endpoints - Provides a `post` method handler.

### **- ListAPIView**
Used for read-only endpoints to represent a collection of model instances - Provides a `get` method handler.

### **- RetrieveAPIView**
Used for read-only endpoints to represent a single model instance - Provides a `get` method handler.

### **- DestroyAPIView**
Used for delete-only endpoints for a single model instance - Provides a `delete` method handler.

### **- UpdateAPIView**
Used for update-only endpoints for a single model instance - Provides `put` and `patch` method handlers.

### **- ListCreateAPIView**
Used for read-write endpoints to represent a collection of model instances - Provides `get` and `post` method handlers.

### **- RetrieveUpdateAPIView**
Used for read or update endpoints to represent a single model instance - Provides `get`, `put` and `patch` method handlers.

### **- RetrieveDestroyAPIView**
Used for read or delete endpoints to represent a single model instance - Provides `get` and `delete` method handlers.

### **- RetrieveUpdateDestroyAPIView**
Used for read-write-delete endpoints to represent a single model instance - Provides `get`, `put`, `patch` and `delete` method handlers.