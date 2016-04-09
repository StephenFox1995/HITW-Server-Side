
/**
@param element The element to set.
@param value The value.
*/

var post_member_url = 'http://localhost:6565/add_member/'
function setTextFieldValue(element, value) {
  element.value = value
}

function addClickOffEvent(element, action) {
  var isClickInside = specifiedElement.contains(event.target);
  if (!isClickInside) {
    action()
  }
}

function POSTMember(firstname, lastname, handicap) {
  window.alert("Attempting..")

  $.ajax({
    url:'http://localhost:6565/add_member/',
    type: 'post',
    content-type: 'application/json',
    data {
      firstname: firstname,
      lastname: lastname,
      handicap: handicap
    },
    success: function(data) {
      window.alert("it worked")
    }
  })
}
