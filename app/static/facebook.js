
/**
Asks the Facebook SDK for the current login status of the user.
@param response A callback with a response object passed.
*/
function getFacebookLoginStatus(response) {
  window.fbAsyncInit = function() {
    FB.init({
      appId      : '1750775448505371',
      cookie     : true,
      xfbml      : true,
      version    : 'v2.5'
    });
    FB.getLoginStatus(response);
  };

  // Load the SDK asynchronously
  (function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));
}

function getFacebookUserToken() {
  return FB.getAuthResponse();
}
