
/**
@param element The element to set.
@param value The value.
*/
function setTextFieldValue(element, value) {
  element.value = value
}

function addClickOffEvent(element, action) {
  var isClickInside = specifiedElement.contains(event.target);
  if (!isClickInside) {
    action()
  }
}
