## Design

A simple implementation using python requests. Each data type has its own handler. 
Requests are made by instantiating an SDK class, and using its defined handlers to access 
different endpoints.

Individual handlers inherit from the base handler and define dataclasses to match the shape
of incoming data, as well as construct appropriate URLs. The base handler is responsible
for shared logic around making requests, error handling as well as any logic needed for filtering, 
sorting, or pagination.

The end result is a method call like this:

```
r = sdk.movie.get_by_id('5cd95395de30eff6ebccde5d', limit=3)
```

To expand this SDK, simply create new handlers for other data types such as characters or books and define
dataclasses and urls accordingly.

To further improve this SDK, I would improve the user experience around filtering and pagination, 
creating classes to more easily use these features instead of simply passing strings as params
from the method call.