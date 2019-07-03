# Github diff proxy

Returns diff url file in a REST API call

```JS
fetch(`http://localhost:8000/?url=${diffURL}`, {method: 'GET'})
      .then(function (data) {
          data.json().then(json => {
              console.log(json);
          }).
          catch(err => {

                  console.log(err);
              }
          );
      })
      .catch(function (error) {
      
      });

```
