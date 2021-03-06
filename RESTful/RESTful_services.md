client (front end) - HTTP - server (back end)
Representational State Transfer: convention for building these HTTP services  
**CRUD**: create read update delete data  
client can sent HTTP request to endpoint to talk to server
HTTP methods: **GET** **POST**(create) **PUT**(update) **DELETE**  
**Eg**: Update a customer  
　　Request: PUT /api/customers/1  {name:''}  
　　Response: {id:1, name:''}  
   
     
    
> https://www.youtube.com/watch?v=FOZtRzY5x8E
### API explanation and clarification  

1. What is an API  
　Application Programming Interface  
　A way to let **software components** to talk to each other  
　Analogy: Object-Oriented Programming: API = the set of **methods / attributes** of the object  

2. How does APIs relate to Web Services?  
　Web services are a set of rules and technologiesi that enable two or more components **on the web** to interoperate
　Web services are **APIs in the context of web**  
　Web services are set of techs and rules enable two or more components on the web to **talk to each other**  
　The first web service used: **WSDL(language) + SOAP(technology:XML/HTTP)**  
　**distributed programming:** end software or system is a set of interlinked components that are located in different computers and communicated with each other thru some protocol(SOAK) despite their programming language.  
　service description using WSDL (**registry queies** (the communication rules))  
　Not every API is a web service  
　**REST API = REST web service** - Web service APIs that adhere to the REST architectural constraints  

3. What is a REST API?  
　an API that follows the rules of REST specification  


### What is REST 
1. How does HTTP relate to REST  
　HTTP: an application layer protocol for sending and receiving messages over a network  
　REST is a specification that dictates how **distributes systems** on the web should communicate  
　REST is a way to implement and use the HTTP protocol  

2. How does the WEB relate to REST  
　REST is the underlying architecture of the WEB  


### Why REST
　**standardization of one type of web services is important**  
  
### RESTful web services
　How can the client tell the service provider which operation it wants to perform? **Method info**  
　　-- should be expressed in the **HTTP verb** (GET/...)  
　How can the client tell the service provider what data to operate on? **Scoping info**  
　　-- should go in the **URI**  
　　EG: DELETE api/users/:userId HTTP/1.1  
  
### How it works  
   HTTP  
   Scoping info goes in the **parameters part of the URI**    
   data exchange format(XML,JSON)  
   communication is stateless  
   
   
______

> https://restfulapi.net/
## Guiding Principles of REST
### Client–server
### Stateless
Each request from client to server must contain **all of the information necessary** to understand the request  
**cannot** store context on the **server**
### Cacheable
Cache constraints require that the data within a response to a request be implicitly or explicitly **labeled as cacheable or non-cacheable**. (client part)
### Uniform interface
four interface constraints: identification of resources; manipulation of resources through representations; self-descriptive messages; and, hypermedia as the engine of application state.  

______
REST uses a **resource identifier** to identify the **particular resource** involved in an interaction between components.  

The **state of the resource** at any particular timestamp is known as **resource representation**. A representation consists of **data, metadata describing the data and hypermedia links** which can help the clients in transition to the next desired state.  

In simplest words, in the REST architectural style, data and functionality are considered **resources** and are accessed using **Uniform Resource Identifiers** (URIs). The resources are acted upon by using a set of simple, well-defined **operations**. The clients and servers **exchange representations of resources** by using a **standardized interface and protocol – typically HTTP**.  

Resources are **decoupled** from their representation so that their content **can be accessed in a variety of formats**, such as HTML, XML, plain text, PDF, JPEG, JSON, and others.  

**Metadata** about the resource is available and used, for example, to **control caching, detect transmission errors, negotiate the appropriate representation format, and perform authentication or access control**. And most importantly, every interaction with a resource is **stateless**.

All these principles help RESTful applications to be **simple, lightweight, and fast**.

