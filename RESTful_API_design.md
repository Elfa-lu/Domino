> https://restfulapi.net/rest-api-design-tutorial-with-example/

### 1.Identify Object Model
identifying the objects which will be presented as resources  

```
device  
configuration  
```

### 2.Create Model URIs
a device is a top-level resource. And configuration is sub-resource under device  
URIs do not use any verb or operation. **Nouns only** 

```
/devices/{id}/configurations/{id}
```

### 3.Determine Representations
XML or JSON format  

#### Collection of Device Resource
When returning a collection resource, include **only most important information** about resource.  
This will keep the size of payload small, and so will **improve the performance** of REST APIs.  

#### Single Device Resource
include **complete** information of a device in this URI.  
Here, also include a list of links for **sub-resources and other supported operations**. This will make your REST API **HATEOAS** driven.  
Collection may be in two forms **primary collection and secondary collection**.  
Secondary collection is sub-collection from a primary collection only.  
Each resource/collection contain **at least one** link i.e. to itself.  
Having two links is important as you can provide access to a device specific configuration in more **unique manner**  
To get complete information about a resource, you need to access through its specific resource URI only.  

```
<link rel="self" href="/devices/12345/configurations/11223344" />
<link rel="detail" href="/configurations/11223344" />
```

```
<device id="12345"> 
    <link rel="self" href="/devices/12345"/>
 
    <id>12345</id> 
    <deviceFamily>apple-es</deviceFamily> 
    ...
    # more details. won't be included in collection
    <configurations size="2">
        <link rel="self" href="/configurations" />
 
        <configuration id="42342">
            <link rel="self" href="/configurations/42342" />
        </configuration>
 
        <configuration id="675675">
            <link rel="self" href="/configurations/675675" />
        </configuration>
    </configurations>
 
    <method href="/devices/12345/exec-rpc" rel="rpc"/> 
    <method href="/devices/12345/synch-config"rel="synch device configuration"/> 
</device>
```


### 4.Assign HTTP Methods

#### Filter
```
?limit=10
?offset=10 #start from
?page=2&per_page=100
?sortby=name&order=asc
?animal_type_id=1 #where
```

#### Browse all devices or configurations  
```
HTTP GET /configurations?startIndex=0&size=20
```

#### Create a device or configuration
```
HTTP POST /configurations
```

#### Update a device or configuration

#### Remove a device or configuration
A successful response SHOULD be **202 (Accepted)** if resource has been queues for deletion (async operation),  
or **200 (OK) / 204 (No Content)** if resource has been deleted permanently (sync operation).  
Normally, you may want to **SOFT DELETE** a resource in these requests – in other words, set their **status INACTIVE**.  
By following this approach, you will not need to find and remove its references from other places as well.  

#### Status Codes
200 OK - [GET]
201 CREATED - [POST/PUT/PATCH]
202 Accepted - [*]
204 NO CONTENT - [DELETE]
400 INVALID REQUEST - [POST/PUT/PATCH]
401 Unauthorized - [*]
403 Forbidden - [*]
404 NOT FOUND - [*]：record doesn't exist
406 Not Acceptable - [GET]：format not available - JSON-XML
410 Gone -[GET]
422 Unprocesable entity - [POST/PUT/PATCH]
500 INTERNAL SERVER ERROR - [*]

#### Hypermedia API
link to the next step
```
{"link": {
  "rel":   "collection https://www.example.com/zoos",
  "href":  "https://api.example.com/zoos",
  "title": "List of zoos",
  "type":  "application/vnd.yourformat+json"
}}
```

(HATEOAS) - Github
```
{
  "current_user_url": "https://api.github.com/user",
  "authorizations_url": "https://api.github.com/authorizations",
  // ...
}
```



