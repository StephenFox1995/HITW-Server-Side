
var done = false
function addImageToGallery(image) {
  $('.gallery').append(galleryItem(image))
  $('.gallery').bootstrapGallery();
  $('.gallery').justifyGallery();
  $('.gallery').bootstrapGallery({
    iconset: "fontawesome"
  });
}

// Returns the ccs for a gallery item.
function galleryItem(src) {
  return '<a href="' + src + '">' +
  '<img src= "' + src + '">' +
  '</a>';
}
