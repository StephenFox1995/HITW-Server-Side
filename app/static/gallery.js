function addGallery(element, images) {
  if (images instanceof Array) {
    $(element).append(galleryBody());

    images.forEach(function(image) {
      $('.row').append(galleryItem(image));
    });
  }
}

// Returns the ccs for a gallery item.
function galleryItem(url) {
  return '<div class="col-lg-3 col-sm-4 col-xs-6"><a title="Image 1" href="#"><img class="thumbnail img-responsive" src="' + url + '"></a></div>';
}

// Reuturns the css for a gallery item.
function galleryBody() {
  var body =
      '<h1>Gallery</h1>' +
      '<div class="row"></div>'
  return body;
}
