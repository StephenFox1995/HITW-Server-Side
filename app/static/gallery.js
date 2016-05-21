function addGallery(element, images) {
  if (images instanceof Array) {
    $(element).append(galleryBody());

    images.forEach(function(image) {
      $('.gallery').append('row', galleryItem(image));
    });
  }

  $('.gallery').bootstrapGallery();
  $('.gallery-overview').bootstrapGallery({
    iconset: "fontawesome"
  });
  $('.gallery').justifyGallery();
}

// Returns the ccs for a gallery item.
function galleryItem(src) {
  return '<a class="col-xs-6 col-sm-4" href="' + src + '">' +
              '<img src= "' + src + '">' +
          '</a>';
}

// Reuturns the css for a gallery item.
function galleryBody() {
  var body = '<h1>Gallery</h1>';
    return body;
}
