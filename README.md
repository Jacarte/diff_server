# Github diff proxy

Returns diff url file in a REST API call

Deploy on ```http://jacarte.pythonanywhere.com```

```JS
fetch(`http://jacarte.pythonanywhere.com/?url=${diffURL}`, {method: 'GET'})
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

## TODO
- This is a proof of concept, Django is a bazooka killing a mosquito in this case ;).
- File cache
