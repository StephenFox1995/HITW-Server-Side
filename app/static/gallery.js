function addGallery(element, data) {
  if (data instanceof Array) {
    $(element).append(galleryBody());

    data.forEach(function(image) {
      $('.gallery').append(galleryItem(image));
    });
  } else {
    $('.gallery').append(galleryItem(data))
  }

  $('.gallery').justifyGallery();
  $('.gallery').bootstrapGallery();
  $('.gallery-overview').bootstrapGallery({
    iconset: "fontawesome"
  });

}

// Returns the ccs for a gallery item.
function galleryItem(src) {
  return '<a href="' + src + '">' +
              '<img src= "' + src + '">' +
         '</a>';
}

// Reuturns the css for a gallery item.
function galleryBody() {
  var body = '<h1>Gallery</h1>';
    return body;
}
