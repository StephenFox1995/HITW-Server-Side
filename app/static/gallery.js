
function addImageToGallery(image) {
  $('.gallery').append(galleryItem(image))
  $(".gallery").justifiedGallery();
}

// Returns the ccs for a gallery item.
function galleryItem(image) {
  var src = image.image
  return '<a href="' + src + '">' +
            '<img src= "' + src + '">' +
          '</a>';
}
