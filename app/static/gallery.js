
function addImageToGallery(image) {
  $('.gallery').append(galleryItem(image))
  $(".gallery").justifiedGallery();

  // $('.gallery').justifyGallery();
  // $('.gallery').bootstrapGallery({
  //   iconset: "fontawesome"
  // });
}

// Returns the ccs for a gallery item.
function galleryItem(src) {
  return '<a href="' + src + '">' +
  '<img src= "' + src + '">' +
  '</a>';
}
